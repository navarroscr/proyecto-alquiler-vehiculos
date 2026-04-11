from datos.conexion_mongo import obtener_base_datos

# Se obtiene usuarios desde la base de datos
db = obtener_base_datos()
coleccion_usuarios = db["usuarios"]


# Inserta un usuario nuevo como diccionario

def insertar_usuario(usuario_diccionario):
    resultado = coleccion_usuarios.insert_one(usuario_diccionario)
    print("Usuario insertado con id:", resultado.inserted_id)
    return resultado.inserted_id


# Devuelve todos los usuarios guardados en la colección
def obtener_usuarios():
    lista = list(coleccion_usuarios.find())
    return lista


# Busca un usuario por su campo "id_usuario"
def buscar_usuario_por_id(id_usuario):
    usuario = coleccion_usuarios.find_one({"id_usuario": id_usuario})
    return usuario


# Busca un usuario por su nombre de usuario
def buscar_usuario_por_nombre(nombre_usuario):
    usuario = coleccion_usuarios.find_one({"nombre_usuario": nombre_usuario})
    return usuario


# Actualiza los datos de un usuario buscándolo por id_usuario

def actualizar_usuario(id_usuario, nuevos_datos):
    resultado = coleccion_usuarios.update_one(
        {"id_usuario": id_usuario},
        {"$set": nuevos_datos}
    )
    print("Documentos modificados:", resultado.modified_count)
    return resultado.modified_count


# Elimina un usuario de la colección según su id_usuario
def eliminar_usuario(id_usuario):
    resultado = coleccion_usuarios.delete_one({"id_usuario": id_usuario})
    print("Documentos eliminados:", resultado.deleted_count)
    return resultado.deleted_count