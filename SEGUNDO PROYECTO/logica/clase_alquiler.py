

class Alquiler:
    def __init__(self, id_alquiler, id_cliente, id_vehiculo, fecha_inicio, fecha_fin,
                 cantidad_dias, costo_diario, subtotal, impuesto, seguro, total, estado):
        """Constructor"""
        self._id_alquiler = id_alquiler 
        self.id_cliente = id_cliente
        self.id_vehiculo = id_vehiculo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.cantidad_dias = cantidad_dias
        self.costo_diario = costo_diario
        self.subtotal = subtotal
        self.impuesto = impuesto
        self.seguro = seguro
        self.total = total
        self.estado = estado

    @property
    def id_alquiler(self):
       
        return self._id_alquiler

    @property
    def id_cliente(self):
        
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, value):
       
        if not str(value).strip():
            raise ValueError("El id_cliente no puede estar vacío.")
        self._id_cliente = value

    @property
    def id_vehiculo(self):
        
        return self._id_vehiculo

    @id_vehiculo.setter
    def id_vehiculo(self, value):
       
        if not str(value).strip():
            raise ValueError("El id_vehiculo no puede estar vacío.")
        self._id_vehiculo = value

    @property
    def fecha_inicio(self):
        
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
       
        if not str(value).strip():
            raise ValueError("La fecha de inicio no puede estar vacía.")
        self._fecha_inicio = value

    @property
    def fecha_fin(self):
        
        return self._fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, value):
        
        if not str(value).strip():
            raise ValueError("La fecha de fin no puede estar vacía.")
        self._fecha_fin = value

    @property
    def cantidad_dias(self):
       
        return self._cantidad_dias

    @cantidad_dias.setter
    def cantidad_dias(self, value):
       
        if not isinstance(value, int) or value <= 0:
            raise ValueError("La cantidad de días debe ser un número entero mayor que 0.")
        self._cantidad_dias = value

    @property
    def costo_diario(self):
       
        return self._costo_diario

    @costo_diario.setter
    def costo_diario(self, value):
       
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("El costo diario debe ser un número mayor que 0.")
        self._costo_diario = value

    @property
    def subtotal(self):
       
        return self._subtotal

    @subtotal.setter
    def subtotal(self, value):
        
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("El subtotal debe ser un número mayor o igual que 0.")
        self._subtotal = value

    @property
    def impuesto(self):
        
        return self._impuesto

    @impuesto.setter
    def impuesto(self, value):
       
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("El impuesto debe ser un número mayor o igual que 0.")
        self._impuesto = value

    @property
    def seguro(self):
      
        return self._seguro

    @seguro.setter
    def seguro(self, value):
      
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("El seguro debe ser un número mayor o igual que 0.")
        self._seguro = value

    @property
    def total(self):
      
        return self._total

    @total.setter
    def total(self, value):
       
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("El total debe ser un número mayor o igual que 0.")
        self._total = value

    @property
    def estado(self):
       
        return self._estado

    @estado.setter
    def estado(self, value):
        estados_permitidos = ["pendiente", "en prestamo", "finalizado", "cancelado"]
        estado_normalizado = value.strip().lower()
        if estado_normalizado not in estados_permitidos:
            raise ValueError("El estado debe ser 'pendiente', 'en prestamo', 'finalizado' o 'cancelado'.")
        self._estado = estado_normalizado