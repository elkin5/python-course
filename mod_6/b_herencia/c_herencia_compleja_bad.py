class Punto:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Circulo(Punto):
	def __init__(self, radio):
		self.radio = radio

c = Circulo(2, 7, 5)
