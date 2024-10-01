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