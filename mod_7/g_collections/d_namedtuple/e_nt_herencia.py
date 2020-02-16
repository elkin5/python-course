from collections import namedtuple
from math import sqrt

_Punto = namedtuple("_Punto", "x,y,z")

class Punto(_Punto):

	def distancia(self, otro):
		""" Distancia entre dos puntos """

		dif_x = (self.x - otro.x) ** 2
		dif_y = (self.y - otro.y) ** 2
		dif_z = (self.z - otro.z) ** 2

		return sqrt(dif_x + dif_y + dif_z)

if __name__ == '__main__':
	p = Punto(5, 4, 7)

	print("p:", p)
	print("distancia:", p.distancia(Punto(8, 4, 9)))