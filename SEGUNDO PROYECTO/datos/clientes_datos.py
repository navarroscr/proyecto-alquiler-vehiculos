from datos.conexion_mongo import obtener_base_datos

# Se obtiene clientes desde la base de datos
db = obtener_base_datos()
coleccion_clientes = db["clientes"]



# Inserta un cliente nuevo en la colección
# Recibe un diccionario con los datos del cliente

def insertar_cliente(cliente_diccionario):
    resultado = coleccion_clientes.insert_one(cliente_diccionario)
    print("Cliente insertado con id:", resultado.inserted_id)
    return resultado.inserted_id



# Devuelve todos los clientes guardados en la colección
# Retorna una lista de diccionarios

def obtener_clientes():
    lista = list(coleccion_clientes.find())
    return lista



# Busca un cliente por "id_cliente"


def buscar_cliente_por_id(id_cliente):
    cliente = coleccion_clientes.find_one({"id_cliente": id_cliente})
    return cliente



# Busca un cliente por su número de cédula

def buscar_cliente_por_cedula(cedula):
    cliente = coleccion_clientes.find_one({"cedula": cedula})
    return cliente



# Actualiza los datos de un cliente buscándolo por id_cliente


def actualizar_cliente(id_cliente, nuevos_datos):
    resultado = coleccion_clientes.update_one(
        {"id_cliente": id_cliente},
        {"$set": nuevos_datos}
    )
    print("Documentos modificados:", resultado.modified_count)
    return resultado.modified_count



# Elimina un cliente de la colección según su id_cliente

def eliminar_cliente(id_cliente):
    resultado = coleccion_clientes.delete_one({"id_cliente": id_cliente})
    print("Documentos eliminados:", resultado.deleted_count)
    return resultado.deleted_count