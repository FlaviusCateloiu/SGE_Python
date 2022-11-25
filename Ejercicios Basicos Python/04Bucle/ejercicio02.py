edad = int(input("Introduce tu edad: "))
for i in range(edad):
    if (i + 1) == 1:
        print("Has cumplido", (i + 1), "año.")
    else:
        print("Has cumplido", (i + 1), "años.")