
# Funcion para agregar un producto al inventario,
# solicita nombre, precio y cantidad validando cada entrada,
# si la entrada es invalida vuelve a pedirla
def agregar_producto(inventario):

    # Pedimos el nombre del producto al usuario,
    # comprobamos que el campo no este vacio y que no sea solo numeros,
    # si la entrada es invalida vuelve a pedirla
    print("Ingresar el nombre del producto")
    nombre_del_producto = ''
    while nombre_del_producto == "":
        nombre_del_producto = input('Nombre del Producto: ').strip()
        if nombre_del_producto == '':
            print("El nombre del producto esta vacio, porfavor ingresar de nuevo:")
        elif nombre_del_producto.isnumeric():
            print("El nombre del producto no debe ser numerico, porfavor ingresar de nuevo:")
            nombre_del_producto = ''
        else:
            print(f"\nEl nombre del producto es: {nombre_del_producto} ")

    # Pedimos el precio del producto al usuario,
    # comprobamos que no este vacio,
    # no tenga espacios y sea numerico,
    # si la entrada es invalida vuelve a pedirla
    print("Ingresar el precio unitario del producto")
    precio_del_producto = 0
    while precio_del_producto == 0:
        precio_ingresado = input().strip()
        if precio_ingresado == '':
            print("El precio del producto esta vacio, porfavor ingresar de nuevo:")
        elif ' ' in precio_ingresado:
            print("El precio del producto no debe tener espacios, porfavor ingresar de nuevo:")
        elif not precio_ingresado.replace('.', '', 1).isnumeric():
            print("El precio del producto debe ser un numero, porfavor ingresar de nuevo:")
        else:
            precio_del_producto = float(precio_ingresado)
            print(f"\nEl precio del producto es: ${precio_del_producto:.0f}")

    # Pedimos la cantidad del producto al usuario,
    # comprobamos que no este vacia y que sea un numero entero positivo,
    # si la entrada es invalida vuelve a pedirla
    print("Ingresar la cantidad del producto")
    cantidad_del_producto = 0
    while cantidad_del_producto == 0:
        cantidad_ingresada = input().strip()
        if cantidad_ingresada == '':
            print("La cantidad del producto no puede estar vacia, porfavor ingresar de nuevo:")
        elif not cantidad_ingresada.isnumeric():
            print("La cantidad del producto debe ser un numero entero positivo, porfavor ingresar de nuevo:")
        elif int(cantidad_ingresada) <= 0:
            print("La cantidad del producto debe ser mayor a cero, intente de nuevo:")
        else:
            cantidad_del_producto = int(cantidad_ingresada)
            print(f"\nLa cantidad del producto es: #{cantidad_del_producto}")

    # Almacenamos el producto como diccionario dentro de la lista inventario
    producto = {
        "nombre": nombre_del_producto,
        "precio": precio_del_producto,
        "cantidad": cantidad_del_producto
    }
    inventario.append(producto)

    # Mostramos el resumen del producto registrado con todos sus datos en consola
    print(f"Producto: {nombre_del_producto} Precio: ${precio_del_producto:.0f} Cantidad: {cantidad_del_producto}")
    print("Producto registrado exitosamente en el inventario.")

# Funcion para mostrar todos los productos del inventario,
# recorre la lista con un bucle for y muestra cada producto,
# si el inventario esta vacio muestra un mensaje que lo indica
def mostrar_inventario(inventario):
    print("INVENTARIO")
    if len(inventario) == 0:
        print("El inventario esta vacio. No hay productos registrados.")
    else:
        # Recorremos la lista y mostramos cada producto en formato claro
        for producto in inventario:
            print(f"Producto: {producto['nombre']} Precio: ${producto['precio']:.0f} Cantidad: {producto['cantidad']}")

# Funcion para calcular estadisticas basicas del inventario,
# calcula el valor total sumando precio por cantidad de cada producto,
# y muestra la cantidad total de productos registrados
def calcular_estadisticas(inventario):
    print("RESUMEN DE INVENTARIO")
    if len(inventario) == 0:
        print("No se logro calcular, no se encontraron productos en el inventario")
    else:
        # Calculamos el valor total del inventario multiplicando precio por cantidad de cada producto
        valor_total = 0
        for product in inventario:
            valor_total += product["precio"] * product["cantidad"]
        cantidad_total = len(inventario)
        print(f"El total de productos registrados es: {cantidad_total}")
        print(f"Valor total del inventario es: ${valor_total:.0f}")