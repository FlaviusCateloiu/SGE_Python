vocales = ['a', 'e', 'i', 'o', 'u']
palabra = input("Introduce una palabra: ")

for vocal in vocales:
    count = 0
    for letra in palabra:
        if letra == vocal:
            count += 1
    print(str(vocal) + " sale " + str(count))