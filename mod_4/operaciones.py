def suma(*args):
	num = 0
	for arg in args:
		num += arg
	return num

def producto(*args):
	num = 1
	for arg in args:
		num *= arg
	return num

OPERACIONES = {
	"suma": suma,
	"producto": producto,
}

def operacion(*args, **kwargs):
	return OPERACIONES.get(kwargs.get("operacion"))(*args)

if __name__ == '__main__':

	print(operacion(2, 3, 4, operacion="suma"))
	print(operacion(2, 3, 4, operacion="producto"))
