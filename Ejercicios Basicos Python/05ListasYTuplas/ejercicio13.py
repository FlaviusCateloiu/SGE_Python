import math

numeros = input("Introduce numeros separados por comas: ")
listaNum = numeros.split(",")
suma = 0
sumsq = 0
for i in range(len(listaNum)):
    suma += int(listaNum[i])
    sumsq += int(listaNum[i])**2
media = suma/len(listaNum)
desviacionTipica = math.sqrt((sumsq/len(listaNum)-media**2))
print(f"La media es {media}, y la desviacion tipica es {desviacionTipica}")
