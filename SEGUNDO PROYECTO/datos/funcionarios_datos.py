from datos.conexion_mongo import obtener_base_datos

# se obtiene funcionarios desde la base de datos 
db = obtener_base_datos()
coleccion_funcionarios = db["funcionarios"]


# Inserta un funcionario nuevo en la colección

def insertar_funcionario(funcionario_diccionario):
    resultado = coleccion_funcionarios.insert_one(funcionario_diccionario)
    print("Funcionario insertado con id:", resultado.inserted_id)
    return resultado.inserted_id


# Devuelve todos los funcionarios guardados en la colección
def obtener_funcionarios():
    lista = list(coleccion_funcionarios.find())
    return lista


# Busca un funcionario por su campo "id_funcionario"
def buscar_funcionario_por_id(id_funcionario):
    funcionario = coleccion_funcionarios.find_one({"id_funcionario": id_funcionario})
    return funcionario


# Busca un funcionario por su número de cédula
def buscar_funcionario_por_cedula(cedula):
    funcionario = coleccion_funcionarios.find_one({"cedula": cedula})
    return funcionario


# Actualiza los datos de un funcionario buscándolo por id_funcionario

def actualizar_funcionario(id_funcionario, nuevos_datos):
    resultado = coleccion_funcionarios.update_one(
        {"id_funcionario": id_funcionario},
        {"$set": nuevos_datos}
    )
    print("Documentos modificados:", resultado.modified_count)
    return resultado.modified_count


# Elimina un funcionario de la colección según su id_funcionario
def eliminar_funcionario(id_funcionario):
    resultado = coleccion_funcionarios.delete_one({"id_funcionario": id_funcionario})
    print("Documentos eliminados:", resultado.deleted_count)
    return resultado.deleted_count