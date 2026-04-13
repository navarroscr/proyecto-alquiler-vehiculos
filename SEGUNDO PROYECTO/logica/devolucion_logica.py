from datetime import datetime
import uuid
from logica.clase_devolucion import Devolucion
from datos.devolucion_datos import guardar_devolucion
from datos.alquiler_datos import buscar_alquiler_por_id, cambiar_estado_alquiler
from datos.vehiculo_datos import actualizar_vehiculo


# Calcula el costo de mora por días de retraso
# Incluye días extra + 15% interés + 13% impuesto + seguro por días
def calcular_mora(dias_retraso, costo_diario, seguro_diario):
    if dias_retraso <= 0:
        return 0, 0, 0, 0

    subtotal = dias_retraso * costo_diario
    interes = subtotal * 0.15
    impuesto = subtotal * 0.13
    seguro = dias_retraso * seguro_diario

    return subtotal, interes, impuesto, seguro


def procesar_devolucion(id_alquiler, fecha_devolucion_str, hay_danos, descripcion_dano, costo_danos, seguro_diario):
    try:
        # Verificar que el alquiler exista
        alquiler = buscar_alquiler_por_id(id_alquiler)
        if not alquiler:
            raise ValueError("El alquiler no existe.")

        # Verificar que el alquiler esté activo
        if alquiler["estado"] != "en prestamo":
            raise ValueError("El alquiler no está en estado 'en prestamo'.")

        # Convertir fechas
        fecha_devolucion = datetime.strptime(fecha_devolucion_str, "%Y-%m-%d").date()
        fecha_fin = alquiler["fecha_fin"]

        # Si fecha_fin viene como string lo convertimos
        if isinstance(fecha_fin, str):
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()

        # Calcular días de retraso
        dias_retraso = (fecha_devolucion - fecha_fin).days
        if dias_retraso < 0:
            dias_retraso = 0

        # Calcular mora si hay retraso
        costo_diario = alquiler["costo_diario"]
        subtotal_mora, interes, impuesto_mora, seguro_mora = calcular_mora(dias_retraso, costo_diario, seguro_diario)

        # Total a pagar: mora + daños
        total = subtotal_mora + interes + impuesto_mora + seguro_mora + costo_danos

        # Crear objeto devolución con validaciones de la clase
        id_devolucion = str(uuid.uuid4())[:8]
        nueva_devolucion = Devolucion(
            id_devolucion, id_alquiler, fecha_devolucion_str,
            dias_retraso, interes, impuesto_mora, seguro_mora,
            hay_danos, descripcion_dano, costo_danos, total
        )

        # Guardar devolución en base de datos
        devolucion_dict = {
            "id_devolucion": nueva_devolucion.id_devolucion,
            "id_alquiler": nueva_devolucion.id_alquiler,
            "fecha_devolucion": nueva_devolucion.fecha_devolucion,
            "dias_retraso": nueva_devolucion.dias_retraso,
            "interes": nueva_devolucion.interes,
            "impuesto": nueva_devolucion.impuesto,
            "seguro": nueva_devolucion.seguro,
            "hay_danos": nueva_devolucion.hay_danos,
            "descripcion_dano": nueva_devolucion.descripcion_dano,
            "costo_danos": nueva_devolucion.costo_danos,
            "total": nueva_devolucion.total
        }
        guardar_devolucion(devolucion_dict)

        # Actualizar estado del alquiler a finalizado
        cambiar_estado_alquiler(id_alquiler, "finalizado")

        # Volver a poner el vehículo como disponible
        actualizar_vehiculo(alquiler["id_vehiculo"], {"estado": "disponible"})

        # Retornar desglose para mostrar al usuario
        return {
            "id_devolucion": id_devolucion,
            "dias_retraso": dias_retraso,
            "interes": interes,
            "impuesto_mora": impuesto_mora,
            "seguro_mora": seguro_mora,
            "costo_danos": costo_danos,
            "total": total
        }

    except ValueError as e:
        print("Error de validación:", e)
        raise
    except Exception as e:
        print("Error al procesar devolución:", e)
        raise