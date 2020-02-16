class Punto:
	""" Define las coordenadas x, y, z de un punto en un espacio tridimensional. """

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

if __name__ == '__main__':
	p = Punto(5, -4, 7)

	print("x:", p.x)
	print("y:", p.y)
	print("z:", p.z)

	print(p)