# Sistema Gestión de Productos


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

### Instalar e iniciar MySql Workbench:


***Cargar y ejecutar el script productos.sql***

:wrench:
`línea de código Script sql para crear Base de Datos`

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

### Pre-requisitos de instalacion y puesta en funcionamiento 📋  :wrench:
**Utilice control de version [Git](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git)**

**Y administrador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar**.

### 1. En VSC abrir un terminal de comando en Su Carpeta de trabajo e iniciar git

```
git init
```
### 2. Clonar Repositorio:

```
git clone https://github.com/Nestor-Abel-Gonzalez/gestor_productos.git
```
### 3. crear un entorno virtual:   
```
 python -m virtualenv
```
### 4. Activar entorno virtual:
```
cd venv\Scripts\activate
```

### 5. En el Directorio raiz:

  ***crear un archivo .env que contenga los datos de su sistema DB localhost, DB Name, DB user etc.
    se adjunta un arhcivo Ejemplo .envexample***
   
### 6. instalar los paquetes necesarios:
```
pip install -r requirements.txt
```

### 7. Para iniciar Ejecutar:

   ```
   python main.py
```

---
