from collections import namedtuple

Usuario = namedtuple("Usuario", "nombre, mail, clave")

user = Usuario("lucaslucyk", "lucaslucyk@lucaslucyk", "AzulSchool")

user2 = user._replace(mail="lucaslucyk@lucaslucyk.com", clave="otraClave")

print(user)
print(user2)

user2.clave = "Intento cambia la clave"