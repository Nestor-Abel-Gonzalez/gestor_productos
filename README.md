 
# Desafío 1: Sistema de Gestión de Productos

Objetivo: Desarrollar un sistema para manejar productos en un inventario.

Requisitos:

  •Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
    
  •Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
    
  •Implementar operaciones CRUD para gestionar productos del inventario.
    
  •Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
    
  •Persistir los datos en BD MySql.

Se implementa una solución utilizando Python en el paradigma de programación orientada a objetos.
La persistencia de los datos se realiza en una base de datos SQL.


<hr/>

### 1. crear un entorno virtual:
   
```
 python -m virtualenv
```

3. Activar entorno virtual:
### `cd venv\Scripts\activate`

3. En el Directorio raiz crear un archivo .env que contenga los datos de su sistema DB localhost, DB Name, DB user etc.
   se adjunta un arhcivo Ejemplo

4. Iniciar MySql Workbench y ejecutar el script productos.sql
   
5. Luego para instalar los paquetes necesarios:
### `pip install -r requirements.txt`

6. Para iniciar Ejecutar python main.py

<hr/>
