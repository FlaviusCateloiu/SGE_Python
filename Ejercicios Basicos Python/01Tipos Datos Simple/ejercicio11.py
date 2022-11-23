print("Introduce la cantidad de dinero para la cuenta ahorro: ", end="")
dinero = float(input())

for i in range(3):
    dinero = dinero + ((dinero * 4) / 100)
    print("El año ", i + 1, " has ahorado ",  round(dinero, 2))
