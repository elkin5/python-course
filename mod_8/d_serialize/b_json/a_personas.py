class Persona:
	def __init__(self, nombre, skills=[]):
		self.nombre = nombre
		self.skills = skills

	def add_skill(self, skill):
		if skill not in self.skills:
			self.skills.append(skill)

	def __repr__(self):
		return f'{type(self).__name__}(nombre={self.nombre}, skills={self.skills})'