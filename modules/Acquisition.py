# -*- coding: utf-8 -*-

import requests
import pandas as pd

def monuments():
    response = requests.get('https://datos.madrid.es/egob/catalogo/208844-0-monumentos-edificios.json')
    resultado = response.json()
    monuments = pd.json_normalize(resultado['@graph'])
    monuments["Type of place"]= "Edificios de carácter monumental"
    monuments = monuments.rename(columns={"title": "Place of interest", "address.street-address": "Place address", "location.longitude": "Long_start", "location.latitude": "Lat_start"}, errors="raise")
    monuments_clean = monuments[["Place of interest","Type of place","Place address","Long_start","Lat_start"]]
    monuments_clean['Lat_start'] = pd.to_numeric(monuments_clean['Lat_start'],errors = 'coerce')
    monuments_clean['Long_start'] = pd.to_numeric(monuments_clean['Long_start'],errors = 'coerce')
    monuments_clean = monuments_clean.fillna(0)
    return monuments_clean

def stations():
    stations = pd.read_json("data/bicimad_stations.json", orient='records')
    geometry_coordinates = stations["geometry_coordinates"].str.split(expand=True)
    geometry_coordinates.columns = ['LONGITUD', 'LATITUD']
    geometry_coordinates['LONGITUD'] = geometry_coordinates['LONGITUD'].str.replace("[","")
    geometry_coordinates['LONGITUD'] = geometry_coordinates['LONGITUD'].str.replace(",","")
    geometry_coordinates['LATITUD'] = geometry_coordinates['LATITUD'].str.replace("]","")
    stations = pd.concat([stations, geometry_coordinates], axis=1)
    stations_clean = stations.rename(columns={"name": "BiciMAD station", "address": "Station location", "LONGITUD": "Long_finish", "LATITUD": "Lat_finish"}, errors="raise")
    stations_clean = stations_clean[["BiciMAD station","Station location","Long_finish","Lat_finish"]]
    stations_clean['Lat_finish'] = pd.to_numeric(stations_clean['Lat_finish'],errors = 'coerce')
    stations_clean['Long_finish'] = pd.to_numeric(stations_clean['Long_finish'],errors = 'coerce')
    stations_clean = stations_clean.fillna(0)
    return stations_clean