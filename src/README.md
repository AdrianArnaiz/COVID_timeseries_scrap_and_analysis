**Resultado del ultimo Scraping automático**: [![Build Status](https://travis-ci.org/AdrianArnaiz/scrap_uoc.svg?branch=master)](https://travis-ci.org/AdrianArnaiz/scrap_uoc)

# Código del scrapping

* Scraping realizado sobre [worldometer - coronavirus](https://www.worldometers.info/coronavirus/). El objetivo es scrapear diariamente la tabla de datos para tratarla y conseguir actualizar las series temporales de los diferentes datos por país.

* Scraping puntual realizado sobre [worldometer - population](https://www.worldometers.info/coronavirus/).

## Autores:
* [**Patricia García Suarez**](mailto:pgarcia054@uoc.edu)
* [**Adrián Arnaiz Rodríguez**](mailto:aarnaizr@uoc.edu) 


## Ficheros

### Práctica 1

* `Scraping_covid19.py`: ejecución del scraping. Hace el scraping de la página para obetener los datos, el tratamiento necesario de la tabla para actualizar los correspondientes csv finales, reintentos, tratatamiento de excepciones y salida verbose a un log.
* `log_covid.log`: log de la ejecución de los scraping. Tiene un valor añadido, ya que como se actualiza mediante un bot de Travis, podemos ver el resultado, horas, posibles problemas...
* `requirementes.txt`: fichero de requerimientos para su ejecución en python.

### Práctica 2

* `scrap_population.py`: scraping puntual que obtiene la cantidad y densidad de población de cada país en 2020.

## Instalación y ejecución

### Instalación

1. Clonar el repositorio
2. Crear entorno virtual de python. **Python 3.6**.
3. Instalar requirements (preferiblemente pip). `pip install -r requirements.txt`

### Ejecución

Ejecutar **desde este directorio** (*/src*) el script `Scraping_covid19.py`. Se actualizará el log con el resultado y los csv en su carpeta correspondiente.
