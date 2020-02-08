class Punto:
	pass

def setear_x(self, valor):
	self.x = valor

Punto.setear_x = setear_x

p1 = Punto()
p1.setear_x(25)

print(p1.x)