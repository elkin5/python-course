class Punto:
	""" Define las coordenadas x, y, z de un punto en un espacio tridimensional. """

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		clase = type(self).__name__
		return f'{clase}({self.x}, {self.y}, {self.z})'

	def __eq__(self, otro):
		return True if self.x == otro.x and \
			self.y == otro.y and \
			self.z == otro.z \
			else False

if __name__ == '__main__':
	p = Punto(5, -4, 7)

	print(p)
	print(p == Punto(5, -4, 7))
	print(p == Punto(5, -4, 6))