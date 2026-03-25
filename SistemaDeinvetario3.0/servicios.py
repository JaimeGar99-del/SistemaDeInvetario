# servicios.py
# Operaciones CRUD del inventario: agregar, mostrar, buscar, actualizar, eliminar y estadisticas.
 
def agregar_producto(inventario):
 
    # ── Validar nombre ───────────────────────────────────────
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
 
    # ── Validar precio ───────────────────────────────────────
    print("Ingresar el precio unitario del producto")
    precio_del_producto = -1
    while precio_del_producto < 0:
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
 
    # ── Validar cantidad ─────────────────────────────────────
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
 
    # ── Guardar y confirmar ──────────────────────────────────
    producto = {
        "nombre": nombre_del_producto,
        "precio": precio_del_producto,
        "cantidad": cantidad_del_producto
    }
    inventario.append(producto)
    print(f"Producto: {nombre_del_producto} Precio: ${precio_del_producto:.0f} Cantidad: {cantidad_del_producto}")
    print("Producto registrado exitosamente en el inventario.")
 
 
def mostrar_inventario(inventario):
 
    print("INVENTARIO")
    if len(inventario) == 0:
        print("El inventario esta vacio. No hay productos registrados.")
    else:
        # Recorre la lista e imprime cada producto
        for producto in inventario:
            print(f"Producto: {producto['nombre']} Precio: ${producto['precio']:.0f} Cantidad: {producto['cantidad']}")
 
 
def buscar_producto(inventario):
 
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip()
    if nombre_buscado == '':
        print("El nombre no puede estar vacio.")
        return
 
    # Recorre el inventario comparando en minusculas para ignorar mayusculas
    for producto in inventario:
        if producto['nombre'].lower() == nombre_buscado.lower():
            print(f"Producto encontrado -> Nombre: {producto['nombre']} Precio: ${producto['precio']:.0f} Cantidad: {producto['cantidad']}")
            return
 
    # Solo llega aqui si el for termino sin encontrar el producto
    print(f"El producto '{nombre_buscado}' no fue encontrado en el inventario.")
 
 
def actualizar_producto(inventario):
 
    nombre_buscado = input("Ingrese el nombre del producto a actualizar: ").strip()
    if nombre_buscado == '':
        print("El nombre no puede estar vacio.")
        return
 
    # Busca el producto; si no existe, sale de la funcion
    producto_encontrado = None
    for producto in inventario:
        if producto['nombre'].lower() == nombre_buscado.lower():
            producto_encontrado = producto
            break
    if producto_encontrado is None:
        print(f"El producto '{nombre_buscado}' no existe en el inventario.")
        return
 
    # ── Actualizar precio (Enter = sin cambio) ───────────────
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
 
    # ── Actualizar cantidad (Enter = sin cambio) ─────────────
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
 
    nombre_buscado = input("Ingrese el nombre del producto a eliminar: ").strip()
    if nombre_buscado == '':
        print("El nombre no puede estar vacio.")
        return
 
    # Busca el producto, pide confirmacion y lo elimina si existe
    for producto in inventario:
        if producto['nombre'].lower() == nombre_buscado.lower():
            confirmacion = input(f"Confirma eliminar '{producto['nombre']}'? (S/N): ").strip().upper()
            if confirmacion == 'S':
                inventario.remove(producto)
                print(f"Producto '{nombre_buscado}' eliminado exitosamente.")
            else:
                print("Operacion cancelada.")
            return
 
    print(f"El producto '{nombre_buscado}' no fue encontrado en el inventario.")
 
 
def calcular_estadisticas(inventario):
 
    print("RESUMEN DE INVENTARIO")
    if len(inventario) == 0:
        print("No se logro calcular, no se encontraron productos en el inventario")
        return
 
    # Un solo for acumula totales y rastrea el maximo de precio y cantidad
    unidades_totales = 0
    valor_total = 0
    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]
 
    for p in inventario:
        unidades_totales += p["cantidad"]
        valor_total += p["precio"] * p["cantidad"]
        if p["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = p
        if p["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = p
 
    print(f"Total de productos registrados: {len(inventario)}")
    print(f"Unidades totales en stock: {unidades_totales}")
    print(f"Valor total del inventario: ${valor_total:.0f}")
    print(f"Producto mas caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']:.0f})")
    print(f"Producto con mayor stock: {producto_mayor_stock['nombre']} ({producto_mayor_stock['cantidad']} unidades)")