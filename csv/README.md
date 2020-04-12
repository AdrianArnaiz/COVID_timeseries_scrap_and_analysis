# Dataset final
 
Directorio donde guardamos todos los datasets resultados del scrapping. Sin embargo, nosotros tratamos las tablas resultanes de cada scrapping para hacer un dataset final alojado en el directorio `./covid_19_series`. 

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3748050.svg)](https://doi.org/10.5281/zenodo.3748050)

Este dataset está alojado en *Zenodo*. Sin emabargo, la particularidad de este dataset es que se actualiza diariamente. En zenodo hay una primera versión de la fecha 10/04. Se irá actualizando en versiones sucesivas (cuando pasen un número considerable de días, para no crear una versión diferente en zenodo por día).

## Descripción
La descripción individual del dataset se encontrará en cada directorio

* **daily**: un csv por cada scraping realizado que contendrá la tabla de datos de worldometers (paises x dato) (raw data).
* **series`**: un csv por dato a analizar su variabilidad en el tiempo por países (paises x fecha) (processed data).