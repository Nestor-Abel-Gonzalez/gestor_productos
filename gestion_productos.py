'''
Desafío 1: Sistema de Gestión de Productos

Objetivo: Desarrollar un sistema para manejar productos en un inventario.

Requisitos:
    •Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
    •Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
    •Implementar operaciones CRUD para gestionar productos del inventario.
    •Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
    •Persistir los datos en BD MySql.
'''

import mysql.connector
from mysql.connector import Error
from decouple import config



class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad):
        self.__id_producto = self.validar_id(id_producto)
        self.__nombre = nombre
        self.__precio = self.validar_precio(precio)
        self.__cantidad = self.validar_cantidad(cantidad)

    @property
    def id_producto(self):
        return self.__id_producto
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = self.validar_precio(nuevo_precio)
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    def validar_id(self, id_producto):
        if not id_producto:
            raise ValueError("El ID no puede estar vacío.")
        return id_producto

    def validar_precio(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser un valor positivo.")
        return precio
    
    def validar_cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        return cantidad

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    def __str__(self):
        return f"(ID: {self.id_producto}){self.nombre}  Cantidad: {self.cantidad}"

class ProductoElectronico(Producto):
    def __init__(self, id_producto, nombre, precio, cantidad, garantia):
        super().__init__(id_producto, nombre, precio, cantidad)
        self.__garantia = garantia

    @property
    def garantia(self):
        return self.__garantia

    def to_dict(self):
        data = super().to_dict()
        data["garantia"] = self.garantia
        return data

    def __str__(self):
        return f"{super().__str__()} - Garantía: {self.garantia}"



class ProductoAlimenticio(Producto):
    def __init__(self, id_producto, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(id_producto, nombre, precio, cantidad)
        self.__fecha_expiracion = fecha_expiracion

    @property
    def fecha_expiracion(self):
        return self.__fecha_expiracion

    def to_dict(self):
        data = super().to_dict()
        data["fecha_expiracion"] = self.fecha_expiracion
        return data

    def __str__(self):
        return f"{super().__str__()} - Fecha de Expiración: {self.fecha_expiracion}"

class GestionProductos:
    def __init__(self):
        self.conn = mysql.connector.connect(
        host=config('DB_HOST'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        database=config('DB_NAME'),
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.crear_tabla()


    def cerrar_conexion(self):
        if self.conn.is_connected():
            self.conn.close()

                
    def crear_tabla(self):
        query = """
        CREATE TABLE IF NOT EXISTS productos (
            id_producto INT NOT NULL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            cantidad INT NOT NULL,
            garantia VARCHAR(100),
            fecha_expiracion DATE
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def crear_producto(self, producto):
        query = """
        INSERT INTO productos (id_producto, nombre, precio, cantidad, garantia, fecha_expiracion)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (
            producto.id_producto,
            producto.nombre,
            producto.precio,
            producto.cantidad,
            getattr(producto, 'garantia',None),
            getattr(producto, 'fecha_expiracion',None)
        )
        try:
            self.cursor.execute(query, valores)
            self.conn.commit()
            print(f"\nProducto {producto.nombre} creado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    
    def leer_producto(self, id_producto):
        query = "SELECT * FROM productos WHERE id_producto = %s"
        self.cursor.execute(query, (id_producto,))
        producto_data = self.cursor.fetchone()

        if producto_data:
            if producto_data['garantia']:  # Si tiene el campo 'garantia', es un producto electrónico
                producto = ProductoElectronico(
                    id_producto=producto_data['id_producto'],
                    nombre=producto_data['nombre'],
                    precio=producto_data['precio'],
                    cantidad=producto_data['cantidad'],
                    garantia=producto_data['garantia']
                )
            elif producto_data['fecha_expiracion']:  # Si tiene el campo 'fecha_expiracion', es un producto alimenticio
                producto = ProductoAlimenticio(
                    id_producto=producto_data['id_producto'],
                    nombre=producto_data['nombre'],
                    precio=producto_data['precio'],
                    cantidad=producto_data['cantidad'],
                    fecha_expiracion=producto_data['fecha_expiracion']
                )
            else:
                print(f"El producto con ID {id_producto} no tiene información suficiente.")
                return

            print(f'PRODUCTO ENCONTRADO: --->> {producto}')
        else:
            print(f'¡¡No se encontró producto con ID!! {id_producto}')

    def actualizar_producto(self, id_producto, nuevo_precio):
        query = "UPDATE productos SET precio = %s WHERE id_producto = %s"
        self.cursor.execute(query, (nuevo_precio, id_producto))
        self.conn.commit()
        if self.cursor.rowcount:
            print(f'Precio actualizado para el producto ID:{id_producto}')
        else:
            print(f'No se encontró producto con ID:{id_producto}')

    def eliminar_producto(self, id_producto):
        query = "DELETE FROM productos WHERE id_producto = %s"
        self.cursor.execute(query, (id_producto,))
        self.conn.commit()
        if self.cursor.rowcount:
            print(f'Producto ID:{id_producto} eliminado correctamente')
        else:
            print(f'No se encontró producto con ID:{id_producto}')

    def leer_datos(self):
        query = "SELECT * FROM productos"
        self.cursor.execute(query)
        return self.cursor.fetchall()
