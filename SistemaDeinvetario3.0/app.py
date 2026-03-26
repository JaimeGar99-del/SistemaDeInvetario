# app.py
# Menú principal del sistema de inventario.
# Importa las operaciones de servicios.py y la persistencia de archivos.py.
 
from servicios import agregar_producto,\
    mostrar_inventario, buscar_producto,\
    actualizar_producto, eliminar_producto,\
    calcular_estadisticas
from archivos import guardar_csv, cargar_csv
 
# Lista central donde cada elemento es un diccionario {"nombre", "precio", "cantidad"}
inventario = []
 
# El bucle se mantiene activo hasta que el usuario elija la opción 9
print("SISTEMA DE REGISTRO DE INVENTARIO")
opcion = ''
while opcion != '9':
    print("\n¿Que accion desea realizar?")
    print("  1. Agregar producto")
    print("  2. Mostrar inventario")
    print("  3. Buscar producto")
    print("  4. Actualizar producto")
    print("  5. Eliminar producto")
    print("  6. Calcular estadisticas")
    print("  7. Guardar CSV")
    print("  8. Cargar CSV")
    print("  9. Salir")
    opcion = input("Ingrese una opcion (1-9): ").strip()
 
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
        # Cualquier entrada que no sea 1-9 se informa sin cerrar el programa
        print("\nOpcion invalida. Por favor ingresar un numero entre 1 y 9.")
 
print("good bye")