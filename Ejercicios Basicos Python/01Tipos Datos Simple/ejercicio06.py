print("Introduce un numero positivo: ", end="")
num = int(input())
if num >= 0:
    print(num * (num + 1) / 2)
else:
    print("Tienes que introducir un numero positivo.")