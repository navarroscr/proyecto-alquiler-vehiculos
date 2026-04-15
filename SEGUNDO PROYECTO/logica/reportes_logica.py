from datetime import datetime
import datos.alquiler_datos as alquiler_datos
import datos.vehiculo_datos as vehiculo_datos
import datos.clientes_datos as clientes_datos


def obtener_vehiculos_mas_rentados(desde_str, hasta_str):
    """
    Retorna los datos necesarios para el grafico de vehiculos mas rentados.
    
    Parametros:
        desde_str: fecha inicial en formato YYYY-MM-DD
        hasta_str: fecha final en formato YYYY-MM-DD
    
    Retorna:
        tuple: (etiquetas, valores, porcentajes) para el grafico de barras
    """
    try:
        desde = datetime.strptime(desde_str, "%Y-%m-%d").date()
        hasta = datetime.strptime(hasta_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Formato de fecha invalido. Use YYYY-MM-DD.")

    # Obtener todos los alquileres
    alquileres = alquiler_datos.obtener_todos_los_alquileres()
    
    # Contar alquileres por vehiculo en el rango de fechas
    conteo = {}
    for a in alquileres:
        try:
            fecha_inicio = a.get("fecha_inicio")
            if isinstance(fecha_inicio, str):
                fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
            elif hasattr(fecha_inicio, "date"):
                fecha_inicio = fecha_inicio.date()
            
            if desde <= fecha_inicio <= hasta:
                id_v = str(a.get("id_vehiculo", ""))
                conteo[id_v] = conteo.get(id_v, 0) + 1
        except Exception:
            continue

    if not conteo:
        return [], [], []

    # Obtener nombre del modelo para cada vehiculo
    etiquetas = []
    valores = []
    for id_v, cantidad in sorted(conteo.items(), key=lambda x: x[1], reverse=True):
        vehiculo = vehiculo_datos.buscar_vehiculo_por_id(id_v)
        if vehiculo:
            nombre = f"{vehiculo.get('marca', '')} {vehiculo.get('tipo', '')}"
        else:
            nombre = id_v
        etiquetas.append(nombre)
        valores.append(cantidad)

    # Calcular porcentajes
    total_alquileres = sum(valores)
    porcentajes = [(v / total_alquileres) * 100 for v in valores]

    return etiquetas, valores, porcentajes


def obtener_segmentacion_edades(anio_str):
    """
    Retorna los datos para el grafico de segmentacion de clientes por edad.
    
    Parametros:
        anio_str: año en formato YYYY
    
    Retorna:
        tuple: (datos_activos, meses) donde datos_activos es un diccionario
               con rangos de edad como claves y listas de 12 meses como valores
    """
    try:
        anio = int(anio_str)
    except ValueError:
        raise ValueError("Ingrese un año valido (ej: 2025).")

    # Rangos de edad segun el enunciado
    rangos = [
        (18, 19, "18-19"),
        (20, 24, "20-24"),
        (25, 29, "25-29"),
        (30, 34, "30-34"),
        (35, 39, "35-39"),
        (40, 44, "40-44"),
        (45, 49, "45-49"),
        (50, 54, "50-54"),
        (55, 59, "55-59"),
        (60, 99, "60+"),
    ]

    # Obtener todos los alquileres del año indicado
    alquileres = alquiler_datos.obtener_todos_los_alquileres()
    alquileres_anio = []
    for a in alquileres:
        try:
            fecha_inicio = a.get("fecha_inicio")
            if isinstance(fecha_inicio, str):
                fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
            elif hasattr(fecha_inicio, "date"):
                fecha_inicio = fecha_inicio.date()
            if fecha_inicio.year == anio:
                alquileres_anio.append((a, fecha_inicio))
        except Exception:
            continue

    if not alquileres_anio:
        return {}, []

    # Cargar clientes en un diccionario para busqueda rapida
    clientes = {c.get("id_cliente"): c for c in clientes_datos.obtener_clientes()}

    # Contar alquileres por rango de edad y mes
    datos = {r[2]: [0] * 12 for r in rangos}

    for alquiler, fecha_inicio in alquileres_anio:
        id_cliente = str(alquiler.get("id_cliente", ""))
        cliente = clientes.get(id_cliente)
        if not cliente:
            continue

        # Calcular edad del cliente
        nacimiento = cliente.get("fecha_nacimiento")
        if not nacimiento:
            continue
        try:
            if isinstance(nacimiento, str):
                nacimiento = datetime.strptime(nacimiento, "%Y-%m-%d").date()
            elif hasattr(nacimiento, "date"):
                nacimiento = nacimiento.date()

            edad = (fecha_inicio - nacimiento).days // 365
        except Exception:
            continue

        # Buscar en que rango cae
        mes = fecha_inicio.month - 1
        for min_e, max_e, etiqueta in rangos:
            if min_e <= edad <= max_e:
                datos[etiqueta][mes] += 1
                break

    # Filtrar rangos que tienen al menos un alquiler
    datos_activos = {k: v for k, v in datos.items() if any(v)}

    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
             "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

    return datos_activos, meses