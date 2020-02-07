class Persona:
	def hablar(self, mensaje):
		print(mensaje)

class Profesor(Persona):
	pass

profe = Profesor()

print(isinstance(profe, Profesor))
print(isinstance(profe, Persona))

profe.hablar("Hola!")