# Sistema Gestión de Productos
---
**Desafío 1, objetivo:** Desarrollar un sistema para administrar productos en un inventario.  
 
**Requisitos: 📋**

  •Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
    
  •Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
    
  •Implementar operaciones CRUD para gestionar productos del inventario.
    
  •Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
    
  •Persistir los datos en BD MySql.

***Se implementa una solución utilizando Python en el paradigma de programación orientada a objetos.
La persistencia de los datos se realiza en una base de datos SQL.***




---

:wrench_and_hammer:


`línea de código del Script sql`

```sql
CREATE DATABASE IF NOT EXISTS productos CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

USE productos;

CREATE TABLE productos (
    id_producto INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    cantidad INT NOT NULL,
    garantia VARCHAR(255) NOT NULL,
    fecha_expiracion DATE
);
```
 
**Utilice el administrador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar**.

### 1. crear un entorno virtual:   
```
 python -m virtualenv
```
### 2. Activar entorno virtual:
```
cd venv\Scripts\activate
```
3. En el Directorio raiz crear un archivo .env que contenga los datos de su sistema DB localhost, DB Name, DB user etc.
   se adjunta un arhcivo Ejemplo

4. Iniciar MySql Workbench y ejecutar el script productos.sql
   
5. Luego para instalar los paquetes necesarios:
### `pip install -r requirements.txt`

6. Para iniciar Ejecutar python main.py

---
