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

class Brujo(Mago, Guerrero):
	pass

if __name__ == '__main__':
	
	brujo = Brujo()
	brujo.atacar()

	#print(Brujo.__mro__)