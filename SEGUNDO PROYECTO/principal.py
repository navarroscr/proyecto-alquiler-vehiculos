# principal.py
# Archivo de prueba en consola 
# MODULO DE PRUEBA PARA VERIFICAR LAS FUNCIONES YA CREADAS

import logica.clientes_logica as clientes_logica
import logica.funcionario_logica as funcionarios_logica
import logica.vehiculo_logica as vehiculo_logica
import logica.usuario_logica as usuarios_logica
import logica.alquiler_logica as alquiler_logica
import logica.devolucion_logica as devolucion_logica


# ==================== MENÚ PRINCIPAL ====================

def mostrar_menu_principal():
    print("\n===== AUTOTRUST S.A. =====")
    print("1. Módulo clientes")
    print("2. Módulo funcionarios")
    print("3. Módulo vehículos")
    print("4. Módulo usuarios")
    print("5. Módulo alquileres")
    print("6. Salir")
    print("==========================")


# ==================== SUBMENÚ CLIENTES ====================

def mostrar_menu_clientes():
    print("\n--- MÓDULO CLIENTES ---")
    print("1. Crear cliente")
    print("2. Ver clientes")
    print("3. Buscar cliente por id")
    print("4. Actualizar cliente")
    print("5. Eliminar cliente")
    print("6. Volver al menú principal")
    print("-----------------------")


def opcion_crear_cliente():
    print("\n-- Crear nuevo cliente --")
    id_cliente = input("Id del cliente: ")
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    direccion = input("Dirección: ")
    clientes_logica.crear_cliente(id_cliente, nombre, cedula, telefono, correo, direccion)


def opcion_ver_clientes():
    print("\n-- Lista de clientes --")
    lista = clientes_logica.obtener_todos_los_clientes()
    if len(lista) == 0:
        print("No hay clientes registrados.")
    else:
        for cliente in lista:
            print("\n--- Cliente ---")
            print("ID:", cliente["id_cliente"])
            print("Nombre:", cliente["nombre"])
            print("Cédula:", cliente["cedula"])
            print("Teléfono:", cliente["telefono"])
            print("Correo:", cliente["correo"])
            print("Dirección:", cliente["direccion"])
            print("Estado:", cliente["estado"])


def opcion_buscar_cliente():
    print("\n-- Buscar cliente por id --")
    id_cliente = input("Id del cliente: ")
    cliente = clientes_logica.buscar_cliente(id_cliente)
    if cliente is None:
        print("No se encontró ningún cliente con ese id.")
    else:
        print("\n--- Cliente encontrado ---")
        print("ID:", cliente["id_cliente"])
        print("Nombre:", cliente["nombre"])
        print("Cédula:", cliente["cedula"])
        print("Teléfono:", cliente["telefono"])
        print("Correo:", cliente["correo"])
        print("Dirección:", cliente["direccion"])
        print("Estado:", cliente["estado"])


def opcion_actualizar_cliente():
    print("\n-- Actualizar cliente --")
    id_cliente = input("Id del cliente a actualizar: ")
    print("Ingrese los datos a cambiar (enter para omitir):")
    nombre = input("Nuevo nombre: ")
    telefono = input("Nuevo teléfono: ")
    correo = input("Nuevo correo: ")
    direccion = input("Nueva dirección: ")

    nuevos_datos = {}
    if nombre != "":
        nuevos_datos["nombre"] = nombre
    if telefono != "":
        nuevos_datos["telefono"] = telefono
    if correo != "":
        nuevos_datos["correo"] = correo
    if direccion != "":
        nuevos_datos["direccion"] = direccion

    if len(nuevos_datos) == 0:
        print("No se ingresó ningún dato para actualizar.")
    else:
        clientes_logica.actualizar_cliente(id_cliente, nuevos_datos)


def opcion_eliminar_cliente():
    print("\n-- Eliminar cliente --")
    id_cliente = input("Id del cliente a eliminar: ")
    clientes_logica.eliminar_cliente(id_cliente)


