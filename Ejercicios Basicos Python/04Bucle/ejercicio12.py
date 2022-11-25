frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

cont = 0
for i in frase:
    if i == letra:
        cont += 1

print("La letra '{0}' aparece {1} veces en la frase '{2}'." .format(letra, cont, frase))