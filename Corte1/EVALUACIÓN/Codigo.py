# ------------------ SISTEMA DE INVENTARIO ------------------

# 1. Mensaje de bienvenida
print("====================================")
print("  BIENVENIDO AL SISTEMA INVENTARIO  ")
print("====================================")

# 7. Tupla (información fija)
categorias = ("Tecnologia", "Hogar", "Alimentos", "Ropa")

# 6. Lista donde se almacenan los productos
inventario = []


# Función para agregar producto
def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")

    codigo = input("Ingrese el código: ").strip()
    nombre = input("Ingrese el nombre: ").strip()

    # 10. Validación: código y nombre no vacíos
    if codigo == "" or nombre == "":
        print("Error: El código y el nombre no pueden estar vacíos.")
        return

    # 10. Validación: código duplicado
    for producto in inventario:
        if producto["codigo"] == codigo:
            print("Error: Ya existe un producto con ese código.")
            return

    # 4. Conversión de tipos + validación
    try:
        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("Error: Debe ingresar valores numéricos válidos.")
        return

    # 10. Validación: precio y cantidad no negativos
    if precio < 0 or cantidad < 0:
        print("Error: El precio y la cantidad no pueden ser negativos.")
        return

    print("Categorías disponibles:", categorias)
    categoria = input("Ingrese la categoría: ").strip()

    # 10. Validación: categoría permitida
    if categoria not in categorias:
        print("Error: Categoría inválida.")
        return

    # 8. Diccionario por producto
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }

    inventario.append(producto)
    print("Producto agregado correctamente.")


# Mostrar productos
def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")

    if len(inventario) == 0:
        print("No hay productos registrados.")
        return

    # 9. Ciclo for
    for producto in inventario:
        print("----------------------")
        print("Código:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Precio:", producto["precio"])
        print("Cantidad:", producto["cantidad"])
        print("Categoría:", producto["categoria"])


# Buscar producto
def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")
    codigo = input("Ingrese el código a buscar: ").strip()

    for producto in inventario:
        if producto["codigo"] == codigo:
            print("\nProducto encontrado:")
            print("----------------------")
            print("Código:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Precio:", producto["precio"])
            print("Cantidad:", producto["cantidad"])
            print("Categoría:", producto["categoria"])
            return

    print("Producto no encontrado.")


# Eliminar producto
def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el código a eliminar: ").strip()

    for producto in inventario:
        if producto["codigo"] == codigo:
            inventario.remove(producto)
            print("Producto eliminado correctamente.")
            return

    print("Producto no encontrado.")


# 2. Menú con while
while True:
    print("\n===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ").strip()

    # 10. Validación de opción del menú
    if opcion not in ("1", "2", "3", "4", "5"):
        print("Error: Opción inválida. Intente de nuevo.")
        continue

    # 5. Condicionales if, elif y else
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    else:
        print("Saliendo del sistema...")
        break  # 11. Salida correcta
        print("Saliendo del sistema...")
        break  # 11. Salida correcta
    else:
        print("Opción inválida.")
