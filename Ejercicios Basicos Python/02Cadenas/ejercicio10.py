print("Introduce los productos de la cesta separados por comas.")
productosCesta = input()

productos = productosCesta.split(",")

for i in productos:
    print(i)