import sqlite3

#creamos conexion
conexion = sqlite3.connect('pacientes.sqlite3')

#creamos un cursor
cursor = conexion.cursor()

#obtenemos todos los registros y guardamos en registros
cursor.execute('SELECT * FROM pacientes')
registros = cursor.fetchall()

#recorremos e imprimimos todos los registros
[print(registro) for registro in registros]

#cerramos conexiones
cursor.close()
conexion.close()