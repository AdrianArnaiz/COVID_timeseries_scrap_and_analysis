# Practica 1: Web Scrapping  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3748050.svg)](https://doi.org/10.5281/zenodo.3748050)

**Resultado del ultimo Scraping automático**: [![Build Status](https://travis-ci.org/AdrianArnaiz/scrap_uoc.svg?branch=master)](https://travis-ci.org/AdrianArnaiz/scrap_uoc)

Caso práctico de la recopilación de datos mediante técnicas de scrapping.


## Autores:
* [**Patricia García Suarez**](mailto:pgarcia054@uoc.edu)
* [**Adrián Arnaiz Rodríguez**](mailto:aarnaizr@uoc.edu) 

## Descripción del proyecto
![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Actualmente nos encontramos ante un suceso histórico, una pandemia a nivel mundial. En dicho contexto, conocer la evolución a lo largo del tiempo de la situación del virus **COVID-19** por países es imprescindible para poder actuar en consecuencia. Si se disponen de buenos datos y un buen modelo, se puede incluso predecir datos futuros para poder prevenir o gestionar de manera más efectica tanto recursos como medidas a tomar. Para ello se ha hecho un estudio riguroso de las diferentes fuentes de datos existentes en la red y nos hemos decantado por worldmeters porque cumple con todas las funcionalidades que buscabamos: variedad en los datos, centralizados, rigurosos y actualizados dinámicamente. Por ello, se ha considerado esta página como un repositorio central de los datos del COVID de la cual se obtiene un dataset principal que se actualizara todos los días a la misma hora gracias al sistema de integración continua Travis-CI.

## Estructura del proyecto
![#f03c15](https://placehold.it/15/f03c15/000000?text=+) En la carpeta principal nos encontramos con el archivo ".travis.yml" el cual contiene la configuración requerida por Travis-CI. Además, estructuramos el resto de ficheros en los siguientes tres directorios:  

* **src/**: Contiene el fichero con el código principal, el .log generado y los requerimientos para Travis CI:
    * Scraping_covid19.py: contiene el código para el scraping y la generación de los csv y el archivo .log
    * log_covid.log: generado por Scraping_covid19.py, recoge información de todos los commits cada vez que se ejecuta
    * requirements.txt: archivo con los requerimientos necesarios para que Travis CI ejecute correctamente el archivo .py  
    
* **doc/**: Contiene la documentación con la respuesta a las preguntas propuestas para la práctica y la tabla de contribuciones en formato RMarkDown y PDF, así como los ficheros necesarios para generar dicho informe.  

* **csv/**: Contiene los ficheros csv generados del scrapping. Estos se dividen en dos subdirectorios:
    * **covid_19_daily/**: ficheros csv con las actualizaciones automáticas de la situación del COVID19 por día obtenidas directamente de worldometers.
    * **covid_19_series/**: ficheros csv generados y actualizados a partir de Scraping_covid19.py

*************
## Bibliografía 
Ensheng Dong, Hongru Du, and Lauren Gardner. An interactive web-based dashboard to track covid-19 in real time. *The Lancet infectious diseases*, 2020.  

Reichard Lawson, *Web scraping with Python*. Packt Publishing Ltd, 2015.  

Max Roser, Hannah Ritchie, and Esteban Ortiz-Ospina. Coronavirus disease (covid-19)-statistics and research. *Our world in Data*, 2020.  

Laia Subirats Mate and Mireia Calvo Gonzalez. Web Scraping. Technical report, UOC, Barcelona, (sf). PID00266970.  

Worldometers. Covid-19 coronavirus pandemic. https://www.worldometers.info/coronavirus/ , 2020.  
