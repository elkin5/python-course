file = open("lorem.txt")

print("posición 1:", file.tell())
print(file.read(50))	#primeros 50 caracteres

#vemos la posición actual y nos desplazamos al inicio
print("posición 2:",file.tell())
file.seek(0)
print("posición 3:",file.tell())

print(file.read(50))	#primeros 50 caracteres
print("posición 4:",file.tell())

file.close()