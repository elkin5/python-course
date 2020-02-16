import collections

Punto = collections.namedtuple("Punto", "x y z")

p = Punto(5, 7, 10)

print("x:", p.x)
print("z:", p[-1])
print("Tamaño:", len(p))

print(p)
print(p == Punto(5, 7, 10))