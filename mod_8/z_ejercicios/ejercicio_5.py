import pacientes, pickle, json

def from_json(json_object):
	if type(json_object) == dict:
		elementos = {}
		
		for k,v in json_object.items():
			elementos[k] = pacientes.Paciente(*v)
		return elementos

	return json_object

with open('pacientes.json', encoding="utf-8") as file:
	data_json = json.load(file, object_hook=from_json)

with open('pacientes.pickle', 'rb') as file:
	data_pickle = pickle.load(file)

	print(data_pickle == data_json)