file = open("lorem.txt")

print("Es seekable?:", file.seekable())
file.seek(50)
print("Posición:", file.tell())

print("Es readable?:", file.readable())
print(file.read(50))

print("Es writable?:", file.writable())

try:
	print(file.write("Escribo contenido..."))
finally:
	file.close()
