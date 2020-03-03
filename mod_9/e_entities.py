import sqlite3

#creamos conexion
conexion = sqlite3.connect('pacientes.sqlite3')

#creamos un cursor
cursor = conexion.cursor()

#Creamos los valores
valores = (6, "Matias", "Ferreyra", 28, "No")

#Insertamos los valores
cursor.execute('INSERT INTO pacientes(id, nombre, apellido, edad, diabetico) VALUES(?, ?, ?, ?, ?)', valores)

#confirmamos los cambios
conexion.commit()

#cerramos conexiones
cursor.close()
conexion.close()