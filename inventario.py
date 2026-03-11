#Programa de registro de inventario
#Registrar productos con su nombre, precio y cantidad.
#Calcular operaciones básicas como total de unidades y costo aproximado.

nombre_del_producto = ''
precio_del_producto = 0
cantidad_del_producto = 0
costo_total = 0

try:
    print("Sistema de Registro de Inventario")

    #Preguntar si desea registrar un producto
    inicio_del_programa = str(input("¿Desea registrar un nuevo producto? si/no: ")).lower().strip()
    if inicio_del_programa != "no":
       #Pedimos el nombre del producto al usuario,
       #comprobamos que el campo no esté vacío y que no sea solo números,
       #si la entrada es inválida vuelve a pedirla
        print("Ingresar el nombre del producto")
        print("*" * 40)
        nombre_valido = False
        while not nombre_valido:
            nombre_del_producto = str(input()).strip()
            if nombre_del_producto == '':
                print("Error: el nombre del producto no puede estar vacío, intente de nuevo:")
            elif nombre_del_producto.isnumeric():
                print("Error: el nombre del producto no puede ser solo números, intente de nuevo:")
            else:
                print(f"\nEl producto a registrar es: {nombre_del_producto}")
                nombre_valido = True
            #Pedimos el precio del producto al usuario,
            #comprobamos que no esté vacío,
            #no tenga espacios y sea numérico,
            #si la entrada es inválida vuelve a pedirla
            print("*" * 40)
            print("Ingresar el precio unitario del producto")
            print("*" * 40)
            precio_valido = False
            while not precio_valido:
                precio_ingresado = input().strip()
                if precio_ingresado == '':
                    print("Error: el precio no puede estar vacío, intente de nuevo:")
                elif ' ' in precio_ingresado:
                    print("Error: el precio no puede contener espacios, intente de nuevo:")
                elif not precio_ingresado.replace('.', '', 1).isnumeric():
                    print("Error: el precio debe ser un número, no texto, intente de nuevo:")
                else:
                    precio_del_producto = float(precio_ingresado)
                    print(f"\nEl precio del producto es: ${precio_del_producto:.0f}")
                    precio_valido = True

            #Pedimos la cantidad del producto al usuario,
            #comprobamos que no esté vacía y que sea un número entero positivo,
            #si la entrada es inválida vuelve a pedirla
            print("*" * 40)
            print("Ingresar la cantidad del producto")
            print("*" * 40)
            cantidad_valida = False
            while not cantidad_valida:
                cantidad_ingresada = input().strip()
                if cantidad_ingresada == '':
                    print("Error: la cantidad no puede estar vacía, intente de nuevo:")
                elif not cantidad_ingresada.isnumeric():
                    print("Error: la cantidad debe ser un número entero positivo, intente de nuevo:")
                elif int(cantidad_ingresada) <= 0:
                    print("Error: la cantidad debe ser mayor a cero, intente de nuevo:")
                else:
                    cantidad_del_producto = int(cantidad_ingresada)
                    cantidad_valida = True
                    #Almacenamos el resultado de multiplicar el precio por la cantidad para obtener el costo total
                    costo_total = precio_del_producto * cantidad_del_producto

                    #Mostramos el resumen del producto registrado con todos sus datos en consola
                    print("\n" + "=" * 40)
                    print(f"Producto: {nombre_del_producto} | Precio: {precio_del_producto:.0f} | Cantidad: {cantidad_del_producto} | Total: {costo_total:.0f}")
                    print("=" * 40)
                    print("\nProducto registrado exitosamente en el inventario.")

    else:
        #El usuario eligió no registrar un producto
        print("*" * 40)
        print("El programa se ha cerrado correctamente")
        print("*" * 40)

except ValueError:
    print("Error del sistema, inicie de nuevo")

#Este programa permite registrar un producto en el inventario solicitando su nombre, precio unitario
#y cantidad al usuario. Valida cada entrada para evitar errores, calcula el costo total
#multiplicando precio por cantidad, y muestra un resumen con todos los datos en consola.