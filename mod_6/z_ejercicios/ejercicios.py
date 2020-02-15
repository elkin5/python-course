class Punto:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	@property
	def cuadrante(self):
		if self.x >= 0 and self.y >= 0:
			return 1
		elif self.x >= 0 and self.y < 0:
			return 2
		elif self.x < 0 and self.y < 0:
			return 3
		else:
			return 4

class Vector:
	def __init__(self, punto_1, punto_2):
	    self.a = punto_1
	    self.b = punto_2

	@property
	def ab(self):
		return (self.b.x - self.a.x, self.b.y - self.a.y)
	
class Guerrero:
	def __init__(self):
		self.vida = 100
		self.estado_arma = 100
		self.estado = "ataque"
		self.estado_escudo = 100	
	
	def atacar(self, objetivo):
		if self.estado_arma >= 2 and self.estado == "ataque" and objetivo.is_alive:
			
			self.estado_arma -= 2

			if objetivo.estado == "defensa":
				objetivo.estado_escudo -= 5
			elif objetivo.estado == "ataque":
				objetivo.vida -= 20

	@property
	def is_alive(self):
		return True if self.vida > 0 else False

	@property
	def estado(self):
		return self._estado
		
	@estado.setter
	def estado(self, estado):
		if estado != "defensa" and estado != "ataque":
			raise ValueError("Los estados pueden ser defensa o ataque")

		if estado == "defensa" and self.estado_escudo <= 0:
			raise ValueError("No puede estar en modo defensa con escudo dañado")

		self._estado = estado


if __name__ == '__main__':
	#tests

	p1 = Punto(5, -3)
	print(p1.cuadrante)

	v1 = Vector(Punto(2, 3), Punto(5, 5))
	print(v1.ab)

	warrior_1 = Guerrero()
	warrior_1.estado = "defensa"

	warrior_2 = Guerrero()
	warrior_2.atacar(warrior_1)

	print(warrior_1.vida, warrior_1.estado_escudo, warrior_2.estado_arma)
