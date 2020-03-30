import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
page = requests.get('https://www.worldometers.info/coronavirus/')
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

# Creamos el dataset con pandas con la fecha de hoy
df_covid19 = pd.DataFrame(df_data, columns=df_head, index=list(range(1, len(df_data)+1)))
df_covid19.to_csv(r'{}_covid19.csv'.format(dt.date.today()))

