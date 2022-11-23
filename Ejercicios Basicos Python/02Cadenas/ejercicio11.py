producto = input("Introduce el nombre del producto: ")
precioProd = float(input("Introduce el precio del producto: "))
numUnidadesProd = int(input("Introduce el numero de unidades del producto: "))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = numUnidadesProd, precioProd = precioProd, total = numUnidadesProd * precioProd))


