class Persona:
	def hablar(self, mensaje):
		print(mensaje)

class Profesor(Persona):
	pass

perso = Persona()
profe = Profesor()

perso.hablar("Hola gente!")
profe.hablar("Hola alumnos!")