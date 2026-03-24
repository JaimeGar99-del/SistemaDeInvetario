def agregar_producto(inventario, nombre_del_producto, precio_del_producto, cantidad_del_producto):
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

    producto = {
        "nombre": nombre_del_producto,
        "precio": precio_del_producto,
        "cantidad": cantidad_del_producto
    }
    inventario.append(producto)

    # Mostramos el resumen del producto registrado con todos sus datos en consola
    print(f"Producto: {nombre_del_producto} Precio: ${precio_del_producto:.0f} Cantidad: {cantidad_del_producto}")
    print("Producto registrado exitosamente en el inventario.")

def mostrar_inventario(inventario):
    print("INVENTARIO")
    if len(inventario) == 0:
        print("El inventario esta vacio. No hay productos registrados.")
    else:
        # Recorremos la lista y mostramos cada producto en formato claro
        for producto in inventario:
            print(f"Producto: {producto['nombre']} Precio: ${producto['precio']:.0f} Cantidad: {producto['cantidad']}")

def buscar_producto(inventario):
    pass
def actualizar_producto(inventario):
    pass
def eliminar_producto(inventario):
    pass
def calcular_estadisticas(inventario):
    pass
def guardar_csv(inventario):
    pass
def cargar_csv(inventario):
    pass