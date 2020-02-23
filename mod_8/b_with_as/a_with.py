#abrimos y guardamos en variable file
with open("lorem.txt") as file:
	
	#imprimimos el contenido en caso de ser posible
	print(file.read() if file.readable() else "No se puede leer.") 