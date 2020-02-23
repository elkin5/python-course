class Persona:
	def __init__(self, nombre):
		self.nombre = nombre
		self.skills = []

	def add_skill(self, skill):
		if skill not in self.skills:
			self.skills.append(skill)