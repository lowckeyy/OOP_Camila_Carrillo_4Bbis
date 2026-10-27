-- 1. Asegurar que existe el schema
CREATE SCHEMA IF NOT EXISTS login_mvc;

-- 2. Eliminar la tabla anterior para borrar la configuración vieja
DROP TABLE IF EXISTS login_mvc.users CASCADE;

-- 3. Crear la tabla especificando la secuencia identity
CREATE TABLE login_mvc.users (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    pass VARCHAR(255) NOT NULL
);