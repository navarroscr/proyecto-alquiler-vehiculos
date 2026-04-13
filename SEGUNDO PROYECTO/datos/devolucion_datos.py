from datos.db_sql import (
    insertar_devolucion,
    obtener_devoluciones,
    obtener_devolucion_por_alquiler
)


# Guarda una nueva devolución en la base de datos
def guardar_devolucion(devolucion_dict):
    resultado = insertar_devolucion(devolucion_dict)
    print("Devolución guardada:", devolucion_dict["id_devolucion"])
    return resultado


# Retorna todas las devoluciones registradas
def obtener_todas_las_devoluciones():
    return obtener_devoluciones()


# Busca la devolución asociada a un alquiler
def buscar_devolucion_por_alquiler(id_alquiler):
    return obtener_devolucion_por_alquiler(id_alquiler)