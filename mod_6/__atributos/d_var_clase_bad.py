class Perro:
    trucos = []
    def __init__(self, nombre):
        self.nombre = nombre


p1 = Perro("Firulais")
p2 = Perro("Ayudante de Santa")

p1.trucos.append("saltar")
p2.trucos.append("rodar")

print(p1.trucos)
print(p2.trucos)
