from math import sqrt

class Punto:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distancia(self, otroPunto):
		delta_x = self.x - otroPunto.x
		delta_y = self.y - otroPunto.y

		return sqrt(delta_x ** 2 + delta_y ** 2)

p1 = Punto(1, 2)
p2 = Punto(3, 4)

print(p1.distancia(p2) == Punto.distancia(p1, p2))
