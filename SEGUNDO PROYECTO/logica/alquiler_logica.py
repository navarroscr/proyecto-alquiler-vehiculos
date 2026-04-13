from datetime import datetime
import uuid
from logica.clase_alquiler import Alquiler
from datos.alquiler_datos import guardar_alquiler, buscar_alquiler_activo, cambiar_estado_alquiler
from datos.vehiculo_datos import buscar_vehiculo_por_id, actualizar_vehiculo


# Calcula la cantidad de días entre dos fechas (mínimo 1 día)
def calcular_dias(fecha_inicio, fecha_fin):
    dias = (fecha_fin - fecha_inicio).days
    return dias if dias > 0 else 1


# Calcula el desglose de costos del alquiler
def calcular_costos(dias, costo_diario, seguro_diario):
    subtotal = dias * costo_diario
    impuesto = subtotal * 0.13
    seguro = dias * seguro_diario
    total = subtotal + impuesto + seguro
    return subtotal, impuesto, seguro, total


def registrar_alquiler(id_cliente, id_vehiculo, fecha_inicio_str, fecha_fin_str, seguro_diario):
    try:
        # Validar que el vehículo exista
        vehiculo = buscar_vehiculo_por_id(id_vehiculo)
        if not vehiculo:
            raise ValueError("El vehículo no existe.")

        # Validar que el vehículo esté disponible
        if vehiculo["estado"] != "disponible":
            raise ValueError("El vehículo no está disponible para alquiler.")

        # Convertir fechas
        fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d").date()
        fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d").date()
        hoy = datetime.now().date()

        # Validar que las fechas no sean pasadas
        if fecha_inicio < hoy:
            raise ValueError("La fecha de inicio no puede ser anterior a hoy.")

        if fecha_fin < fecha_inicio:
            raise ValueError("La fecha de fin no puede ser anterior a la fecha de inicio.")

        # Validar que no haya un alquiler activo para ese vehículo
        alquiler_activo = buscar_alquiler_activo(id_vehiculo)
        if alquiler_activo:
            raise ValueError("El vehículo ya tiene un alquiler activo.")

        # Calcular días y costos
        dias = calcular_dias(fecha_inicio, fecha_fin)
        costo_diario = vehiculo["costo_diario"]
        subtotal, impuesto, seguro, total = calcular_costos(dias, costo_diario, seguro_diario)

        # Crear objeto alquiler con validaciones de la clase
        id_alquiler = str(uuid.uuid4())[:8]
        nuevo_alquiler = Alquiler(
            id_alquiler, id_cliente, id_vehiculo,
            fecha_inicio_str, fecha_fin_str,
            dias, costo_diario, subtotal, impuesto, seguro, total, "pendiente"
        )

        # Guardar en base de datos
        alquiler_dict = {
            "id_alquiler": nuevo_alquiler.id_alquiler,
            "id_cliente": nuevo_alquiler.id_cliente,
            "id_vehiculo": nuevo_alquiler.id_vehiculo,
            "fecha_inicio": nuevo_alquiler.fecha_inicio,
            "fecha_fin": nuevo_alquiler.fecha_fin,
            "cantidad_dias": nuevo_alquiler.cantidad_dias,
            "costo_diario": nuevo_alquiler.costo_diario,
            "subtotal": nuevo_alquiler.subtotal,
            "impuesto": nuevo_alquiler.impuesto,
            "seguro_diario": nuevo_alquiler.seguro,
            "total": nuevo_alquiler.total,
            "estado": nuevo_alquiler.estado
        }
        guardar_alquiler(alquiler_dict)

        # Cambiar estado del vehículo a reservado
        actualizar_vehiculo(id_vehiculo, {"estado": "reservado"})

        # Retornar desglose para mostrar al usuario
        return {
            "id_alquiler": id_alquiler,
            "dias": dias,
            "subtotal": subtotal,
            "impuesto": impuesto,
            "seguro": seguro,
            "total": total
        }

    except ValueError as e:
        print("Error de validación:", e)
        raise
    except Exception as e:
        print("Error al registrar alquiler:", e)
        raise


# Cambia el estado de un alquiler de pendiente a en prestamo
# Se llama cuando el funcionario entrega el vehículo al cliente
def activar_alquiler(id_alquiler, id_vehiculo):
    try:
        cambiar_estado_alquiler(id_alquiler, "en prestamo")
        actualizar_vehiculo(id_vehiculo, {"estado": "en prestamo"})
        print("Alquiler activado correctamente.")
    except Exception as e:
        print("Error al activar alquiler:", e)
        raise