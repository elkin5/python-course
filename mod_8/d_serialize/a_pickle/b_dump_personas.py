import pickle, a_personas
	
data = {"personas": []}

p1 = a_personas.Persona("Lucas")
p2 = a_personas.Persona("Juan")

p1.add_skill("Python")
p2.add_skill("Java")

data["personas"].append(p1)
data["personas"].append(p2)

with open('personas.pickle', 'wb') as file:
	pickle.dump(data, file)

print(data)