class Triangulo:
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

		self.area = base * altura / 2

t = Triangulo(4, 3)
print(t.area)

t.base = 10
print(t.area)