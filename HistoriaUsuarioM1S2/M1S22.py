from Functions import addproduct, showinventories, statics



#Variables para uso del programa.
inventories = []
product = {"Name" : "", "Price" : 0.0, "Quantity" : 0}
counter = 0
total = 0

print("=======Bienvenido al control de inventario=======")

#ciclo que permite la iteracion del menu.
while True:
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Calcular Estadisticas")
    print("4. salir")
    #try y except para manejo de excepciones de tipado.
    try:
        option = int(input("Ingrese el numero de la opcion que desea realizar: "))
        # control de las opciones del menu.
        if option == 1:
            name = input("\nIngrese el nombre del producto: ")
            price = float(input("Agregue el precio del producto: "))
            quantity = int(input("Ingrese la cantidad solicitada del producto: "))
            addproduct(inventories, name, price, quantity)
        elif option == 2:
            showinventories(inventories)
        elif option == 3:
            statics(option, inventories, counter, total)
        elif option == 4:
            #finalizamos el programa.
            break
        else:
            print("selecciones un valor valido en las opciones del menu.")
    except ValueError as e:
        print(f"Error {e}: la entrada no es un numero valido, intenta de nuevo.")