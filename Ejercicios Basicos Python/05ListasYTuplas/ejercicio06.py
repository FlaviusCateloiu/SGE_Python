asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobadas = []

for i in asignaturas:
    nota = float(input(f"Introduce la nota de {i}: "))
    if nota >= 5:
        aprobadas.append(i)

for i in aprobadas:
    asignaturas.remove(i)

print(f"Las asignaturas que tienes que repetir son estas: {asignaturas}")
