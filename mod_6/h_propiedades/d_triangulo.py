class Triangulo:
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	@property
	def base(self):
		return self._base

	@base.setter
	def base(self, base):
		if base < 0:
			raise ValueError("La base no puede ser un número negativo")
		self._base = base
	
t = Triangulo(4, 5)
print(t.base)
t.base = 10
t.base = -50