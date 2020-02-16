frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

print(min(frase.split(), key=len))
print(max(frase.split(), key=len))