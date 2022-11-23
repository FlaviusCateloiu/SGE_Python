producto = input("Introduce el nombre del producto: ")
precioProd = float(input("Introduce el precio del producto: "))
numUnidadesProd = int(input("Introduce el numero de unidades del producto: "))
print('{producto}: {precio:6.2f}€ x {unidades:3d} unidades = {total:8.2f}€'.format(producto = producto, unidades = numUnidadesProd, precio = precioProd, total = numUnidadesProd * precioProd))


