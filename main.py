import os
import platform

from gestion_productos import (
    ProductoElectronico,
    ProductoAlimenticio,
    GestionProductos,
)

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')  # Para Linux/Unix/MacOs

def mostrar_menu():
    print("========== Menú Gestión de Productos ==========")
    
    print('1. Agregar Producto Electrónico')
    print('2. Agregar Producto Alimenticio')
    print('3. Buscar Producto por ID')
    print('4. Actualizar Precio del Producto')
    print('5. Eliminar Producto por ID')
    print('6. Mostrar Todos los Productos')
    print('7. Salir')
    print('==================================================')



def agregar_producto(gestion, tipo_producto):
    try:
        id_producto = input('Ingrese ID del producto: ')
        nombre = input('Ingrese nombre del producto: ')
        precio = float(input('Ingrese precio del producto: '))
        cantidad = int(input('Ingrese stock del producto: '))

        if tipo_producto == '1':
            garantia = input('Ingrese garantía del producto: ')
            producto = ProductoElectronico(id_producto, nombre, precio, cantidad, garantia)
        elif tipo_producto == '2':
            fecha_expiracion = input('Ingrese fecha de expiración del producto: AA-MM-DD: ')
            producto = ProductoAlimenticio(id_producto, nombre, precio, cantidad, fecha_expiracion)
        else:
            print('Opción inválida')
            return

        gestion.crear_producto(producto)
        input('Presione enter para continuar...')

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')

def buscar_producto_por_id(gestion):
    print()
    id_producto = input('Ingrese el ID del producto a buscar: ')
    print('----------------------------------------------------------------------------')
    gestion.leer_producto(id_producto)
    print('----------------------------------------------------------------------------')
    input('Presione enter para continuar...')

def actualizar_precio_producto(gestion):
    print()
    id_producto = input('Ingrese el ID del producto para actualizar precio: ')
    precio = float(input('Ingrese el nuevo precio del producto: '))
    gestion.actualizar_producto(id_producto, precio)
    print()
    input('Presione enter para continuar...')

def eliminar_producto_por_id(gestion):
    print()
    id_producto = input('Ingrese el ID del producto a eliminar: ')
    gestion.eliminar_producto(id_producto)
    print()
    input('Presione enter para continuar...')



def mostrar_todos_los_productos(gestion):
    print()
    print('===================== LISTADO COMPLETO DE PRODUCTOS ====================\n')
    productos = gestion.leer_datos()
    
    for producto in productos:
        if producto['garantia']:  # Si el producto tiene garantía, es un ProductoElectronico
            print(f"Id: {producto['id_producto']} ==> {producto['nombre']} - Stock: {producto['cantidad']} - Garantía: {producto['garantia']} - Precio: {producto['precio']}")
        elif producto['fecha_expiracion']:  # Si tiene fecha de expiración, es un ProductoAlimenticio
            print(f"Id: {producto['id_producto']} ==> {producto['nombre']} - Stock: {producto['cantidad']} - Fecha que Expira: {producto['fecha_expiracion']} - Precio: {producto['precio']}")
        else:
            print(f"Id: {producto['id_producto']} ==> {producto['nombre']} - Stock: {producto['cantidad']} - Precio: {producto['precio']}")
    
    print('=========================================================================\n')
    input('Presione enter para continuar...')





if __name__ == "__main__":
    gestion = GestionProductos()
   
    while True:
        
        limpiar_pantalla()
        
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2':
            agregar_producto(gestion, opcion)
        
        elif opcion == '3':
            buscar_producto_por_id(gestion)

        elif opcion == '4':
            actualizar_precio_producto(gestion)

        elif opcion == '5':
            eliminar_producto_por_id(gestion)

        elif opcion == '6':
            mostrar_todos_los_productos(gestion)

        elif opcion == '7':
            print('Saliendo del programa...')
            gestion.cerrar_conexion()
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-7)')
