import json, a_personas

def from_json(json_object):
	if '__class__' in json_object:
		if json_object['__class__'] == 'a_personas.Persona':
			return a_personas.Persona(**json_object['__value__'])
	return json_object

with open('datos.json', encoding="utf-8") as file:
	data = json.load(file, object_hook=from_json)

	for persona in data["personas"]:
		print(persona)