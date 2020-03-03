with open("lorem.txt") as file:
	
	#guardamos e imprimimos hasta encontrar un salto de línea
	lineas = file.readlines(1)
	print(type(lineas), "| Elementos:", len(lineas))
	print("Var lineas:", lineas)

	[print(line) for line in file.readlines()]
