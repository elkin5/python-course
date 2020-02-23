import pickle, a_personas

with open('personas.pickle', 'rb') as file:
	data = pickle.load(file)

	for persona in data["personas"]:
		print(persona.nombre, persona.skills)