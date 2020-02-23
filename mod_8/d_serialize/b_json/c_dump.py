import a_personas, json

def to_json(python_object):            
    if isinstance(python_object, a_personas.Persona):
        return {
            '__class__': 'a_personas.Persona',
            '__value__': {
                'nombre': python_object.nombre,
                'skills': python_object.skills
            }
        }
    raise TypeError(repr(python_object) + ' is not JSON serializable')

data = {
    "personas": [
        a_personas.Persona("Lucas", ["Python", "C++", "JS"]),
        a_personas.Persona("Juan", ["Java", "C#"])
    ]
}

print(data)

with open('datos.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2, default=to_json)