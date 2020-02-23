import webbrowser

fileName = "pagina_python.html"
lineas = [
	'<!DOCTYPE html>\n',
	'<html lang="es">\n',
	'\t<head>\n',
	'\t\t<meta charset="utf-8">\n',
	'\t\t<title>Python Web</title>\n',
	'\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n',
	'\t</head>\n',
	'\t<body>\n',
	'\t\t<p>Esto es una página web creada en Python!!</p>\n',
	'\t</body>\n',
	'</html>\n',
]

with open(fileName, mode="w", encoding="utf-8") as file:
	file.writelines(lineas)

webbrowser.open(fileName)