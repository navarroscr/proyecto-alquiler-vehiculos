from logica.clase_clientes import Cliente
import datos.clientes_datos as clientes_datos


# crear el objeto cliente como diccionario 
def crear_cliente(id_cliente, nombre, cedula, telefono, correo, direccion):
    nuevo_cliente = Cliente(id_cliente, nombre, cedula, telefono, correo, direccion, "activo")

    cliente_diccionario = {
        "id_cliente": nuevo_cliente.id_cliente,
        "nombre": nuevo_cliente.nombre,
        "cedula": nuevo_cliente.cedula,
        "telefono": nuevo_cliente.telefono,
        "correo": nuevo_cliente.correo,
        "direccion": nuevo_cliente.direccion,
        "estado": nuevo_cliente.estado
    }

    clientes_datos.insertar_cliente(cliente_diccionario)
    print("Cliente creado correctamente:", nombre)


# Obtiene todos los clientes guardados en la base de datos
def obtener_todos_los_clientes():
    lista = clientes_datos.obtener_clientes()
    return lista


# Busca un cliente por su id_cliente
def buscar_cliente(id_cliente):
    cliente = clientes_datos.buscar_cliente_por_id(id_cliente)
    return cliente


# Actualiza los datos de un cliente según su id_cliente
def actualizar_cliente(id_cliente, nuevos_datos):
    clientes_datos.actualizar_cliente(id_cliente, nuevos_datos)
    print("Cliente actualizado correctamente")


# Elimina un cliente según su id_cliente
def eliminar_cliente(id_cliente):
    clientes_datos.eliminar_cliente(id_cliente)
    print("Cliente eliminado correctamente")