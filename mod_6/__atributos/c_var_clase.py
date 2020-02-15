class Automovil:
    ruedas = 4
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color


auto_1 = Automovil("Audi", "Negro")
auto_2 = Automovil("BMW", "Gris")

print(auto_1.ruedas)
print(auto_2.ruedas)
