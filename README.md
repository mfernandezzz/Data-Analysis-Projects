Este repositorio contiene proyectos de Análisis de Datos con Python.

- Demographic Data Analyzer
En este proyecto se realiza un análisis de datos demográficos utilizando la librería Pandas. El dataset contiene datos demográficos obtenidos de una base de
datos de un Censo realizado en el año 1994.
El objetivo del proyecto es filtrar, extraer y consultar datos como la edad promedio de los hombres, la cantidad y porcentaje de individuos que poseen cada
tipo de formación académica, el porcentaje de individuos con alta cualificación y un salario alto, la cantidad de individuos que trabajan determinada
cantidad de horas por semana y ganan un salario superior, la cantidad y porcentaje de individuos registrados por país con salarios altos y la profesión mas
popular para un país en especifico.

- Medical Data Visualizer
En este proyecto, se realiza un calculo y visualización de datos obtenidos en exámenes médicos. Para dicha visualización se utiliza las librerías Matplotlib y
Seaborn, mientras que para los cálculos se utilizara Pandas y NumPy. 
Las filas del dataset representan pacientes y las columnas representan datos como las medidas corporales, resultados de análisis de sangre y elecciones
en el estilo de vida. 
El objetivo del proyecto es determinar si los pacientes tienen o no sobrepeso, normalizar los datos correspondientes a glucosa y colesterol, mostrar un gráfico
categórico de barras agrupado para visualizar las mediciones de cada análisis para los pacientes con cardio 0 y 1, y mostrar un gráfico de correlación para
visualizar la correlación entre los resultados de los exámenes médicos y los datos físicos de los individuos y sus decisiones de vida.

- Page View Time Series Visualizer
En este proyecto se visualiza la evolución de la cantidad de visualizaciones de un foro web durante el periodo de tiempo comprendido entre Mayo de 2016 y
Diciembre de 2019. Para los cálculos se utiliza la librería Pandas, mientras que vara las visualizaciones se utiliza las librerías Matplotlib y Seaborn.
El objetivo del proyecto es visualizar el crecimiento y/o decrecimiento de las visitas del foro. Previo a la creación de los gráficos, se realiza una limpieza
de los datos para eliminar los outliers. En el apartado de visualizaciones, el primer gráfico de linea muestra la evolución diaria de la cantidad de visitas
del foro, el segundo gráfico de barras agrupado representa la cantidad de visitas que tuvo el foro para cada mes de cada año que se tiene datos, y la ultima
figura contiene dos gráficos de caja, los cuales muestran la distribución de cantidad de visitas del foro anuales y mensuales, respectivamente. 

- Sea Level Predictor
En este proyecto se toma un dataset con registros promedio del nivel del mar obtenidos desde el año 1880. El objetivo es representar dos análisis predictivos,
el primero desde el año 1880 hasta 2050 y el segundo desde el año 2000 hasta 2050. Para la creación del análisis predictivo se utilizara la librería
scipy.stats, mas precisamente, la función lineregress y los métodos .slope / .intercept para el trazado de ambas lineas. Primero se crea un scatter plot con
todos los registros del dataset, luego se traza una linea para predecir la evolución del nivel del mar desde el año 1880 hasta 2050, y luego se traza otra
linea para predecir el aumento del nivel del mar desde el año 2000 hasta 2050.
