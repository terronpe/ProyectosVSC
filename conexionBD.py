#Para conectar con la BD

!pip install mysql-connector-python

import mysql.connector

# Configura los parámetros de conexión
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "terronpe",
    "database": "sakila"
}

# Crea una conexión a la base de datos
conn = mysql.connector.connect(**db_config)

# Ahora puedes ejecutar consultas SQL utilizando 'conn'