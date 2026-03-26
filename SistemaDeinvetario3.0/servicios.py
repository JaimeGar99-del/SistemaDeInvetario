# servicios.py
# Este archivo contiene todas las funciones principales del sistema de inventario:
# agregar, buscar, actualizar, eliminar productos y calcular estadísticas.
def _pedir_valor(tipo):
    """
    Función auxiliar para pedir un número al usuario.
    Puede ser 'precio' o 'cantidad'.
    Valida que:
    - No esté vacío
    - Sea numérico
    - Sea mayor a 0
    """
    # Verificamos si estamos pidiendo precio o cantidad
    es_precio = tipo == 'precio'
    # Mensaje dinámico dependiendo del tipo
    print(f"Ingresar el {'precio unitario' if es_precio else 'cantidad'} del producto")
    # Valor inicial inválido para entrar al while
    valor = -1 if es_precio else 0
    # Mientras el valor sea inválido (<= 0), seguimos pidiendo
    while valor <= 0:
        ingresado = input().strip()
        # Validación: vacío
        if ingresado == '':
            print(f"El {tipo} no puede estar vacio, porfavor ingresar de nuevo:")
        # Validación: precio no debe tener espacios
        elif es_precio and ' ' in ingresado:
            print("El precio no debe tener espacios, porfavor ingresar de nuevo:")
        # Validación: debe ser número
        elif not ingresado.replace('.', '', 1).isnumeric():
            print(f"El {tipo} debe ser un numero, porfavor ingresar de nuevo:")
        else:
            # Convertimos a float si es precio, a int si es cantidad
            valor = float(ingresado) if es_precio else int(ingresado)
            # Validación: debe ser mayor a 0
            if valor <= 0:
                print(f"El {tipo} debe ser mayor a cero, porfavor ingresar de nuevo:")
                valor = -1 if es_precio else 0
            else:
                print(f"\nEl {tipo} es: {'$' if es_precio else '#'}{valor:.0f}")
    return valor

def agregar_producto(inventario):
    """
    Agrega un producto al inventario pidiendo datos al usuario.
    """
    print("Ingresar el nombre del producto")
    nombre_del_producto = ''
    # Validamos el nombre
    while nombre_del_producto == "":
        nombre_del_producto = input('Nombre del Producto: ').strip()
        if nombre_del_producto == '':
            print("El nombre del producto esta vacio, porfavor ingresar de nuevo:")
        elif nombre_del_producto.isnumeric():
            print("El nombre del producto no debe ser numerico, porfavor ingresar de nuevo:")
            nombre_del_producto = ''
        else:
            print(f"\nEl nombre del producto es: {nombre_del_producto} ")
    # Pedimos precio y cantidad usando la función auxiliar
    precio_del_producto = _pedir_valor('precio')
    cantidad_del_producto = _pedir_valor('cantidad')
    # Creamos el producto como diccionario
    producto = {
        "nombre": nombre_del_producto,
        "precio": precio_del_producto,
        "cantidad": cantidad_del_producto
    }
    # Lo agregamos al inventario (lista)
    inventario.append(producto)
    print(f"Producto: {nombre_del_producto} Precio: ${precio_del_producto:.0f} Cantidad: {cantidad_del_producto}")
    print("Producto registrado exitosamente en el inventario.")

