class Vivienda:
	def abrir_puerta(self):
		print ("Abriendo puerta.")

class Persona:
	def ingresar_vivienda(self, vivienda):
		vivienda.abrir_puerta()
		# Asumimos que una vivienda debe poseer el método abrir_puerta


departamento = Vivienda()
perso = Persona()

perso.ingresar_vivienda(departamento)