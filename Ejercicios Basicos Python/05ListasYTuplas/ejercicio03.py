subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for i in subjects:
    notas.append(int(input(f"Introduce la nota de {i}: ")))

print()
for i in range(len(subjects)):
    print(f"En {subjects[i]} has sacado {notas[i]}.")