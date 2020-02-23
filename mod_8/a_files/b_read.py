file = open("lorem.txt")

print(file.read(50))	#primeros 50 caracteres
print(file.read(50))	#Siguientes 50 caracteres

print(file.read())		#Todo el contenido restante

file.close()