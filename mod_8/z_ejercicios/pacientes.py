from collections import namedtuple

class Paciente(namedtuple("_Paciente", "id, nombre, apellido, edad, diabetico")):
	""" Datos de pacientes """

	@property
	def es_diabetico(self):
		return True if self.diabetico == "Sí" else False