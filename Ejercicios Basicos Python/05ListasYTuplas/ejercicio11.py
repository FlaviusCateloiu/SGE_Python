tupla1 = (1, 2, 3)
tupla2 = (-1, 0, 2)
producto = 0
for i in range(len(tupla1)):
    producto += tupla1[i] * tupla2[i]

print(f"El producto de {tupla1} con {tupla2} es {producto}.")