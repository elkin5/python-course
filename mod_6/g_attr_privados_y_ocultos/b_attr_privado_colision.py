class Canasta:

	CAPACIDAD_MAXIMA = 10

	def __init__(self, contenido):
		self._contenido = contenido

	def contenido(self):
		return min(self.CAPACIDAD_MAXIMA, self._contenido)

c = Canasta(5)
cc = Canasta(15)

print("c:", c.contenido())
print("cc:", cc.contenido())