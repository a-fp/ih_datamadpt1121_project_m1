from modules import Acquisition as Ac
from modules import geo_calculations as Ge
import pandas as pd

stations_clean = Ac.stations()
monuments_clean = Ac.monuments()

def mercator_1():
    monuments_clean["Mercator_start"] = monuments_clean.apply(lambda x: Ge.to_mercator(x['Lat_start'],x['Long_start']),axis=1)
    return monuments_clean
def mercator_2():
    stations_clean["Mercator_finish"] = stations_clean.apply(lambda x: Ge.to_mercator(x['Lat_finish'],x['Long_finish']),axis=1)
    return stations_clean

monuments_clean = mercator_1()
stations_clean = mercator_2()

def merge():
    df_sumary = pd.merge(monuments_clean,stations_clean, how="cross")
    return df_sumary