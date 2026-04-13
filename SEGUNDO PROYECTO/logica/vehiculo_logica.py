from logica.validaciones import *
from datos.db_mongo import insertar_vehiculo, obtener_vehiculos

def registrar_vehiculo(placa, marca):
    try:
        validar_vacio(placa, "placa")
        validar_vacio(marca, "marca")
        validar_placa(placa)

        lista = obtener_vehiculos()
        validar_duplicado(lista, placa, "placa")

        data = {
            "placa": placa,
            "marca": marca,
            "estado": "disponible"
        }

        insertar_vehiculo(data)

        return "Vehículo registrado correctamente"

    except Exception as e:
        return str(e)