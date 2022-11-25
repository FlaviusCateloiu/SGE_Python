nombre = input("Introduce el nombre: ")
sexo = input("Introduce el sexo (H o M): ")

if (sexo == "M" and nombre.lower() < "m") or (sexo == "H" and nombre.lower() > "n"):
    print("Perteneces al grupo A.")
else:
    print("Perteneces al grupo B.")