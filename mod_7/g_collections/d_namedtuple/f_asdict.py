from collections import namedtuple

Persona = namedtuple("Persona", "nombre, apellido, genero")

p = Persona("Lucas", "Lucyk", "M")
dd = p._asdict()

print(type(dd))

for k,v in dd.items():
	print(k, ">>", v)