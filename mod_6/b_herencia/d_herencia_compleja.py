class Punto:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Circulo(Punto):
	def __init__(self, x, y, radio):
		super().__init__(x, y)	#Punto.__init__(self, x, y)
		self.radio = radio
		

c = Circulo(2, 7, 5)

print ("x:", c.x)
print("y:", c.y)
print("r:", c.radio)

