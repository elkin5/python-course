import sqlite3

#creamos conexion
conexion = sqlite3.connect('pacientes.sqlite3')

#creamos un cursor
cursor = conexion.cursor()
print(type(cursor))

#creamos una tabla
cursor.execute('CREATE TABLE if not exists pacientes(id integer PRIMARY KEY, nombre text, apellido text, edad integer, diabetico text)')

#cerramos conexiones
cursor.close()
conexion.close()


