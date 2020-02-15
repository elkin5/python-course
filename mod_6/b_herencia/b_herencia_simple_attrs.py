class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Alumno(Persona):
    pass


alumno = Alumno("Lucas", "Lucyk")
print(alumno.nombre)
