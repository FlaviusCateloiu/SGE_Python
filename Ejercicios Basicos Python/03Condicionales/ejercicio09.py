edadCliente = int(input("Introduce tu edad: "))
if edadCliente < 4:
    precioEntrada = 0
elif edadCliente <= 18:
    precioEntrada = 5
else:
    precioEntrada = 10

print("Tienes que pagar ", precioEntrada, "€ por la entrada.")