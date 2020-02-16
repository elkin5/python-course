class Numeros:
	def __init__(self, *args):
		self.valores = args

	def __int__(self):
		if not self.valores:
			return 0

		#número con la sumatoria de todos los valores del objeto
		suma = sum(self.valores)
		return suma

	def __float__(self):
		if not self.valores:
			return 0.0
			
		return sum(self.valores) / len(self.valores)

if __name__ == '__main__':
	nn = Numeros(1, 2, 3)

	print(float(nn))