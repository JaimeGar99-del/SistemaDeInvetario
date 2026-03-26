import csv  
# Importa la librería csv
# archivos.py
# Este archivo sirve para guardar y cargar el inventario en archivos CSV
def guardar_csv(inventario):
    """
    Guarda el inventario en un archivo CSV.
    """
    # Si no hay productos, no guarda nada
    if len(inventario) == 0:
        print("El inventario esta vacio. No hay datos para guardar.")
        return
    # Pide la ruta del archivo
    ruta = input("Ingrese la ruta del archivo (ej: inventario.csv): ").strip()
    # Mientras escriba algo y NO termine en .csv → error
    while ruta != '' and not ruta.lower().endswith(".csv"):
        print("Error: la ruta debe terminar en .csv, intente de nuevo:")
        ruta = input("Ingrese la ruta del archivo (ej: inventario.csv): ").strip()
    # Si no escribe nada → usa nombre por defecto
    if ruta == '':
        ruta = 'inventario.csv'
    try:
        # Abre el archivo en modo escritura (borra lo anterior)
        with open(ruta, "w") as archivo:
            # Escribe encabezado
            archivo.write("nombre,precio,cantidad\n")
            # Recorre todos los productos
            for producto in inventario:
                # Crea la línea del producto
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                # La escribe en el archivo
                archivo.write(linea)
        print(f"Inventario guardado en: {ruta}")
    # Errores comunes
    except PermissionError:
        print(f"Error: no tienes permisos para escribir en {ruta}")
    except OSError as e:
        print(f"Error del sistema: {e}")
    except:
        print("Error")

def cargar_csv(inventario):
    """
    Carga productos desde un archivo CSV.
    """
    valido = False
    # Se repite hasta que el archivo sea válido
    while not valido:
        ruta = input("Ingrese la ruta del archivo (ej: inventario.csv): ").strip()
        # Validación: vacío
        if ruta == '':
            print("La ruta no puede estar vacía.")
        # Validación: extensión
        elif not ruta.lower().endswith(".csv"):
            print("Error: la ruta debe terminar en .csv, intente de nuevo.")
        else:
            try:
                # Abre el archivo
                with open(ruta, "r") as archivo:
                    lineas = archivo.readlines()
                # Si está vacío → error
                if len(lineas) == 0:
                    print("El archivo CSV está vacío.")
                else:
                    # Toma el encabezado
                    header = lineas[0].strip()
                    # Valida encabezado correcto
                    if header.lower() != "nombre,precio,cantidad":
                        print("Error: el encabezado del CSV no es válido.")
                    else:
                        valido = True  

            except FileNotFoundError:
                print(f"Error: no se encontró el archivo '{ruta}'.")
            except UnicodeDecodeError:
                print(f"Error: no se pudo leer '{ruta}' por problemas de codificación.")
            except Exception as e:
                print(f"Error inesperado: {e}")
    # Lista donde se guardan los productos válidos
    productos_cargados = []
    errores = 0  # contador de errores
    try:
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
        # Recorre cada fila (menos el encabezado)
        for numero_fila, linea in enumerate(lineas[1:], start=2):
            linea = linea.strip()
            # Si la fila está vacía → se ignora
            if linea == '':
                continue
            columnas = linea.split(",")
            # Si no tiene 3 columnas → error
            if len(columnas) != 3:
                print(f"  Fila {numero_fila} omitida: no tiene exactamente 3 columnas.")
                errores += 1
                continue
            nombre = columnas[0].strip()
            try:
                # Convierte datos
                precio = float(columnas[1].strip())
                cantidad = int(columnas[2].strip())
                # Validaciones
                if precio < 0 or cantidad < 0:
                    raise ValueError("Valores negativos no permitidos.")
                if nombre == '':
                    raise ValueError("El nombre no puede estar vacío.")
                # Guarda producto válido
                productos_cargados.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })
            except ValueError as e:
                print(f"  Fila {numero_fila} omitida: {e}")
                errores += 1
    except Exception as e:
        print(f"Error inesperado al procesar el archivo: {e}")
        return
    # Si no se cargó nada válido
    if len(productos_cargados) == 0:
        print(f"No se encontraron productos válidos. Filas inválidas: {errores}")
        return
    # Pregunta qué hacer con el inventario actual
    opcion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
    # Valida opción
    while opcion not in ('S', 'N'):
        print("Opción inválida. Ingresa S para sobrescribir o N para fusionar.")
        opcion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
    # Si elige sobrescribir
    if opcion == 'S':
        inventario.clear()  # borra todo
        inventario.extend(productos_cargados)  # agrega lo nuevo
        accion = "reemplazo"
        print(f"Inventario reemplazado con {len(productos_cargados)} producto(s).")
    # Si elige fusionar
    else:
        nuevos = 0
        actualizados = 0
        for prod_nuevo in productos_cargados:
            encontrado = None
            # Busca si ya existe
            for prod_existente in inventario:
                if prod_existente['nombre'].lower() == prod_nuevo['nombre'].lower():
                    encontrado = prod_existente
                    break
            # Si existe → actualiza
            if encontrado:
                encontrado['cantidad'] += prod_nuevo['cantidad']
                if encontrado['precio'] != prod_nuevo['precio']:
                    print(f"  Precio de '{prod_nuevo['nombre']}' actualizado: "
                          f"${encontrado['precio']:.0f} -> ${prod_nuevo['precio']:.0f}")
                    encontrado['precio'] = prod_nuevo['precio']
                actualizados += 1
            # Si no existe → lo agrega
            else:
                inventario.append(prod_nuevo)
                nuevos += 1
        accion = "fusion"
        print(f"Fusión completada: {nuevos} nuevo(s), {actualizados} actualizado(s).")
    # Muestra errores si hubo
    if errores > 0:
        print(f"{errores} fila(s) inválida(s) omitida(s).")
    # Resumen final
    print(f"Resumen -> Productos cargados: {len(productos_cargados)} | "
          f"Filas inválidas: {errores} | Acción: {accion}")