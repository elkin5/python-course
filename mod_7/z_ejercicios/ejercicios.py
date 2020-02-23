from collections import namedtuple, Counter, defaultdict

Pizza = namedtuple("Pizza", "tamanyo, precio, ingredientes")
pizzas = []

#Ejercicio 2
pedidos = [
	["XL", 100, ["Queso", "Jamón"]],
	["XL", 120, ["Queso", "Pepperoni"]],
	["M", 80, ["Queso", "Piña"]],
	["S", 60, ["Queso"]],
	["M", 70, ["Pepperoni"]],
	["L", 90, ["Queso", "Pepperoni"]],
	["L", 80, ["Queso", "Tomates"]],
]

for tamanyo, precio, ingredientes in pedidos:
	pizzas.append(Pizza(tamanyo, precio, ingredientes))


#Ejercicio 3
ingredientes = []
for pizza in pizzas:
	ingredientes.extend(pizza.ingredientes)

ranking_ingredientes = Counter(ingredientes)
print(ranking_ingredientes.most_common(1))

#Ejercicio 4
rank_ing = defaultdict(int)
rank_ing.update(ranking_ingredientes)

print(rank_ing["Pepperoni"], rank_ing["Pepinillos"])

#ejercicio 5
tamanyo_precios = defaultdict(list)
for pizza in pizzas:
	tamanyo_precios[pizza.tamanyo].append(pizza.precio)

for k,v in tamanyo_precios.items():
	print(k, "min:", min(v))
	print(k, "max:", max(v))