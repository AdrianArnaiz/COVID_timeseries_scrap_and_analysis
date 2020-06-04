# Dataset final
 
Directorio donde guardamos todos los datasets resultados del scrapping, descarga directa de "WorldBankData" e "Investing" y el dataset final resultante de la limpieza de datos. 

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3748050.svg)](https://doi.org/10.5281/zenodo.3748050)

Este dataset está alojado en *Zenodo*. Sin emabargo, la particularidad de este dataset es que se actualiza diariamente. En zenodo hay una primera versión de la fecha 10/04. Se irá actualizando en versiones sucesivas (cuando pasen un número considerable de días, para no crear una versión diferente en zenodo por día).

## Descripción
La descripción individual del dataset se encontrará en cada directorio

* **WorldBankData/**: ficheros csv descargados de la web de WorldBankData con datos poblacionales de cada país.
  * `Metadata_Country.csv`
  * `Metadata_Indicator_API_SP.POP.65UP.TO.ZS_DS2_en_csv_v2_1121570.csv`
  * `UP65_Percentage.csv`
  
* **covid_19_daily/**: un csv por cada scraping realizado que contendrá la tabla de datos de worldometers (paises x dato) (raw data).

* **covid_19_series/**: un csv por dato a analizar su variabilidad en el tiempo por países (paises x fecha) (processed data).

* **Investing/**: ficheros csv descargados de la web Investing con datos de índices bursátiles de algunos países.

* `world_population_2020.csv`: archivo con la población mundial y densidad de dicha población en 2020 de cada país.

* `country_40dc_metadata.csv`: **archivo final** tras la unión y limpieza de datos.
