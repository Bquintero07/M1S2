inventarys = []
product = {"Name" : "", "Price" : 0.0, "Quantity" : 0}

print("=======Bienvenido al control de inventario=======")

while True:
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Calcular Estadisticas")
    print("4. salir")
    try:
        option = int(input("Ingrese el numero de la opcion que desea realizar: "))
        if option < 1 or option > 4:
            raise ValueError
        if option == 1:
            name = input("\nIngrese el nombre del producto: ")
            price = float(input("Agregue el precio del producto: "))
            quantity = int(input("Ingrese la cantidad solicitada del producto: "))
            product = {"Name" : name, "Price" : price, "Quantity" : quantity}
            inventarys.append(product)
        elif option == 2:
            if len(inventarys) != 0:
                print("\nEstos son los porductos en la lista")
                for inventary in inventarys:
                    print(f"{inventary}\n")
            else:
                print("\nNo hay ningun producto en la lista aun.\n")
        elif option == 3:
            print("opcion 3")
        elif option == 4:
            break
    except ValueError as e:
        print(f"Error {e}: la entrada no es un numero valido, intenta de nuevo.")
    

