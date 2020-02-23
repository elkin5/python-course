import json

with open('datos.json', encoding="utf-8") as file:
	data = json.load(file)

	print(type(data))

	for persona in data["personas"]:
		[print(k, v) for k,v in persona.items()]