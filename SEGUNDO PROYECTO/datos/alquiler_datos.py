from datos.db_sql import (
    insertar_alquiler,
    obtener_alquileres,
    obtener_alquiler_por_id,
    obtener_alquileres_por_cliente,
    obtener_alquiler_activo_por_vehiculo,
    actualizar_estado_alquiler
)


# Guarda un nuevo alquiler en la base de datos
def guardar_alquiler(alquiler_dict):
    resultado = insertar_alquiler(alquiler_dict)
    print("Alquiler guardado:", alquiler_dict["id_alquiler"])
    return resultado


# Retorna todos los alquileres registrados
def obtener_todos_los_alquileres():
    return obtener_alquileres()


# Busca un alquiler por su id
def buscar_alquiler_por_id(id_alquiler):
    return obtener_alquiler_por_id(id_alquiler)


# Retorna el historial de alquileres de un cliente
def buscar_alquileres_cliente(id_cliente):
    return obtener_alquileres_por_cliente(id_cliente)


# Retorna el alquiler activo de un vehículo (pendiente o en prestamo)
def buscar_alquiler_activo(id_vehiculo):
    return obtener_alquiler_activo_por_vehiculo(id_vehiculo)


# Actualiza el estado de un alquiler (pendiente, en prestamo, finalizado, cancelado)
def cambiar_estado_alquiler(id_alquiler, nuevo_estado):
    actualizar_estado_alquiler(id_alquiler, nuevo_estado)
    print("Estado actualizado:", nuevo_estado)