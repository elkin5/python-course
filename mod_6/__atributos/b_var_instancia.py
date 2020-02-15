class Persona:
    def __init__(self, valor_nombre, valor_edad):
        self.nombre = valor_nombre
        self.edad = valor_edad

persona_1 = Persona("Lucas", 25)
persona_2 = Persona(valor_nombre="Juan", valor_edad=30)

print("Nombre:", persona_1.nombre)
print("Edad:", persona_2.edad)
