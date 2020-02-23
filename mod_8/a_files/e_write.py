file = open("lorem.txt", "a+")

#comprobamos y leemos 50 caracteres
print("Es readable?:", file.readable())
print(file.read(50))

#comprobamos y escribimos texto lorem
print("Es writable?:", file.writable())

cadena = """
Donec et massa pulvinar, dictum ante rutrum, laoreet odio. Interdum et malesuada fames ac ante ipsum primis in faucibus.\
Duis ultrices augue eu pellentesque dictum. Curabitur ut nunc semper, pulvinar sapien pretium, viverra dolor.\
Vestibulum pulvinar vehicula elit, at congue. \
"""
file.write(cadena)

#nos desplazamos al comienzo de la cadena agregada con:
#posició actual + largo de lectura hasta el final - el largo de la cadena creada
file.seek(file.tell() + len(file.read()) - len(cadena))

#leemos e imprimimos desde dicha posición
print(file.read())

#cerramos el archivo
file.close()