class Persona:
	def __init__(self, nombre, secreto):
		self.nombre = nombre
		self._secreto = secreto

p = Persona("Juan", "Prefiere Java")

print("Nombre:", p.nombre)
print("Secreto:", p._secreto)