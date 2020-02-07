class Humano:
	def atacar(self):
		print("Puñetazo!")

class Rey(Humano):
	pass

class Mago(Humano):
	def atacar(self):
		print("Hechizo!")

class Guerrero(Humano):
	def atacar(self):
		print("Espada!")

if __name__ == '__main__':
	
	humano = Humano()
	rey = Rey()
	mago = Mago()

	humano.atacar()
	rey.atacar()
	mago.atacar()