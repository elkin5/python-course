import sqlite3

#creamos conexion
conexion = sqlite3.connect('pacientes.sqlite3')

#creamos un cursor
cursor = conexion.cursor()

#seteamos el campo diabetico = No para todas las edades menor a 50
cursor.execute('UPDATE pacientes SET diabetico = "No" WHERE edad < 50')

#Imprimimos los registros que fueron afectados por la sentencia ejecutada
print("Registros afectados:", cursor.rowcount)

#Confirmamos los cambios
conexion.commit()

#obtenemos todos los registros y guardamos en registros
cursor.execute('SELECT * FROM pacientes')
registros = cursor.fetchall()

#recorremos e imprimimos todos los registros
[print(registro) for registro in registros]

#cerramos conexiones
cursor.close()
conexion.close()