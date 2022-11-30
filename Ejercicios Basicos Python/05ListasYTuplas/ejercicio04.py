ganadores = []
for i in range(6):
    ganadores.append(int(input("Introduce un número ganador: ")))

ganadores.sort()
print("Los números ganadores son " + str(ganadores))