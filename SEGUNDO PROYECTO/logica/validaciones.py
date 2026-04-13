import re


# Valida que un campo no esté vacío o sea None
def validar_vacio(valor, campo):
    if valor is None or str(valor).strip() == "":
        raise ValueError(f"{campo} no puede estar vacío.")


# Formato de placa (ABC-123)
def validar_formato_placa(placa):
    patron = r'^[A-Z]{3}-\d{3}$'
    if not re.match(patron, placa.strip().upper()):
        raise ValueError("Formato de placa inválido. Debe ser ABC-123.")


# Valida que no exista un valor duplicado en una lista de diccionarios
def validar_duplicado(lista, campo, valor):
    for item in lista:
        if item.get(campo) == valor:
            raise ValueError(f"Ya existe un registro con {campo}: {valor}.")


# Valida que un correo tenga formato básico válido
def validar_correo(correo):
    patron = r'^[\w.-]+@[\w.-]+\.\w+$'
    if not re.match(patron, correo.strip()):
        raise ValueError("El correo electrónico no tiene un formato válido.")


# Valida que un teléfono contenga solo dígitos y tenga entre 8 y 15 caracteres
def validar_telefono(telefono):
    telefono_str = str(telefono).strip()
    if not telefono_str.isdigit() or not (8 <= len(telefono_str) <= 15):
        raise ValueError("El teléfono debe contener solo números y tener entre 8 y 15 dígitos.")


# Valida que un número sea positivo
def validar_positivo(valor, campo):
    if not isinstance(valor, (int, float)) or valor <= 0:
        raise ValueError(f"{campo} debe ser un número mayor que 0.")


# Valida que una fecha de fin no sea anterior a la fecha de inicio
def validar_rango_fechas(fecha_inicio, fecha_fin):
    if fecha_fin < fecha_inicio:
        raise ValueError("La fecha de fin no puede ser anterior a la fecha de inicio.")