
#Registrar productos con su nombre, precio y cantidad en un programa simple.
#Calcular operaciones básicas como total de unidades y costo aproximado.
#Aplicar fundamentos de programación: entrada de datos, variables, operaciones matemáticas y salidas en consola.

#mencionamos las variables a pedir al usuario
nombre_del_producto = ''
precio_del_producto = 0
cantidad_del_producto = 0

## Comprobamos que el usuario quiera registar un nuevo producto en el inventario
try:
    print("Sistema de Registro de invtario")
    inicio_del_programa = str(input("Desea registar un nuevo producto? si/no: ")).lower().strip()
    if inicio_del_programa != "no":
        print("*"*40)
        print("Ingresar el nombre del producto")
        print("*"*40)
### Pedimos el nombre del producto al usuario, comprobamos q el campo no este vacio y que no sea solo numeros
        nombre_del_producto = str(input())
        if nombre_del_producto == '':
            print("Error: el nombre del producto no puede estar vacio")
        elif nombre_del_producto.isnumeric():
            print("Error: el nombre del producto no puede ser solo numeros")
        else:
            print(f"\nEl producto a registar es: {nombre_del_producto}")
        print("*"*40)
        print("Ingresar el precio del producto")
        print("*"*40)
### Pedimos el precio del producto al cliente, y comprobamos que el campo no este vacio, no contenga espacios, y no sea texto
        precio_del_producto = input().strip()
        if precio_del_producto == '':
            print("Error: el precio no puede estar vacío")
        elif ' ' in precio_del_producto:
            print("Error: el precio no puede contener espacios")
        elif not precio_del_producto.replace('.', '', 1).isnumeric():
            print("Error: el precio debe ser un número, no texto")
        else:
            precio_del_producto = float(precio_del_producto)
            print(f"\nEl precio del producto es: ${precio_del_producto:.1f}")

        
    else:
        print("*"*40)
        print("El programa se ah cerrado correctamente")
        print("*"*40)
except ValueError:
    print("Error del sistema inicie de nuevo")       