def menu_clientes():
    opcion = ""
    while opcion != "6":
        mostrar_menu_clientes()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            opcion_crear_cliente()
        elif opcion == "2":
            opcion_ver_clientes()
        elif opcion == "3":
            opcion_buscar_cliente()
        elif opcion == "4":
            opcion_actualizar_cliente()
        elif opcion == "5":
            opcion_eliminar_cliente()
        elif opcion == "6":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida, intente de nuevo.")


# ==================== SUBMENÚ FUNCIONARIOS ====================

def mostrar_menu_funcionarios():
    print("\n--- MÓDULO FUNCIONARIOS ---")
    print("1. Crear funcionario")
    print("2. Ver funcionarios")
    print("3. Buscar funcionario por id")
    print("4. Actualizar funcionario")
    print("5. Eliminar funcionario")
    print("6. Volver al menú principal")
    print("--------------------------")


def opcion_crear_funcionario():
    print("\n-- Crear nuevo funcionario --")
    id_funcionario = input("Id del funcionario: ")
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    puesto = input("Puesto: ")
    funcionarios_logica.crear_funcionario(id_funcionario, nombre, cedula, telefono, correo, puesto)


def opcion_ver_funcionarios():
    print("\n-- Lista de funcionarios --")
    lista = funcionarios_logica.obtener_todos_los_funcionarios()
    if len(lista) == 0:
        print("No hay funcionarios registrados.")
    else:
        for funcionario in lista:
            print("\n--- Funcionario ---")
            print("ID:", funcionario["id_funcionario"])
            print("Nombre:", funcionario["nombre"])
            print("Cédula:", funcionario["cedula"])
            print("Teléfono:", funcionario["telefono"])
            print("Correo:", funcionario["correo"])
            print("Puesto:", funcionario["puesto"])
            print("Estado:", funcionario["estado"])


def opcion_buscar_funcionario():
    print("\n-- Buscar funcionario por id --")
    id_funcionario = input("Id del funcionario: ")
    funcionario = funcionarios_logica.buscar_funcionario(id_funcionario)
    if funcionario is None:
        print("No se encontró ningún funcionario con ese id.")
    else:
        print("\n--- Funcionario encontrado ---")
        print("ID:", funcionario["id_funcionario"])
        print("Nombre:", funcionario["nombre"])
        print("Cédula:", funcionario["cedula"])
        print("Teléfono:", funcionario["telefono"])
        print("Correo:", funcionario["correo"])
        print("Puesto:", funcionario["puesto"])
        print("Estado:", funcionario["estado"])


def opcion_actualizar_funcionario():
    print("\n-- Actualizar funcionario --")
    id_funcionario = input("Id del funcionario a actualizar: ")
    print("Ingrese los datos a cambiar (enter para omitir):")
    nombre = input("Nuevo nombre: ")
    telefono = input("Nuevo teléfono: ")
    correo = input("Nuevo correo: ")
    puesto = input("Nuevo puesto: ")

    nuevos_datos = {}
    if nombre != "":
        nuevos_datos["nombre"] = nombre
    if telefono != "":
        nuevos_datos["telefono"] = telefono
    if correo != "":
        nuevos_datos["correo"] = correo
    if puesto != "":
        nuevos_datos["puesto"] = puesto

    if len(nuevos_datos) == 0:
        print("No se ingresó ningún dato para actualizar.")
    else:
        funcionarios_logica.actualizar_funcionario(id_funcionario, nuevos_datos)


def opcion_eliminar_funcionario():
    print("\n-- Eliminar funcionario --")
    id_funcionario = input("Id del funcionario a eliminar: ")
    funcionarios_logica.eliminar_funcionario(id_funcionario)


def menu_funcionarios():
    opcion = ""
    while opcion != "6":
        mostrar_menu_funcionarios()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            opcion_crear_funcionario()
        elif opcion == "2":
            opcion_ver_funcionarios()
        elif opcion == "3":
            opcion_buscar_funcionario()
        elif opcion == "4":
            opcion_actualizar_funcionario()
        elif opcion == "5":
            opcion_eliminar_funcionario()
        elif opcion == "6":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida, intente de nuevo.")


