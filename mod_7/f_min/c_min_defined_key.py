def suma_de_valores(palabra):
	""" Retorna la sumatoria de valores ASCII de todas las letras de una palabra"""

	#para cadena vacía
	if not palabra:
		return 0

	#Sumatoria de ord() de cada letra
	val = 0
	for letra in palabra:
		val += ord(letra)

	return val

if __name__ == '__main__':

	frase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed imperdiet risus massa, non varius arcu. "

	minimo = min(frase.split(), key=suma_de_valores)
	maximo = max(frase.split(), key=suma_de_valores)

	print("Mínimo:", minimo, "| Suma ascii:", suma_de_valores(minimo))
	print("Máximo:", maximo, "| Suma ascii:", suma_de_valores(maximo))