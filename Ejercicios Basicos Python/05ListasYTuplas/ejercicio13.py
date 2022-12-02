numeros = input("Introduce numeros separados por comas: ")
listaNum = numeros.split(",")
suma = 0
sumsq = 0
for i in range(len(listaNum)):
    suma += int(listaNum[i])
    sumsq += i**2
media = suma/len(listaNum)
desviacionTipica = (sumsq/len(listaNum)-media**2)**(1/2)
print(f"La media es {media}, y la desviacion tipica es {desviacionTipica}")