import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import os
import time
import logging

path_daily = r'../csv/covid_19_daily/'
path_series = r'../csv/covid_19_series/'



#Insertamos mensajes de log, porque el objetivo es automatizar la ejecución y así sabemos que hha pasado en cada una.
# Nos referimos a automatizar el lanzamiento automático del script.

logging.basicConfig(filename='log_covid.log', format='[|%(asctime)s| - %(name)s - %(levelname)s] - %(message)s', level=logging.INFO)
logging.info('\n')
logging.info('|--------------------|')
logging.info('|INICIO DEL SCRAPPING|')
logging.info('| - Patricia Garcia  |')
logging.info('| - Adrian Arnaiz    |')
logging.info('|--------------------|')


#Creamos lógica de reintentos por fallo de conexión (excepciones) y por fallo en la pagina (statuscode)
page=None
rt=0
connected=False
while rt<=2:
    try:
        page = requests.get('https://www.worldometers.info/coronavirus/')
        if page.status_code==200:
            connected=True
            break
        rt+=1
        logging.warning('Fallo en la pagina: '+str(page.status_code)+' - Reintento: '+str(rt))
        time.sleep(3)
    except Exception as ex:
        logging.warning('Fallo en la conexion: '+ str(ex)+' - Reintento: '+str(rt))
        rt+=1
        time.sleep(3)

if connected:
    logging.info('Conexion completada con exito - 200')

    try:
        soup = BeautifulSoup(page.content, features="html.parser")
        table = soup.find("table", {"id" : "main_table_countries_today"})
        table_head = table.find("thead")
        table_body = table.find("tbody")

        # Extraemos el header
        df_head = [x.text for x in table_head.find_all('th')]

        # Ahora creamos una lista de listas con todos los datos
        # De cada uno de los países
        df_data = []
        for x in table_body.find_all('tr'):
            data = [y.text for y in x.find_all('td')]
            df_data.append(data)

    except Exception as ex:
        logging.warning("FALLO al scrapear")
        raise Exception('Fallo al scrapear')

    logging.info('Datos extraidos satisfactoriamente de la pagina')
    # Creamos el dataset con pandas con la fecha y hora de hoy
    df_covid19 = pd.DataFrame(df_data, columns=df_head, index=list(range(1, len(df_data)+1)))
    #Establecemos como índice el país
    df_covid19 = df_covid19.set_index(['Country,Other'])
    #Convertimos las columnas a número: para ello reemplazar la ',' que marca los miles
    df_covid19.replace([',',' '],'', regex=True, inplace=True)
    df_covid19 = df_covid19.apply(pd.to_numeric)

    #Guardamos el csv diario: Añadimos fecha al nombre del csv por si hay mas de 1 ejecución en un día
    now = dt.datetime.now()
    nombre_csv = now.strftime("%Y-%m-%d__%Hh_%Mm_%S")
    df_covid19.to_csv(path_daily+r'{}_covid19.csv'.format(nombre_csv))
    logging.info('Guardado csv daily: '+nombre_csv)
    

    #Vamos a hacer timeSeries de algunas de las variable santeriormente sacadas
    nombre_columna = now.strftime("%Y/%m/%d %H:%M:%S")
    time_series_var = ['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases', 'TotalTests']

    for var in time_series_var:
        csv_path = path_series+var+'_covid19_timeserie.csv'
        try:
            if not os.path.exists(csv_path):
                #Creamos "csv", elegimos el índice (países) y la columna de nuestra variable renombrada con la fecha
                new_df = pd.DataFrame(df_covid19[var].rename(nombre_columna))
                new_df.to_csv(csv_path)
                logging.info('CREADO csv:'+csv_path)
            else:
                #Leemos la serie temporal de esa variable (poniendo index el pais)
                df_series = pd.read_csv(csv_path, index_col=0)
                #Añadimos columna. Con concat añade respetando indices (si hay nuevos añade filas, si no hay de los antiguos deja a Nan)
                df_series = pd.concat([df_series, df_covid19[var].rename(nombre_columna)], axis=1, sort=False)
                #Guardamos csv
                df_series.index.name = 'Country'
                df_series.to_csv(csv_path)
                logging.info('ACTUALIZADO csv:'+csv_path)
        except: 
            logging.warning('Fallo al actualizar la serie temporal de: '+var)
    
logging.info('FIN\n')
