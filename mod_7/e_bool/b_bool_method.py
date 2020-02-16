class Guerrero:
	def __init__(self, nombre):
		self.nombre = nombre
		self.vida = 100

	def __bool__(self):
		return True if self.vida > 0 else False


if __name__ == '__main__':
	g1 = Guerrero("Thor")

	print(bool(g1))

	g1.vida = 0
	print(bool(g1))