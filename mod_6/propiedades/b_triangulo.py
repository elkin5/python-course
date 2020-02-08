class Triangulo:
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	def area(self):
		return self.base * self.altura / 2

t = Triangulo(4, 3)
print(t.area())

t.base = 10
print(t.area())


tt = Triangulo(-5, 2)
print(tt.area())