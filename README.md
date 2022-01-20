
<p align=“left”><img src=“https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png”></p>

## **Which is the nearest BiciMad station?:no_bicycles:**
*Ironhack Madrid - Data Analytics Part Time - Noviembre 2021 - Proyecto Módulo 1*

Using the **Data Pipeline** you calculate the nearest BiciMad station from any monument in Madrid.

## **Data:books:** 
There are 2 main datasources:

- **Azure SQL Database** The database contains information from the BiciMAD stations including their location (i.e.: latitude / longitude).

- **API REST**. We will use the API REST from the [Portal de datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/) for download the data from the monuments.

## **Executing program: :arrow_forward:**

Enter in the terminal:
```bash
    Python main.py -f "parameter"
```
The parameters are: 'all' or 'minimum':

- **“minimum”:** With 'minimum', you will get a table with the address of the nearest BiciMAD station from the monumemt that you choose, and it will download as `.csv` .
- **“all”:**  With 'all', you will get a table with the address of the nearest BiciMAD station from the monumemt that you choose, and it will download as `.csv` .

## **Project Main Stack: :bulb:**

- [Azure SQL Database](https://portal.azure.com/)
- [SQL Alchemy](https://docs.sqlalchemy.org/en/13/intro.html) (alternatively you can use _Azure Data Studio_)
- [Requests](https://requests.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)
- Module `geo_calculations.py`
- [Argparse](https://docs.python.org/3.7/library/argparse.html)
(10 kB)
https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png
- [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/)



















 


 

