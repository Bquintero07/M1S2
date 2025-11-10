# Variables para uso del programa.
inventarys = []
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
        if option < 1 or option > 4:
            raise ValueError
        elif option == 1:
            #se piden los datos por input, se asignan al diccionario y luego el diccionario se agrega a la lista.
            name = input("\nIngrese el nombre del producto: ")
            price = float(input("Agregue el precio del producto: "))
            quantity = int(input("Ingrese la cantidad solicitada del producto: "))
            product = {"Name" : name, "Price" : price, "Quantity" : quantity}
            inventarys.append(product)
        elif option == 2:
            #verificamos que la lista no este vacia, luego recorremos la lista para mostrar elemento por elemento y le damos formato en el print.
            if len(inventarys) != 0:
                print("\nEstos son los porductos en la lista: \n")
                for inventary in inventarys:
                    print(f"Nombre: {inventary["Name"]} | Precio: {inventary["Price"]} | Cantidad: {inventary["Quantity"]}")
            else:
                print("\nNo hay ningun producto en la lista aun.\n")
        elif option == 3:
            #creamos un menu interno en el punto 3, lo controlamos con el while y le damos la opcion de volver al menu anterior
            while True:
                print("Que estadisticas desea calcular")
                print("1. Valor total del inventario")
                print("2. Cantidad total de productos registrados")
                print("3. volver al menu anterior")
                #try y except para manejo de excepciones de tipado.
                try:
                    option1 = int(input("Ingrese el numero de la opcion que desea realizar: "))
                    # control de las opciones del menu.
                    if option < 1 or option > 3:
                        raise ValueError
                    elif option1 == 1:
                        #verificamos que la lista no este vacia, luego iteramos uno por uno en los items de la lista
                        #creamos una variable para ir calculando el precio de cada articulo con finalprice = inventary["Price"] * inventary["Quantity"]
                        #luego almacenamos la suma total de estos calculos en counter para poder mostrar el precio final.
                        print("El valor total del inventario es de: ")
                        if len(inventarys) != 0:
                            for inventary in inventarys:
                                finalprice = inventary["Price"] * inventary["Quantity"]
                                counter += finalprice
                            print(f"{counter} $\n")
                        else:
                            print("No hay productos en el inventario")
                    elif option1 == 2:
                        #verificamos que la lista no este vacia leugo vamos sumando la cantidad de articulos en total
                        # finalmente mostramos la informaicon en el print.
                        if len(inventarys) != 0:
                            for inventary in inventarys:
                                total += inventary["Quantity"]
                            print(f"En estos momentos usted ha registrado {total} productos\n")
                    elif option == 3:
                        #volvemos al menu anterior
                        break
                except ValueError as e:
                    print(f"Error {e}: la entrada no es un numero valido, intenta de nuevo.")
        elif option == 4:
            #finalizamos el programa.
            break
    except ValueError as e:
        print(f"Error {e}: la entrada no es un numero valido, intenta de nuevo.")
    

