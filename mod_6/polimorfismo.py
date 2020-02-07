class Persona:
	def saludar(self):
		return "Hola"

class Profesor(Persona):
	def saludar(self):
		print(super().saludar() + " alumnos.")

class Alumno(Persona):
	def saludar(self):
		print(super().saludar() + " profesor.")


#Instancias...

alumno = Alumno()
profesor = Profesor()

profesor.saludar()
alumno.saludar()

