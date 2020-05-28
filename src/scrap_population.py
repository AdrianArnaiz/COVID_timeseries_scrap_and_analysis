import pandas as pd
import requests
from bs4 import BeautifulSoup

path_csv = r'../csv/'
page = requests.get('https://www.worldometers.info/world-population/population-by-country/')

soup = BeautifulSoup(page.content, features="html.parser")
table = soup.find("table", {"id": "example2"})
table_head = table.find("thead")
table_body = table.find("tbody")

# Extraemos el header
df_head = [x.text for x in table_head.find_all('th')[1:6]]

# Ahora creamos una lista de listas con todos los datos
# De cada uno de los países
df_data = []
for x in table_body.find_all('tr')[:]:
    data = [y.text for y in x.find_all('td')[1:6]]
    df_data.append(data)

# Creamos el dataset con pandas
df_population = pd.DataFrame(df_data, columns=df_head, index=list(range(1, len(df_data) + 1)))
# Establecemos como índice el país
df_population = df_population.set_index(['Country (or dependency)'])
# Convertimos las columnas a número: para ello reemplazar la ',' que marca los miles
df_population.replace([',', ' ', 'NA', 'N/A'], '', regex=True, inplace=True)
df_population = df_population.drop(['Yearly Change', 'Net Change'], axis=1)
df_population = df_population.apply(pd.to_numeric)

# Guardamos el csv
df_population.to_csv(path_csv + r'world_population_2020.csv')
