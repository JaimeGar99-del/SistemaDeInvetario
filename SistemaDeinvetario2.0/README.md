# Sistema de Registro de Inventario

Un programa hecho en Python que te permite gestionar un inventario de productos mediante un menu interactivo. Puedes agregar productos, ver el inventario completo y calcular estadisticas basicas como el valor total.

---

## Equipo

| Nombre |
|---|
| Jaime Garcia |

---

## ¿Qué hace este programa?

1. Muestra un **menu interactivo** con 4 opciones disponibles.
2. Te permite **agregar productos** con su nombre, precio y cantidad.
3. Te permite **ver todos los productos** registrados en el inventario.
4. Te permite **calcular estadisticas** como el valor total y la cantidad de productos.
5. Se mantiene activo hasta que elijas **salir**.

Si escribes algo invalido, el programa te avisa y te vuelve a pedir el dato sin cerrarse.

---

## ¿Qué necesito para ejecutarlo?

Solo necesitas tener **Python 3** instalado en tu computadora.

Puedes verificarlo abriendo la terminal y escribiendo:

```bash
python --version
```

Si aparece algo como `Python 3.x.x`, ¡ya estas listo!

---

## ¿Cómo se ejecuta?

1. Abre una terminal en la carpeta donde esta el archivo.
2. Escribe este comando y presiona Enter:

```bash
python inventario.py
```

---

## Ejemplo de uso

Esto es lo que veras cuando ejecutes el programa:

```
SISTEMA DE REGISTRO DE INVENTARIO

¿Que accion desea realizar?
  1. Agregar producto
  2. Mostrar inventario
  3. Calcular estadisticas
  4. Salir
Ingrese una opcion ej (1):
```

Si eliges agregar un producto:

```
Ingresar el nombre del producto
Nombre del Producto: Lapiz

Ingresar el precio unitario del producto
500

Ingresar la cantidad del producto
3

Producto: Lapiz Precio: $500 Cantidad: 3
Producto registrado exitosamente en el inventario.
```

Si luego eliges mostrar el inventario:

```
INVENTARIO
Producto: Lapiz Precio: $500 Cantidad: 3
```

Si eliges calcular estadisticas:

```
RESUMEN DE INVENTARIO
El total de productos registrados es: 1
Valor total del inventario es: $1500
```

---

## ¿Qué pasa si escribo algo incorrecto?

El programa valida cada entrada y te avisa sin cerrarse:

```
Nombre del Producto: 123
El nombre del producto no debe ser numerico, porfavor ingresar de nuevo:

Ingresar el precio unitario del producto
abc
El precio del producto debe ser un numero, porfavor ingresar de nuevo:

Ingresar la cantidad del producto
-5
La cantidad del producto debe ser mayor a cero, intente de nuevo:
```

---

## ¿Qué archivos tiene el proyecto?

```
inventario.py    | El programa principal (aqui esta todo el codigo)
README.md        | Este archivo, explica como funciona el proyecto
```

---

## ¿Cómo funciona por dentro?

El programa esta estructurado en 3 funciones principales:

| Funcion | Descripcion |
|---|---|
| `agregar_producto(inventario)` | Solicita y valida los datos del producto, luego lo guarda en la lista |
| `mostrar_inventario(inventario)` | Recorre la lista y muestra todos los productos registrados |
| `calcular_estadisticas(inventario)` | Calcula el valor total y la cantidad de productos |

Los productos se almacenan como diccionarios dentro de una lista:

```python
producto = {"nombre": "Lapiz", "precio": 500, "cantidad": 3}
inventario.append(producto)
```
---
## pseudocodigo
```

# Lista que almacena todos los productos registrados como diccionarios
# inventario = []

# while menu
#     opcion 1 agregar producto
#         pedimos nombre del producto
#             si esta vacio → avisar
#             si es numerico → avisar
#             sino → guardar nombre
#         pedimos precio del producto
#             si esta vacio → avisar
#             si tiene espacios → avisar
#             si no es numerico → avisar
#             sino → guardar precio
#         pedimos cantidad del producto
#             si esta vacia → avisar
#             si no es numero entero positivo → avisar
#             si es menor o igual a cero → avisar
#             sino → guardar cantidad
#         creamos diccionario con nombre, precio y cantidad
#         agregamos el diccionario a la lista inventario

#     opcion 2 mostrar inventario
#         si el inventario esta vacio → avisar
#         sino → recorremos la lista
#             mostramos nombre, precio y cantidad de cada producto

#     opcion 3 calcular estadisticas
#         si el inventario esta vacio → avisar
#         sino → recorremos la lista
#             acumulamos precio * cantidad de cada producto
#             contamos la cantidad de productos registrados
#             mostramos el valor total y la cantidad de productos

#     opcion 4 salimos
```
---
---

### Link al repositorio: [SistemaDeInventario](https://github.com/JaimeGar99-del/SistemaDeInvetario)

---
> 💡 **Nota:** Este proyecto fue desarrollado como practica de fundamentos de programacion en Python, aplicando condicionales, bucles, funciones y estructuras de datos.