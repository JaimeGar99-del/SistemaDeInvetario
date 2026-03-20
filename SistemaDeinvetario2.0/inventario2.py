#importamos las funciones del inventario_funciones
from inventario_funciones import agregar_producto, mostrar_inventario, calcular_estadisticas
# Programa de registro de inventario
# Gestionar varios productos en el inventario mediante un menu interactivo.
# Organizar registros, validar datos y obtener estadisticas basicas de forma sencilla.

# Lista que almacena todos los productos registrados como diccionarios
inventario = []
# Menu principal del sistema,
# se mantiene activo con un bucle while hasta que el usuario elija salir,
# usa condicionales if, elif y else para procesar la opcion elegida,
# si el usuario ingresa una opcion invalida muestra un mensaje de error y pide nuevamente la entrada
print("SISTEMA DE REGISTRO DE INVENTARIO")
opcion = ''
while opcion != '4':
    print("\n¿Que accion desea realizar?")
    print("  1. Agregar producto ")
    print("  2. Mostrar inventario")
    print("  3. Calcular estadisticas")
    print("  4. Salir")
    opcion = input("Ingrese una opcion ej (1): ").strip()
    if opcion == '1':
        agregar_producto(inventario)
    elif opcion == '2':
        mostrar_inventario(inventario)
    elif opcion == '3':
        calcular_estadisticas(inventario)
    elif opcion == '4':
        pass
    #     # print("good bye")
    #     # break
    else:
        print("\nOpcion invalida. Por favor ingresar un numero entre 1 y 4.")
print("good bye")

# Este programa permite gestionar un inventario de productos mediante un menu interactivo.
# Valida cada entrada del usuario, almacena los productos en una lista de diccionarios,
# y calcula estadisticas basicas como el valor total y la cantidad de productos registrados.