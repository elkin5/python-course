import sqlite3

#creamos conexion
conexion = sqlite3.connect('pacientes.sqlite3')

#creamos un cursor
cursor = conexion.cursor()

#obtenemos únicamente los registros de diabéticos
cursor.execute('SELECT name from sqlite_master where type= "table"')
registros = cursor.fetchall()

#imprimimos los valores obtenidos
[print(registro) for registro in registros]

#cerramos conexiones
cursor.close()
conexion.close()