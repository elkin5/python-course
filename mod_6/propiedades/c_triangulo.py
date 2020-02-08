class Triangulo:
	def __init__(self, base, altura):
		self._base = base
		self._altura = altura

	def set_base(self, base):
		if base < 0:
			raise ValueError("La base no puede ser un número negativo")
		self._base = base

	def set_altura(self, altura):
		if altura < 0:
			raise ValueError("La altura no puede ser un número negativo")
		self._altura = altura


t = Triangulo(4, 3)
t.set_base(-4)


