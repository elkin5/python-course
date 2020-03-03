import sqlite3

#creamos conexion
conexion = sqlite3.connect('pacientes.sqlite3')

#creamos un cursor
cursor = conexion.cursor()

#Creamos una tabla medicos con los campos id y apellido
cursor.execute('CREATE TABLE if not exists medicos(id integer PRIMARY KEY, apellido text)')

#Creamos una lista de datos. Cada elemento es una tupla de valores
data = [(1, "Rodriguez"), (2, "Pérez"), (3, "Álvarez"), (4, "Acevedo")]

#Insertamos los valores pasando la lista de valores
cursor.executemany("INSERT INTO medicos VALUES(?, ?)", data)

#confirmamos los cambios
conexion.commit()

#obtenemos únicamente los registros de diabéticos
cursor.execute('SELECT * FROM medicos')
registros = cursor.fetchall()

#imprimimos los valores obtenidos
[print(registro) for registro in registros]

#cerramos conexiones
cursor.close()
conexion.close()