# ==================== SUBMENÚ VEHÍCULOS ====================

def mostrar_menu_vehiculos():
    print("\n--- MÓDULO VEHÍCULOS ---")
    print("1. Crear vehículo")
    print("2. Ver vehículos")
    print("3. Buscar vehículo por id")
    print("4. Buscar vehículo por placa")
    print("5. Actualizar vehículo")
    print("6. Eliminar vehículo")
    print("7. Volver al menú principal")
    print("-----------------------")


def opcion_crear_vehiculo():
    print("\n-- Crear nuevo vehículo --")
    id_vehiculo = input("Id del vehículo: ")
    marca = input("Marca: ")
    tipo = input("Tipo: ")
    placa = input("Placa: ")
    numero_motor = input("Número de motor: ")
    transmision = input("Transmisión: ")
    combustible = input("Combustible: ")
    color = input("Color: ")
    cantidad_pasajeros = input("Cantidad de pasajeros: ")
    costo_diario = input("Costo diario: ")
    cantidad_maletas = input("Cantidad de maletas: ")
    imagen = input("Imagen (ruta o nombre): ")
    vehiculo_logica.crear_vehiculo(id_vehiculo, marca, tipo, placa, numero_motor, transmision, combustible, color, cantidad_pasajeros, costo_diario, cantidad_maletas, imagen)


def opcion_ver_vehiculos():
    print("\n-- Lista de vehículos --")
    lista = vehiculo_logica.obtener_todos_los_vehiculos()
    if len(lista) == 0:
        print("No hay vehículos registrados.")
    else:
        for vehiculo in lista:
            print("\n--- Vehículo ---")
            print("ID:", vehiculo["id_vehiculo"])
            print("Marca:", vehiculo["marca"])
            print("Tipo:", vehiculo["tipo"])
            print("Placa:", vehiculo["placa"])
            print("Número de motor:", vehiculo["numero_motor"])
            print("Transmisión:", vehiculo["transmision"])
            print("Combustible:", vehiculo["combustible"])
            print("Color:", vehiculo["color"])
            print("Cantidad de pasajeros:", vehiculo["cantidad_pasajeros"])
            print("Costo diario:", vehiculo["costo_diario"])
            print("Cantidad de maletas:", vehiculo["cantidad_maletas"])
            print("Imagen:", vehiculo["imagen"])
            print("Estado:", vehiculo["estado"])


def opcion_buscar_vehiculo():
    print("\n-- Buscar vehículo por id --")
    id_vehiculo = input("Id del vehículo: ")
    vehiculo = vehiculo_logica.buscar_vehiculo(id_vehiculo)
    if vehiculo is None:
        print("No se encontró ningún vehículo con ese id.")
    else:
        print("\n--- Vehículo encontrado ---")
        print("ID:", vehiculo["id_vehiculo"])
        print("Marca:", vehiculo["marca"])
        print("Tipo:", vehiculo["tipo"])
        print("Placa:", vehiculo["placa"])
        print("Número de motor:", vehiculo["numero_motor"])
        print("Transmisión:", vehiculo["transmision"])
        print("Combustible:", vehiculo["combustible"])
        print("Color:", vehiculo["color"])
        print("Cantidad de pasajeros:", vehiculo["cantidad_pasajeros"])
        print("Costo diario:", vehiculo["costo_diario"])
        print("Cantidad de maletas:", vehiculo["cantidad_maletas"])
        print("Imagen:", vehiculo["imagen"])
        print("Estado:", vehiculo["estado"])


