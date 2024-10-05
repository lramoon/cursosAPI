Pasos para crear la api

 - 1 Instalar el entorno virtual como buena práctica.

    Para instalar el entorno virtual debes hacerlo de la siguiente forma.

    Desde el directorio del proyecto ejecutas el siguiente comando desde el cmd o powershell (En caso de windows)

    py -m pip install virtualenv

    Eso instalar el entorno virtual de forma global, luego debes instalarlo en tu directorio de la aplicación de la siguiente forma:

    py -m virtualenv phyton_modules

    phyton_modules son las dependencias a utilizar en el entorno virtual para valga la redundancia instalar otras dependencias necesarias para la API.

    Luego debes entrar al directorio phyton_modules/scripts/
    
    Y debes ejecutar activate.bat (En caso de windows) para inicializar el entorno virtual.

    Al ejecutarlo saldra algo parecido

    (phyton_modules) C:\ruta\a\tu\directorio\phyton_modules\Scripts>

    al salir el phyton_modules entre () al inicio significa que ya estamos ejecutando el entorno virtual.

- 2 Instalar Flask para crear la API.
 
    Para instalar flask debes ejecutar el siguiente comando:

    pip install flask

- 3 Luego de eso debes irte a la raiz del proyecto
    (phyton_modules) C:\ruta\a\tu\directorio\

    y crear el directorio APP donde estaran los endpoints de tu API.

- 4 Luego debes crear el primer archivo de prueba en este caso categoria.py

    importando las dependencias necesarias e inicializando el proyecto para ver si ya se puede acceder a la API.

- 5 Luego de hacer pruebas neceitamos la siguiente dependencias para conectarnos a base de datos MySQL.
    
    pip install flask-sqlalchemy
    <!-- Para definir schemas de la DB -->
    pip install flask-marshmallow
    pip install marshmallow-sqlalchemy
    <!-- Driver para conectarnos a la DB MySQL PD: se necesitan drivers para conectarse a diferentes DB como MongoDB,etc. -->
    pip install pymysql

#DOCS
https://docs.sqlalchemy.org/en/20/dialects/mysql.html