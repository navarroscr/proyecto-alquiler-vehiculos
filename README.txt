=====================================
  AUTOTRUST S.A. - Sistema de Alquiler de Vehículos
  Programación III - I Cuatrimestre 2026
  Desarrollado por: Jean Carlo Navarro y Samuel Brenes
=====================================

ARCHIVO PRINCIPAL
-----------------
Para ejecutar el sistema correr el archivo:
    principal.py


REQUISITOS
----------
- Python 3.10 o superior
- SQL Server con Windows Authentication
- MongoDB corriendo en localhost:27017


DEPENDENCIAS
------------
Instalar con pip antes de ejecutar:

    pip install pymongo
    pip install pyodbc
    pip install matplotlib
    pip install pandas


BASE DE DATOS
-------------
1. SQL Server:
   - Ejecutar el script autotrust_script.sql en SQL Server Management Studio
   - El script crea la base de datos "autotrust" y las tablas necesarias
   - Usa Windows Authentication (no requiere usuario ni contraseña)

2. MongoDB:
   - No requiere configuración adicional
   - Las colecciones se crean automáticamente al insertar datos
   - Base de datos: autotrust