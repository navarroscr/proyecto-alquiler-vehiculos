from logica.clase_vehiculo import Vehiculo
import datos.vehiculo_datos as vehiculo_datos


# Crea un vehículo nuevo con el estado 'disponible' por defecto
def crear_vehiculo(id_vehiculo, marca, tipo, placa, numero_motor, transmision,
                   combustible, color, cantidad_pasajeros, costo_diario,
                   cantidad_maletas, imagen):
    nuevo_vehiculo = Vehiculo(
        id_vehiculo, marca, tipo, placa, numero_motor, transmision,
        combustible, color, cantidad_pasajeros, costo_diario,
        cantidad_maletas, imagen, "disponible"  # estado inicial siempre disponible
    )

    vehiculo_diccionario = {
        "id_vehiculo": nuevo_vehiculo.id_vehiculo,
        "marca": nuevo_vehiculo.marca,
        "tipo": nuevo_vehiculo.tipo,
        "placa": nuevo_vehiculo.placa,
        "numero_motor": nuevo_vehiculo.numero_motor,
        "transmision": nuevo_vehiculo.transmision,
        "combustible": nuevo_vehiculo.combustible,
        "color": nuevo_vehiculo.color,
        "cantidad_pasajeros": nuevo_vehiculo.cantidad_pasajeros,
        "costo_diario": nuevo_vehiculo.costo_diario,
        "cantidad_maletas": nuevo_vehiculo.cantidad_maletas,
        "imagen": nuevo_vehiculo.imagen,
        "estado": nuevo_vehiculo.estado
    }

    vehiculo_datos.insertar_vehiculo(vehiculo_diccionario)
    print("Vehículo creado correctamente:", marca, placa)


# Obtiene todos los vehículos (activos e inactivos)
def obtener_todos_los_vehiculos():
    return vehiculo_datos.obtener_vehiculos()


# Retorna solo los vehiculos que estan disponibles para alquiler 
def obtener_vehiculos_disponibles():
    lista = vehiculo_datos.obtener_vehiculos()
    return [v for v in lista if v.get("estado") == "disponible"]


# Busca un vehículo por su id_vehiculo
def buscar_vehiculo(id_vehiculo):
    return vehiculo_datos.buscar_vehiculo_por_id(id_vehiculo)


# Busca un vehículo por su placa
def buscar_vehiculo_placa(placa):
    return vehiculo_datos.buscar_vehiculo_por_placa(placa)


# Actualiza los datos de un vehículo según su id_vehiculo
def actualizar_vehiculo(id_vehiculo, nuevos_datos):
    vehiculo_datos.actualizar_vehiculo(id_vehiculo, nuevos_datos)
    print("Vehículo actualizado correctamente")


# se elimina el vehiculo (borrado lógico)

def eliminar_vehiculo(id_vehiculo):
    vehiculo_datos.actualizar_vehiculo(id_vehiculo, {"estado": "inactivo"})
    print("Vehículo desactivado correctamente")