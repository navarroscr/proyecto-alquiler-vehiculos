from datos.conexion_mongo import obtener_base_datos

# Se obtiene vehiculos desde la base de datos
db = obtener_base_datos()
coleccion_vehiculos = db["vehiculos"]


# Inserta un vehículo nuevo como diccionario
def insertar_vehiculo(vehiculo_diccionario):
    resultado = coleccion_vehiculos.insert_one(vehiculo_diccionario)
    print("Vehículo insertado con id:", resultado.inserted_id)
    return resultado.inserted_id


# Devuelve todos los vehículos guardados en la colección
def obtener_vehiculos():
    lista = list(coleccion_vehiculos.find())
    return lista


# Busca un vehículo por su campo "id_vehiculo"
def buscar_vehiculo_por_id(id_vehiculo):
    vehiculo = coleccion_vehiculos.find_one({"id_vehiculo": id_vehiculo})
    return vehiculo


# Busca un vehículo por su número de placa
def buscar_vehiculo_por_placa(placa):
    vehiculo = coleccion_vehiculos.find_one({"placa": placa})
    return vehiculo


# Actualiza los datos de un vehículo buscándolo por id_vehiculo

def actualizar_vehiculo(id_vehiculo, nuevos_datos):
    resultado = coleccion_vehiculos.update_one(
        {"id_vehiculo": id_vehiculo},
        {"$set": nuevos_datos}
    )
    print("Documentos modificados:", resultado.modified_count)
    return resultado.modified_count


# Elimina un vehículo de la colección según su id_vehiculo
def eliminar_vehiculo(id_vehiculo):
    resultado = coleccion_vehiculos.delete_one({"id_vehiculo": id_vehiculo})
    print("Documentos eliminados:", resultado.deleted_count)
    return resultado.deleted_count