def mostrar_productos_detalle (productos):
    print ("Detalles de los productos")
    for codigo, producto in productos.items():
        print (f"Código: {codigo}")
        print (f"Nombre: {producto['nombre']}")
        print (f"Marca: {producto['marca']}")
        print (f"Precio: {producto['precio']}")
        print (f"Stock: {producto['stock']}")
        print (f"Color: {producto['color']}")
        print (f"Caracteristicas: {producto['caracteristicas']}")
        print("\n"*1)

def mostrar_información_breve (productos):
    print ("Información breve de los productos")
    for codigo, producto in productos.items():
        print (f"Código: {codigo}")
        print (f"Nombre: {producto['nombre']}")
        print (f"Precio: {producto['precio']}")
        print (f"Cantidad disponible: {producto['stock']}")
        print("\n"*1) 

def buscar_producto_codigo(productos, codigo):
    while True:
        if codigo in productos:
            producto = productos[codigo]
            print("Información detallada del producto:")
            print(f"Código: {codigo}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Marca: {producto['marca']}")
            print(f"Precio: {producto['precio']}")
            print(f"Stock: {producto['stock']}")
            print(f"Color: {producto['color']}")
            print(f"Características: {producto['caracteristicas']}")
            break
        else:
            print("El código de producto ingresado no existe.")


def realizar_compra(productos, carrito):
    print("Agregar productos al carrito de compras:")
    codigo = input("Ingrese el código del producto: ")
    if codigo in productos:
        cantidad_disponible = productos[codigo]['stock']
        cantidad = float(input("Ingrese la cantidad a comprar: "))
        if cantidad <= cantidad_disponible:
            producto = productos[codigo]
            nombre = producto['nombre']
            precio_unitario = producto['precio']
            costo_total = cantidad * precio_unitario
            producto_agregado = {'nombre': nombre, 'cantidad': cantidad, 'precio_unitario': precio_unitario, 'costo_total': costo_total}
            carrito.append(producto_agregado)
            productos[codigo]['stock'] -= cantidad  # Reducción del stock
            print("Producto agregado al carrito.")
        else:
            print("La cantidad ingresada supera el stock disponible.")
    else:
        print("El código de producto ingresado no existe.")


def mostrar_carrito(carrito):
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        print("Productos en el carrito:")
        
        for i, producto_agregado in enumerate(carrito, start=1):
            print(f"producto_agregado {i}:")
            print(f"Nombre: {producto_agregado['nombre']}")
            print(f"Cantidad: {producto_agregado['cantidad']}")
            print(f"Precio unitario: {producto_agregado['precio_unitario']}")
            print(f"Costo total: {producto_agregado['costo_total']}")
            print("\n" * 1) 
            print(f"nombre: {producto_agregado['nombre']}")

def modificar_carrito(carrito, productos):
    mostrar_carrito(carrito)
    while True:
        opcion = input("¿Desea modificar algún producto del carrito? (SI/NO): ")
        if opcion.upper() == "SI":
            indice = int(input("Ingrese el número de item que desea modificar: ")) - 1
            if indice >= 0 and indice < len(carrito):
                producto_agregado = carrito[indice]
                cantidad_actual = producto_agregado['cantidad']
                print(f"Cantidad actual: {cantidad_actual}")
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    if nueva_cantidad >= 0:
                        diferencia_cantidad = nueva_cantidad - cantidad_actual
                        if diferencia_cantidad <= productos[producto_agregado['codigo']]['stock']:
                            producto_agregado['cantidad'] = nueva_cantidad
                            producto_agregado['costo_total'] = nueva_cantidad * producto_agregado['precio_unitario']
                            productos[producto_agregado['codigo']]['stock'] -= abs(diferencia_cantidad)   # Actualización del stock
                            print("Producto modificado en el carrito.")
                        else:
                            print("La cantidad ingresada supera el stock disponible.")
                    else:
                        print("La cantidad ingresada no es válida.")
                except ValueError:
                    print("Error: La cantidad ingresada no es un número válido.")
        elif opcion.upper() == "NO":
            print("No se realizaron modificaciones en el carrito.")
        else:
            print("Respuesta inválida. Por favor, ingrese 'SI' o 'NO'.")


def finalizar_compra(carrito):
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        mostrar_carrito(carrito)
        print("\n"*1) 
        opcion = input("¿Está conforme con los productos añadidos en el carrito? (SI/NO): ")
        if opcion.upper() == "SI":
            total = sum(item['costo_total'] for item in carrito)
            print("Detalle de la compra:")
            for i, item in enumerate(carrito, start=1):
                print(f"Item {i}:")
                print(f"Nombre: {item['nombre']}")
                print(f"Cantidad: {item['cantidad']}")
                print(f"Precio unitario: {item['precio_unitario']}")
                print(f"Costo total: {item['costo_total']}")
                print("\n"*1) 
            print(f"Total a pagar: {total}")
            carrito.clear()
            print("Compra finalizada.")
        else:
            print("La compra no fue finalizada.")

def main ():
    productos = {
        "001": {
        'nombre': 'mochila',
        'marca': 'Everlast',
        'precio': 22000,
        'stock': 7,
        'color': 'negro',
        'caracteristicas': 'De lona, con amplios bolsillos'
        },
        "002": {
        'nombre': 'cuadernos',
        'marca': 'América',
        'precio': 700,
        'stock': 5,
        'color': 'convinados',
        'caracteristicas': '48 hojas, rayados'
        },
        "003": {
        'nombre': 'lapices',
        'marca': 'faber castell',
        'precio': 900,
        'stock': 10,
        'color': 'convinados',
        'caracteristicas': '12 colores'
        }
    }

    carrito = []

    while True:
        print ("Bienvenidos al carrito de compras")    
        print("\n"*1)
        print ("Elija una opción")
        print ("\n"*1)
        print ("1. Mostrar productos en detalle")
        print ("2. Mostrar informacion breve del producto")
        print ("3. Buscar producto por código")
        print ("4. Realizar compra")
        print ("5. Mostrar carrito")
        print ("6. Modificar carrito")
        print ("7. Finalizar compra")
        print ("8. Salir")
        print("\n"*1)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_productos_detalle (productos)
        elif opcion == "2":
            mostrar_información_breve (productos)
        elif opcion == "3":
            codigo = input ("Ingrese el codigo del producto: ")
            buscar_producto_codigo (productos, codigo)
        elif opcion == "4":
            realizar_compra (productos, carrito)
        elif opcion == "5":
            mostrar_carrito (carrito)
        elif opcion == "6":
            modificar_carrito (carrito, productos)
        elif opcion == "7":
            finalizar_compra (carrito)
        elif opcion == "8":
            break
        else:
            print ("Opcion invalida, por favor seleccione una opción válida")
            print("\n"*1)

if __name__ == "__main__":
    main()






