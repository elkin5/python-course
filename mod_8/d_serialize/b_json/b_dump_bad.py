import a_personas, json

data = {
    "personas": [
        a_personas.Persona("Lucas", ["Python", "C++", "JS"]),
        a_personas.Persona("Juan", ["Java", "C#"])
    ]
}

print(data)

with open('datos.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2) 