def opcion_buscar_vehiculo_placa():
    print("\n-- Buscar vehículo por placa --")
    placa = input("Placa del vehículo: ")
    vehiculo = vehiculo_logica.buscar_vehiculo_placa(placa)
    if vehiculo is None:
        print("No se encontró ningún vehículo con esa placa.")
    else:
        print("\n--- Vehículo encontrado ---")
        print("ID:", vehiculo["id_vehiculo"])
        print("Marca:", vehiculo["marca"])
        print("Tipo:", vehiculo["tipo"])
        print("Placa:", vehiculo["placa"])
        print("Número de motor:", vehiculo["numero_motor"])
        print("Transmisión:", vehiculo["transmision"])
        print("Combustible:", vehiculo["combustible"])
        print("Color:", vehiculo["color"])
        print("Cantidad de pasajeros:", vehiculo["cantidad_pasajeros"])
        print("Costo diario:", vehiculo["costo_diario"])
        print("Cantidad de maletas:", vehiculo["cantidad_maletas"])
        print("Imagen:", vehiculo["imagen"])
        print("Estado:", vehiculo["estado"])


def opcion_actualizar_vehiculo():
    print("\n-- Actualizar vehículo --")
    id_vehiculo = input("Id del vehículo a actualizar: ")
    print("Ingrese los datos a cambiar (enter para omitir):")
    marca = input("Nueva marca: ")
    color = input("Nuevo color: ")
    costo_diario = input("Nuevo costo diario: ")
    estado = input("Nuevo estado: ")

    nuevos_datos = {}
    if marca != "":
        nuevos_datos["marca"] = marca
    if color != "":
        nuevos_datos["color"] = color
    if costo_diario != "":
        nuevos_datos["costo_diario"] = costo_diario
    if estado != "":
        nuevos_datos["estado"] = estado

    if len(nuevos_datos) == 0:
        print("No se ingresó ningún dato para actualizar.")
    else:
        vehiculo_logica.actualizar_vehiculo(id_vehiculo, nuevos_datos)


def opcion_eliminar_vehiculo():
    print("\n-- Eliminar vehículo --")
    id_vehiculo = input("Id del vehículo a eliminar: ")
    vehiculo_logica.eliminar_vehiculo(id_vehiculo)


def menu_vehiculos():
    opcion = ""
    while opcion != "7":
        mostrar_menu_vehiculos()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            opcion_crear_vehiculo()
        elif opcion == "2":
            opcion_ver_vehiculos()
        elif opcion == "3":
            opcion_buscar_vehiculo()
        elif opcion == "4":
            opcion_buscar_vehiculo_placa()
        elif opcion == "5":
            opcion_actualizar_vehiculo()
        elif opcion == "6":
            opcion_eliminar_vehiculo()
        elif opcion == "7":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida, intente de nuevo.")


# ==================== SUBMENÚ USUARIOS ====================

def mostrar_menu_usuarios():
    print("\n--- MÓDULO USUARIOS ---")
    print("1. Crear usuario")
    print("2. Ver usuarios")
    print("3. Buscar usuario por id")
    print("4. Buscar usuario por nombre")
    print("5. Actualizar usuario")
    print("6. Eliminar usuario")
    print("7. Volver al menú principal")
    print("----------------------")


def opcion_crear_usuario():
    print("\n-- Crear nuevo usuario --")
    id_usuario = input("Id del usuario: ")
    nombre_usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    tipo_usuario = input("Tipo de usuario: ")
    usuarios_logica.crear_usuario(id_usuario, nombre_usuario, contrasena, tipo_usuario)


def opcion_ver_usuarios():
    print("\n-- Lista de usuarios --")
    lista = usuarios_logica.obtener_todos_los_usuarios()
    if len(lista) == 0:
        print("No hay usuarios registrados.")
    else:
        for usuario in lista:
            print("\n--- Usuario ---")
            print("ID:", usuario["id_usuario"])
            print("Nombre de usuario:", usuario["nombre_usuario"])
            print("Tipo:", usuario["tipo_usuario"])
            print("Estado:", usuario["estado"])


def opcion_buscar_usuario():
    print("\n-- Buscar usuario por id --")
    id_usuario = input("Id del usuario: ")
    usuario = usuarios_logica.buscar_usuario(id_usuario)
    if usuario is None:
        print("No se encontró ningún usuario con ese id.")
    else:
        print("\n--- Usuario encontrado ---")
        print("ID:", usuario["id_usuario"])
        print("Nombre de usuario:", usuario["nombre_usuario"])
        print("Tipo:", usuario["tipo_usuario"])
        print("Estado:", usuario["estado"])


