import sqlite3

conexion = sqlite3.connect(':memory:')

print(type(conexion))

