from funciones_inventario3 import agregar_producto,\
    mostrar_inventario,buscar_producto,\
    actualizar_producto, eliminar_producto,\
    calcular_estadisticas, guardar_csv , cargar_csv
inventario = []

print("SISTEMA DE REGISTRO DE INVENTARIO")
opcion = ''
while opcion != '4':
    print("\n¿Que accion desea realizar?")
    print("  1. Agregar producto ")
    print("  2. Mostrar inventario")
    print("  3. buscar producto")
    print("  4. actualizar producto")
    print("  5. Eliminar producto")
    print("  6. Calcular estadisticas")
    print("  7. Guardar CSV")
    print("  8. Cargar CSV")
    print("  9. Salir")
    opcion = input("Ingrese una opcion ej (1): ").strip()
    if opcion == '1':
        agregar_producto(inventario)
    elif opcion == '2':
        mostrar_inventario(inventario)
    elif opcion == '3':
        buscar_producto(inventario)
    elif opcion == '4':
        actualizar_producto(inventario)
    elif opcion == '5':
        eliminar_producto(inventario)
    elif opcion == '6':
        calcular_estadisticas(inventario)
    elif opcion == '7':
        guardar_csv(inventario)
    elif opcion == '8':
        cargar_csv(inventario)
    elif opcion == '9':
        pass
    else:
        print("\nOpcion invalida. Por favor ingresar un numero entre 1 y 4.")
print("good bye")