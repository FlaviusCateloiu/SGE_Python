pesoPayaso = 112
pesoMunyeca = 75

print("Introduce el numero de payasos vendidos: ", end="")
numPayasos = int(input())
print("Introduce el numero de muñecas vendidas: ", end="")
numMunyecas = int(input())

print("El peso total del paquete es de ", (numPayasos * pesoPayaso) + (numMunyecas * pesoMunyeca), " g.")