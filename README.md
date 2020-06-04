# Practica 2: Análisis de datos del Covid  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3748050.svg)](https://doi.org/10.5281/zenodo.3748050)

**Último scraping automático - Fecha del dataset final**: 28 de Mayo de 2020

Caso práctico de la recopilación de datos mediante técnicas de scrapping.


## Autores:
* [**Patricia García Suarez**](mailto:pgarcia054@uoc.edu)
* [**Adrián Arnaiz Rodríguez**](mailto:aarnaizr@uoc.edu) 

## Descripción del proyecto
Actualmente nos encontramos ante un suceso histórico, una pandemia a nivel mundial. En dicho contexto, conocer la evolución a lo largo del tiempo de la situación del virus **COVID-19** por países es imprescindible para poder actuar en consecuencia. Si se disponen de buenos datos y un buen modelo, se pueden hacer análisis para encontrar patrones o incluso predecir datos futuros con el fin de prevenir o gestionar de manera más efectica tanto recursos como medidas a tomar. Para ello se ha hecho un estudio riguroso de las diferentes fuentes de datos existentes en la red y nos hemos decantado por worldmeters porque cumple con todas las funcionalidades que buscabamos: variedad en los datos, centralizados, rigurosos y actualizados dinámicamente. De esta manera, hemos obtenido gracias al sistema de integración continua Travis-CI una serie temporal de información valiosa de la situación de COVID-19 por país desde 30/03/2020 hasta 28/05/2020. Además, para llevar a cabo las pruebas estadísticas se han obtenido datos poblacionales de Worldometers (scraping) y WorldBankData; y datos de indices económicos de Investing (descarga directa). Los análisis realizados se resumen en:

* Contrastes hipótesis:
  * Contraste proporciones Esp-Ita, Esp-Port, Esp-Ale
  * Contraste ANOVA entre continentes
* Correlaciones:
  * Correlación entre proporción de tests y proporción de contagiados.
  * Correlación entre variación de indice y numero de casos. Esp,Ita,Por,US.
* Regresión:
  * Time Series Forecasting: ARIMA
  * Proporción a x días ~ densidad + %gente mayor  + etc

## Estructura del proyecto
En la carpeta principal nos encontramos con el archivo `.travis.yml` el cual contiene la configuración requerida por Travis-CI. Además, estructuramos el resto de ficheros en los siguientes tres directorios:  

* **src/**: Contiene los ficheros con el código de scraping, el .log generado y los requerimientos para Travis CI:
    * `Scraping_covid19.py`: scraping diario, generación de los csv y del archivo .log (parado el 28/30/2020)
    * `log_covid.log`: generado por Scraping_covid19.py, es la información recogida de todos los commits de la ejecución automática
    * `requirements.txt`: archivo con los requerimientos necesarios para que Travis CI ejecute correctamente el archivo .py
    * `scrap_population.py`: scraping puntual de la población mundial en 2020
    
* **doc/**: Contiene la documentación de la Práctica 1 y la Práctica 2, cada una en su correspondiente directorio:
   * **PRA1-Scraping/**: Contiene las respuestas a las preguntas propuestas para la práctica 1, con la tabla de contribuciones en formato RMarkDown y PDF, así como los ficheros necesarios para generar dicho informe.  
   * **PRA2-Analysis/**: Contiene las respuestas a las preguntas propuestas para la práctica 2, todo el código y el procedimiento usado tanto para la limpieza de datos como para su análisis, la tabla de contribuciones en formato RMarkDown y PDF, así como los ficheros necesarios para generar el informe.

* **csv/**: Contiene los ficheros csv generados del scrapping, los descargados y el archivo final obtenido de la limpieza de datos necesario para el posterior análisis.
    * **Investing/**: ficheros csv descargados de la web Investing con datos de índices bursátiles de algunos países
        * `Italy_IT40.csv`
        * `Portugal_PSI20.csv`
        * `Spain_IBEX35.csv`
        * `US_SPX500.csv`
    * **WorldBankData/**: ficheros csv descargados de la web de WorldBankData con datos poblacionales de cada país
    * **covid_19_daily/**: ficheros csv con las actualizaciones automáticas diarias de la situación del COVID19 por país.
    * **covid_19_series/**: ficheros csv de generados y actualizados a partir de `Scraping_covid19.py`.
    * `world_population_2020.csv`: archivo con la población mundial y densidad en 2020 de cada país.
    * `country_40dc_metadata.csv`: **archivo final** tras la concatenación y limpieza de datos.

*************
## Bibliografía 

Christos Agiakloglou and Apostolos Tsimpanos. Spurious correlations for stationary ar (1) processes.

Regis Anne. Arima modelling of predicting covid-19 infections. medRxiv, 2020.

Josep Gibergans Bagena. Contraste de dos muestras. Technical report, UOC, Barcelona, (sf). PID087505702309.

José A Cuesta, Mario Castro, Saúl Ares, and Susanna Manrubia. Predictability: Can the turning point and end of an expanding epidemic be precisely forecast? arXiv preprint arXiv:2004.08842, 2020.

Ensheng Dong, Hongru Du, and Lauren Gardner. An interactive web-based dashboard to track covid-19 in real time. The Lancet infectious diseases, 2020.

Richard Lawson. Web scraping with Python. Packt Publishing Ltd, 2015.

Max Roser, Hannah Ritchie, and Esteban Ortiz-Ospina. Coronavirus disease (covid-19)–statistics and research. Our World in Data, 2020.

G Udny Yule. Why do we sometimes get nonsense-correlations between time-series?–a study in sampling and the nature of time-series. Journal of the royal statistical society, 89(1):1–63, 1926.

Laia Subirats Mate and Mireia Calvo Gonzalez. Web scraping. Technical report, UOC, Barcelona, (sf). PID00256970.

Wikipedia. Spurious relationship. https://en.wikipedia.org/wiki/Spurious_relationship, 2020.

Worldometers. Covid-19 coronavirus pandemic. https://www.worldometers.info/coronavirus/, 2020.

Worldometers. World population by country. https://www.worldometers.info/world-population/population-by-country/, 2020.

Investing. Stock Market Quotes & Financial News. https://www.investing.com/, 2020.