def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    """
    print("INVENTARIO")
    # Si está vacío
    if len(inventario) == 0:
        print("El inventario esta vacio. No hay productos registrados.")
    else:
        # Recorremos e imprimimos cada producto
        for producto in inventario:
            print(f"Producto: {producto['nombre']} Precio: ${producto['precio']:.0f} Cantidad: {producto['cantidad']}")

def buscar_producto(inventario):
    """
    Busca un producto por nombre.
    """
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip()
    if nombre_buscado == '':
        print("El nombre no puede estar vacio.")
        return
    # Recorremos el inventario
    for producto in inventario:
        # Comparación sin importar mayúsculas/minúsculas
        if producto['nombre'].lower() == nombre_buscado.lower():
            print(f"Producto encontrado -> Nombre: {producto['nombre']} Precio: ${producto['precio']:.0f} Cantidad: {producto['cantidad']}")
            return
    # Si no se encontró
    print(f"El producto '{nombre_buscado}' no fue encontrado en el inventario.")


def actualizar_producto(inventario):
    """
    Permite actualizar precio y cantidad de un producto existente.
    """
    nombre_buscado = input("Ingrese el nombre del producto a actualizar: ").strip()
    if nombre_buscado == '':
        print("El nombre no puede estar vacio.")
        return
    # Buscar producto
    producto_encontrado = None
    for producto in inventario:
        if producto['nombre'].lower() == nombre_buscado.lower():
            producto_encontrado = producto
            break
    # Si no existe
    if producto_encontrado is None:
        print(f"El producto '{nombre_buscado}' no existe en el inventario.")
        return
    # Actualizar precio
    print("Ingresar nuevo precio (Enter para no cambiar):")
    precio_ingresado = input().strip()
    while precio_ingresado != '':
        if ' ' in precio_ingresado:
            print("El precio no debe tener espacios, porfavor ingresar de nuevo:")
        elif not precio_ingresado.replace('.', '', 1).isnumeric():
            print("El precio debe ser un numero, porfavor ingresar de nuevo:")
        else:
            producto_encontrado['precio'] = float(precio_ingresado)
            break
        precio_ingresado = input().strip()
    # Actualizar cantidad
    print("Ingresar nueva cantidad (Enter para no cambiar):")
    cantidad_ingresada = input().strip()
    while cantidad_ingresada != '':
        if not cantidad_ingresada.isnumeric():
            print("La cantidad debe ser un numero entero positivo, porfavor ingresar de nuevo:")
        elif int(cantidad_ingresada) <= 0:
            print("La cantidad debe ser mayor a cero, intente de nuevo:")
        else:
            producto_encontrado['cantidad'] = int(cantidad_ingresada)
            break
        cantidad_ingresada = input().strip()
    print(f"Producto '{producto_encontrado['nombre']}' actualizado exitosamente.")


def eliminar_producto(inventario):
    """
    Elimina un producto del inventario con confirmación.
    """
    nombre_buscado = input("Ingrese el nombre del producto a eliminar: ").strip()
    if nombre_buscado == '':
        print("El nombre no puede estar vacio.")
        return
    for producto in inventario:
        if producto['nombre'].lower() == nombre_buscado.lower():
            # Confirmación antes de eliminar
            confirmacion = input(f"Confirma eliminar '{producto['nombre']}'? (S/N): ").strip().upper()
            if confirmacion == 'S':
                inventario.remove(producto)
                print(f"Producto '{nombre_buscado}' eliminado exitosamente.")
            else:
                print("Operacion cancelada.")
            return
    print(f"El producto '{nombre_buscado}' no fue encontrado en el inventario.")


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.
    """
    print("RESUMEN DE INVENTARIO")
    # Validación: inventario vacío
    if len(inventario) == 0:
        print("No se logro calcular, no se encontraron productos en el inventario")
        return
    # Variables acumuladoras
    unidades_totales = 0
    valor_total = 0
    # Inicializamos con el primer producto
    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]
    # Recorremos el inventario
    for p in inventario:
        unidades_totales += p["cantidad"]
        valor_total += p["precio"] * p["cantidad"]
        # Comparar precio
        if p["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = p
        # Comparar cantidad
        if p["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = p
    # Mostrar resultados
    print(f"Total de productos registrados: {len(inventario)}")
    print(f"Unidades totales en stock: {unidades_totales}")
    print(f"Valor total del inventario: ${valor_total:.0f}")
    print(f"Producto mas caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']:.0f})")
    print(f"Producto con mayor stock: {producto_mayor_stock['nombre']} ({producto_mayor_stock['cantidad']} unidades)")