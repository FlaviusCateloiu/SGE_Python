tipoPizza = input("Que tipo de pizza quieres Vegetariana (V) o No (N): ")
if tipoPizza == "V":
    print("Elige uno de los ingredientes vegetarianos: Pimiento o Tofu.")
    ingrediente = input()
    print("La pizza es vegetariana y contiene los ingredientes:", ingrediente.lower(), ", mozzarella y tomate.")
else:
    print("Elige uno de los ingredientes no vegetarianos: Peperoni, Jamón y Salmón.")
    ingrediente = input()
    print("La pizza es no vegetariana y contiene los ingredientes:", ingrediente.lower(), ", mozzarella y tomate.")
