import json
data = {
    "personas": [
        {
            "nombre": "Lucas",
            "apellido": "Lucyk",
            "pais": "Argentina"
        },
        {
            "nombre": "Juan",
            "apellido": "Perez",
            "pais": "México"
        },
        {
            "nombre": "Ana",
            "apellido": "Gonzalez",
            "pais": "Uruguay"
        },
    ]
}

with open('datos.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4) 