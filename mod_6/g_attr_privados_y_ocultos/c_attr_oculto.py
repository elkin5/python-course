class Usuario:
	def __init__(self, nombre, contenido_premium):
		self.nombre = nombre
		self.__contenido_premium = contenido_premium

user = Usuario("Lucas Lucyk", "Curso de Python")

print(user.nombre)
#print(user.__contenido_premium)
print(user._Usuario__contenido_premium)