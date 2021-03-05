# Sistema de Plan de Vacunación CEIA-UVG

Este proyecto implementa un sistema de asignación de vacunas, inspirado por la necesidad de asignar vacunas de COVID19, basado en prioridades de edad, factores de riesgo, lugar donde se habita, puesto de trabajo, entre otras. Toma como parámetros de entrada la lista de ubicaciones de centros de vacunación, la lista de pacientes (con toda la información necesaria incluyendo fase de vacunación, factores de riesgo, etc.), la lista de vacunas, la disponibilidad de cada tipo de vacuna y permite agregar lista de pacientes a excluir (por cualquier razón) y permite modificar el plan de asignación en función de las vacunas que realmente se aplicaron (por ejemplo, si gente faltó o si hubo un cambio de última hora).

El proyecto fue implementado por el Centro de Estudios en Informática Aplicada (CEIA) del Instituto de Investigaciones de la Universidad del Valle de Guatemala (UVG). El resultado final es un archivo que consiste en la lista de pacientes en el orden que deben ser vacunados por día y ubicación. Para más información respecto al código, por favor referirse a /docs/build/html/index.html.

# Instrucciones de Uso

## Pasos preliminares

Para utilizar este sistema, primero se deben crear los siguientes archivos de entrada (el nombre de cada archivo y su ubicación pueden ser modificados en config.txt descrito más adelante; a continuación, utilizaremos los nombres default). Nota: Este repositorio incluye archivos de ejemplos para su referencia.

### Clínicas.csv
En el archivo clínicas.csv, introducir cada centro de vacunación, incluyendo el código, el nombre, la capacidad de vacunación por día del centro, el tiempo (en semanas) que toma llevar las vacunas al centro, su ubicación (departamento, municipio, latitud, longitud), y la cantidad de pacientes por fase que se planean vacunar en dicho centro. Actualmente se cuenta con la posibilidad de definir 12 fases distintas llamadas: n1a, n1b, n1c, n2a, n2b, n2c, n2d, n3a, n4a, n4b, n4c, n4d.

### Excluir.csv
El archivo puede estar vació, pero en el caso se desee excluir a ciertos pacientes, es necesario introducir el código del paciente (que coincida con el código en el archivo Pacientes.csv) y la razón para su exclusión.

### Lotes.csv
Este archivo contiene la lista de lotes de vacunas a utilizar. Se debe incluir el código del lote, la fecha de ingreso (en formato día/mes/año), el código de la vacuna (que debe coincidir con el código presente en el archivo Vacunas.csv), el número de vacunas en el lote, y una columna extra vacía al final (que se utiliza en el código para calcular las dosis).

### Pacientes.csv
Este archivo consiste en la información de los pacientes a vacunar. Debe incluir el código del paciente, su información persona (opcional) como NIT, nombre, sexo, numero de afiliado. Obligatoriamente debe incluir fecha de nacimiento, edad, cargo, departamento y municipio donde habita, la dependencia donde será vacunado (departamento, municipio y código que debe coincidir con Clinicas.csv), la fase y subfase a la que pertenece, así como cualquier información de riesgo como si ya tuvo COVID, si es diabético, si tiene sobre peso, si tiene cancer, si tiene VIH o si es paciente renal (estos valores pueden estar vacíos si no se tiene la información pero las columnas deben de existir).

### prioridadCargos.csv
Este archivo contiene la información de la prioridad que se le desea dar a cada cargo. El nombre del cargo debe de coincidir con los cargos en Pacientes.csv, la prioridad puede ser cualquier número de 1 en adelante, entre menor sea el número mayor prioridad. Si se desea que todos los cargos tengan la misma prioridad se puede colocar el mismo número.

### prioridadEdad.csv
Este archivo contiene la información de la prioridad que se le desea asignar a cada rango de edad. Contiene la década de edad a la que el paciente pertenece y la prioridad que se desea. Al igual que en los otros archivos de prioridad, entre menor sea el número (hasta 1) mayor prioridad.

### prioridadMunicipios.csv
Este archivo contiene la información de la prioridad que se asigna al lugar donde se habita. Debe contener un código (que coincida con el archivo Pacientes.csv), el departamento, municipio, el color de semáforo de emergencia, y la prioridad.

### prioridadUnidades.csv
Este archivo contiene la información de la prioridad que se asigna a las unidades de vacunación. Debe incluir el código de la clínica (que debe coincidir con Clinicas.csv y Pacientes.csv), su ubicación, nombre y prioridad.

### prioridadVacunados.csv
Este archivo contiene la información de los pacientes que han sido vacunados en la realidad en cada ubicación, con la vacuna específica y la fecha. Es utilizado para actualizar el plan de vacunación en función de lo que ocurrió en la realidad.

### Vacunas.csv
Este archivo contiene la información de las vacunas. Incluye el código de la vacuna (que debe coincidir con los otros archivos), la marca, el número de dosis necesarios, el tiempo en semanas en que se debe aplicar la segunda dosis, la temperatura a la que se debe guardar y cualquier otra observación.

### Config.txt
Este archivo se utiliza para definir algunos parámetros generales del sistema. Incluye el número de estaciones de vacunación por centro, el número default que se puede vacunar por día, y el tiempo en semanas default que toma para llevar las vacunas a cada centro. También incluye valores de peso en caso se desee ignorar cierto tipo de prioridad o si se le desea asignar un mayor peso. Entre mas grande el número mayor importancia se le da a la prioridad específica. También incluye información de donde se pueden encontrar los archivos necesarios (utilizando un path relativo), y el nombre de los archivos de entrada. Este archivo debe estar en el mismo lugar donde se encuentre el archivo ejecutable.

## Manual de Uso

Una vez los archivos están creados, el programa se corre utilizando el ejecutable con 3 posibles parámetros: -v, -d, o -u. La v y d son para determinar si uno desea o no información extra. La -u es un parámetro muy importante que se utiliza para correr el programa para modificar el plan según las vacunas realizadas en la realidad.
Al correr el programa sin el parámetro -u, el sistema toma todos los archivos y genera un archivo asignaciones.csv que contiene la lista de todos los pacientes en orden, la clínica donde se debe vacunar, con la vacuna que les corresponde y la fecha de la primera y segunda dosis. 

Una vez la vacunación empiece, es posible que la gente vacunada difiera con la del plan, por lo que es necesario actualizar las segundas dosis. Para eso, es necesario actualizar la lista en Vacunados.csv y correr el programa con el parámetro -u. En ese caso, la salida será un nuevo archivo asignaciones_reales_dosis_2.csv que contiene cuando se debe realizar la segunda dosis para las personas que fueron vacunadas en la realidad.

Para cualquier duda, por favor contactar a Juan F. Mancilla-Caceres, Ph.D. a jfmancilla@uvg.edu.gt.

