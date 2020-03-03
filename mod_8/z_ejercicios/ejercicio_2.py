import pacientes

data = {}

with open("pacientes.txt", encoding="utf-8") as file:
	#lista de líneas del archivo pacientes.txt
	lineas = file.readlines()

	for linea in lineas:
		#elimino los caracteres 
		_id, nombre, apellido, edad, diabetico = linea.replace("\n", "").split(";")

		#creo objetos y los guardo en data
		data[_id] = pacientes.Paciente(int(_id), nombre, apellido, int(edad), diabetico)
