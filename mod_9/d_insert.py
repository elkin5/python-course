import sqlite3, csv

#creamos conexion
conexion = sqlite3.connect('pacientes.sqlite3')

#creamos un cursor
cursor = conexion.cursor()

#abrimos el archivo en modo lectura con codificacion utf-8
with open('pacientes.txt', encoding="utf-8") as f:

	#utilizamos el método DictReader del módulo csv.
	#El mismo nos devuelve un objeto DictReader que podemos iterarlo como a una lista
	cf = csv.DictReader(f, delimiter=';') 

	#Recorremos todos los elementos devueltos por DictReader
	for fila in cf:

		#Creamos una sentencia sql accediendo al valor de cada columna en cada una se las filas
		sql = f'INSERT INTO pacientes values({fila["id"]}, "{fila["apellido"]}", "{fila["nombre"]}", {fila["edad"]}, "{fila["diabetico"]}")'
		
		#Imprimimos la sentencia sql creada
		print(sql)

		#ejecutamos la sentencia sql
		cursor.execute(sql)

#confirmamos los cambios
conexion.commit()

#cerramos conexiones
cursor.close()
conexion.close()