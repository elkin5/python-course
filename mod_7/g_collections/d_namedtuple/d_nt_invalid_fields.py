import collections

Usuario = collections.namedtuple(
	"Usuario",
	"_password, nombre, 123",
	rename=True)

print(Usuario._fields)