def opcion_buscar_usuario_nombre():
    print("\n-- Buscar usuario por nombre --")
    nombre_usuario = input("Nombre de usuario: ")
    usuario = usuarios_logica.buscar_usuario_nombre(nombre_usuario)
    if usuario is None:
        print("No se encontró ningún usuario con ese nombre.")
    else:
        print("\n--- Usuario encontrado ---")
        print("ID:", usuario["id_usuario"])
        print("Nombre de usuario:", usuario["nombre_usuario"])
        print("Tipo:", usuario["tipo_usuario"])
        print("Estado:", usuario["estado"])


def opcion_actualizar_usuario():
    print("\n-- Actualizar usuario --")
    id_usuario = input("Id del usuario a actualizar: ")
    print("Ingrese los datos a cambiar (enter para omitir):")
    nombre_usuario = input("Nuevo nombre de usuario: ")
    contrasena = input("Nueva contraseña: ")
    tipo_usuario = input("Nuevo tipo de usuario: ")

    nuevos_datos = {}
    if nombre_usuario != "":
        nuevos_datos["nombre_usuario"] = nombre_usuario
    if contrasena != "":
        nuevos_datos["contrasena"] = contrasena
    if tipo_usuario != "":
        nuevos_datos["tipo_usuario"] = tipo_usuario

    if len(nuevos_datos) == 0:
        print("No se ingresó ningún dato para actualizar.")
    else:
        usuarios_logica.actualizar_usuario(id_usuario, nuevos_datos)


def opcion_eliminar_usuario():
    print("\n-- Eliminar usuario --")
    id_usuario = input("Id del usuario a eliminar: ")
    usuarios_logica.eliminar_usuario(id_usuario)


def menu_usuarios():
    opcion = ""
    while opcion != "7":
        mostrar_menu_usuarios()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            opcion_crear_usuario()
        elif opcion == "2":
            opcion_ver_usuarios()
        elif opcion == "3":
            opcion_buscar_usuario()
        elif opcion == "4":
            opcion_buscar_usuario_nombre()
        elif opcion == "5":
            opcion_actualizar_usuario()
        elif opcion == "6":
            opcion_eliminar_usuario()
        elif opcion == "7":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida, intente de nuevo.")


# ==================== SUBMENÚ ALQUILERES ====================

def mostrar_menu_alquileres():
    print("\n--- MÓDULO ALQUILERES ---")
    print("1. Registrar alquiler")
    print("2. Procesar devolución")
    print("3. Volver al menú principal")
    print("------------------------")


def opcion_registrar_alquiler():
    print("\n-- Registrar alquiler --")
    placa = input("Placa del vehículo: ")
    fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
    resultado = alquiler_logica.registrar_alquiler(placa, fecha_inicio, fecha_fin)
    print(resultado)


def opcion_procesar_devolucion():
    print("\n-- Procesar devolución --")
    placa = input("Placa del vehículo: ")
    fecha_real = input("Fecha real devolución (YYYY-MM-DD): ")
    dano = float(input("Costo de daños (0 si no hay): "))
    resultado = devolucion_logica.procesar_devolucion(placa, fecha_real, dano)
    print(resultado)


def menu_alquileres():
    opcion = ""
    while opcion != "3":
        mostrar_menu_alquileres()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            opcion_registrar_alquiler()
        elif opcion == "2":
            opcion_procesar_devolucion()
        elif opcion == "3":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida, intente de nuevo.")


# ==================== MENÚ PRINCIPAL ====================

def main():
    opcion = ""
    while opcion != "6":
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_funcionarios()
        elif opcion == "3":
            menu_vehiculos()
        elif opcion == "4":
            menu_usuarios()
        elif opcion == "5":
            menu_alquileres()
        elif opcion == "6":
            print("Saliendo del sistema...")
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()