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


CONFIGURACIÓN INICIAL (hacer en orden)
---------------------------------------

1. SQL Server:
   - Abrir SQL Server Management Studio (SSMS)
   - Conectarse al servidor
   - Abrir el archivo autotrust_script.sql
   - Ejecutar con F5
   - Esto crea la base de datos "autotrust" con las tablas
     de alquileres y devoluciones

2. MongoDB:
   - Asegurarse que el servicio de MongoDB esté corriendo
   - Abrir MongoDB Compass
   - Hacer clic en el boton ">_ MONGOSH" en la parte inferior izquierda
   - Pegar y ejecutar el siguiente script:

     use("autotrust");
     if (!db.getCollectionNames().includes("usuarios")) {
         db.createCollection("usuarios");
         print("Coleccion usuarios creada.");
     }
     const adminExistente = db.usuarios.findOne({ nombre_usuario: "admin" });
     if (!adminExistente) {
         db.usuarios.insertOne({
             id_usuario: "001",
             nombre_usuario: "admin",
             contrasena: "1234",
             tipo_usuario: "funcionario",
             estado: "activo"
         });
         print("Usuario admin creado correctamente.");
     } else {
         print("El usuario admin ya existe.");
     }

   - IMPORTANTE: las demas colecciones (clientes, funcionarios,
     vehiculos) se crean automaticamente cuando se insertan
     datos desde el sistema
   - Con el usuario admin se entra al sistema y desde adentro
     se registran los demas datos

3. Iniciar el sistema:
   - Abrir terminal en la carpeta SEGUNDO PROYECTO
     (la que contiene principal.py)
   - Ejecutar: python principal.py


USUARIOS DE PRUEBA
------------------
   Funcionario: admin / 1234


NOTAS
-----
- Si Python no responde en terminal usar la ruta completa:
  C:/Users/TU_USUARIO/AppData/Local/Python/pythoncore-3.14-64/python.exe
- El archivo principal para ejecutar es principal.py
- Las demas colecciones de MongoDB se crean automaticamente
  al usar el sistema por primera vez