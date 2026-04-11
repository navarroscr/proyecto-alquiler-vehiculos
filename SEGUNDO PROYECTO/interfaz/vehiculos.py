from logica.clase_vehiculo import Vehiculo
import datos.vehiculo_datos as vehiculo_datos


# Crea un objeto Vehiculo como diccionario
def crear_vehiculo(id_vehiculo, marca, tipo, placa, numero_motor, transmision, combustible, color, cantidad_pasajeros, costo_diario, cantidad_maletas, imagen):
    nuevo_vehiculo = Vehiculo(id_vehiculo, marca, tipo, placa, numero_motor, transmision, combustible, color, cantidad_pasajeros, costo_diario, cantidad_maletas, imagen)

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


# Obtiene todos los vehículos guardados en la base de datos
def obtener_todos_los_vehiculos():
    lista = vehiculo_datos.obtener_vehiculos()
    return lista


# Busca un vehículo por su id_vehiculo
def buscar_vehiculo(id_vehiculo):
    vehiculo = vehiculo_datos.buscar_vehiculo_por_id(id_vehiculo)
    return vehiculo


# Busca un vehículo por su placa
def buscar_vehiculo_placa(placa):
    vehiculo = vehiculo_datos.buscar_vehiculo_por_placa(placa)
    return vehiculo


# Actualiza los datos de un vehículo según su id_vehiculo
def actualizar_vehiculo(id_vehiculo, nuevos_datos):
    vehiculo_datos.actualizar_vehiculo(id_vehiculo, nuevos_datos)
    print("Vehículo actualizado correctamente")


# Elimina un vehículo según su id_vehiculo
def eliminar_vehiculo(id_vehiculo):
    vehiculo_datos.eliminar_vehiculo(id_vehiculo)
    print("Vehículo eliminado correctamente")