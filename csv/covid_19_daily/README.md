# Dataset final secundario
 
Aunque nuesto objetivo final eran los datasets obtenidos en el directorio `csv/covid_19_series`, guardaremos el resultado de cada scraping. Es decir, estos csv son los diferentes scraping realizados, el diferente estado de la tabla de datos de worldometer en diferentes instantes de tiempo.

Guardamos estos csv por si alguien quiere hacer un tratamiento diferente al realizado por nosotros.

Directorio donde se alojarán un csv por cada scrapping realizado: un csv por día (o más de uno).

La nomenclatura del fichero csv será `y-m-d__Hh_Mm_S.csv`.
* *d*: día.
* *m*: mes.
* *y*: año.
* *H*: hora.
* *M*: minutos.
* *S*: segundos.

Cada fichero tendrá como **filas los países** de los que se han obtenido datos, y **columnas las siguientes:
*  **TotalCases**
*  **NewCases**
*  **TotalDeaths**
*  **NewDeaths**
*  **TotalRecovered**
*  **ActiveCases**
*  **Serious,Critical**
*  **Tot Cases/1M pop**
*  **Deaths/1M pop**
*  **TotalTests**
*  **Tests/1M pop**

Sin embargo, cabe destacar que, si worldometers añade columnas con nueva información, el script está diseñado para que dinámicamente obtenga todas las columnas, incluso las nuevas.
