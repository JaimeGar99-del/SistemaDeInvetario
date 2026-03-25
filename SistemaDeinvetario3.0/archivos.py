def guardar_csv(inventario):

    if len(inventario) == 0:
        print("El inventario esta vacio. No hay datos para guardar.")
        return

    ruta = input("Ingrese la ruta del archivo (ej: inventario.csv): ").strip()
    if ruta == '':
        ruta = 'inventario.csv'
    try:
        with open(ruta, "w") as archivo:
            archivo.write("nombre,precio,cantidad\n")
            for producto in inventario:
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea)
        print(f"Inventario guardado en: {ruta}")
    except PermissionError:
        print(f"Error: no tienes permisos para escribir en {ruta}")
    except OSError as e :
        print(f"Error del sistema: {e}")
    except:
        print("Error")
def cargar_csv(inventario):
    pass