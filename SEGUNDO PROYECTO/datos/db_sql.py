from datos.conexion_sql import obtener_conexion


# ============================================
# ALQUILERES
# ============================================

def insertar_alquiler(alquiler_dict):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO alquileres VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            alquiler_dict["id_alquiler"], alquiler_dict["id_cliente"],
            alquiler_dict["id_vehiculo"], alquiler_dict["fecha_inicio"],
            alquiler_dict["fecha_fin"], alquiler_dict["cantidad_dias"],
            alquiler_dict["costo_diario"], alquiler_dict["subtotal"],
            alquiler_dict["impuesto"], alquiler_dict["seguro_diario"],
            alquiler_dict["total"], alquiler_dict["estado"]
        ))
        conn.commit()
    except Exception as e:
        print("Error al insertar alquiler:", e)
        raise
    finally:
        conn.close()


def obtener_alquileres():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alquileres")
        columnas = [col[0] for col in cursor.description]
        return [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    except Exception as e:
        print("Error al obtener alquileres:", e)
        raise
    finally:
        conn.close()


def obtener_alquiler_por_id(id_alquiler):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alquileres WHERE id_alquiler = ?", (id_alquiler,))
        columnas = [col[0] for col in cursor.description]
        fila = cursor.fetchone()
        return dict(zip(columnas, fila)) if fila else None
    except Exception as e:
        print("Error al buscar alquiler:", e)
        raise
    finally:
        conn.close()


def obtener_alquileres_por_cliente(id_cliente):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alquileres WHERE id_cliente = ?", (id_cliente,))
        columnas = [col[0] for col in cursor.description]
        return [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    except Exception as e:
        print("Error al obtener alquileres del cliente:", e)
        raise
    finally:
        conn.close()


# Retorna el alquiler activo (pendiente o en prestamo) de un vehículo
def obtener_alquiler_activo_por_vehiculo(id_vehiculo):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM alquileres
            WHERE id_vehiculo = ? AND estado IN ('pendiente', 'en prestamo')
        """, (id_vehiculo,))
        columnas = [col[0] for col in cursor.description]
        fila = cursor.fetchone()
        return dict(zip(columnas, fila)) if fila else None
    except Exception as e:
        print("Error al buscar alquiler activo:", e)
        raise
    finally:
        conn.close()


def actualizar_estado_alquiler(id_alquiler, nuevo_estado):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("UPDATE alquileres SET estado = ? WHERE id_alquiler = ?", (nuevo_estado, id_alquiler))
        conn.commit()
    except Exception as e:
        print("Error al actualizar estado:", e)
        raise
    finally:
        conn.close()


# ============================================
# DEVOLUCIONES
# ============================================

def insertar_devolucion(devolucion_dict):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO devoluciones VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            devolucion_dict["id_devolucion"], devolucion_dict["id_alquiler"],
            devolucion_dict["fecha_devolucion"], devolucion_dict["dias_retraso"],
            devolucion_dict["interes"], devolucion_dict["impuesto"],
            devolucion_dict["seguro"], devolucion_dict["hay_danos"],
            devolucion_dict["descripcion_dano"], devolucion_dict["costo_danos"],
            devolucion_dict["total"]
        ))
        conn.commit()
    except Exception as e:
        print("Error al insertar devolución:", e)
        raise
    finally:
        conn.close()


def obtener_devoluciones():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM devoluciones")
        columnas = [col[0] for col in cursor.description]
        return [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    except Exception as e:
        print("Error al obtener devoluciones:", e)
        raise
    finally:
        conn.close()


def obtener_devolucion_por_alquiler(id_alquiler):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM devoluciones WHERE id_alquiler = ?", (id_alquiler,))
        columnas = [col[0] for col in cursor.description]
        fila = cursor.fetchone()
        return dict(zip(columnas, fila)) if fila else None
    except Exception as e:
        print("Error al buscar devolución:", e)
        raise
    finally:
        conn.close()