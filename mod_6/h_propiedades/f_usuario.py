class Usuario:
	def __init__(self, password):
		self._passwords = []
		self.password = password

	@property
	def password(self):
		return None if not len(self._passwords) else self._passwords[-1]

	@password.setter
	def password(self, password):
		if len(password) < 8:
			raise ValueError("El password debe tener 8 dígitos como mínimo")
		self._passwords.append(password)

	@password.deleter
	def password(self):
		self._passwords = []


if __name__ == '__main__':
	user = Usuario("ClaveNumero1")
	print("Clave actual:", user.password)

	user.password = "SegundaClaveAsignada"
	print("Clave actual:", user.password)

	print("Historial de claves:", user._passwords)

	del user.password
	print("Clave actual:", user.password)
	print("Historial de claves:", user._passwords)