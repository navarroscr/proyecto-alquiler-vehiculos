class Devolucion:
    def __init__(self, id_devolucion, id_alquiler, fecha_devolucion, dias_retraso,
                 interes, impuesto, seguro, hay_danos, descripcion_dano, costo_danos, total):
        """Constructor"""
        self._id_devolucion = id_devolucion
        self.id_alquiler = id_alquiler
        self.fecha_devolucion = fecha_devolucion
        self.dias_retraso = dias_retraso
        self.interes = interes
        self.impuesto = impuesto
        self.seguro = seguro
        self.hay_danos = hay_danos
        self.descripcion_dano = descripcion_dano
        self.costo_danos = costo_danos
        self.total = total

    @property
    def id_devolucion(self):
       
        return self._id_devolucion

    @property
    def id_alquiler(self):
        
        return self._id_alquiler

    @id_alquiler.setter
    def id_alquiler(self, value):
       
        if not value.strip():
            raise ValueError("El id_alquiler no puede estar vacío.")
        self._id_alquiler = value

    @property
    def fecha_devolucion(self):
       
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, value):
       
        if not value.strip():
            raise ValueError("La fecha de devolución no puede estar vacía.")
        self._fecha_devolucion = value

    @property
    def dias_retraso(self):
       
        return self._dias_retraso

    @dias_retraso.setter
    def dias_retraso(self, value):
        
        if not isinstance(value, int) or value < 0:
            raise ValueError("Los días de retraso deben ser un número entero mayor o igual que 0.")
        self._dias_retraso = value

    @property
    def interes(self):
        
        return self._interes

    @interes.setter
    def interes(self, value):
       
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("El interés debe ser un número mayor o igual que 0.")
        self._interes = value

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
    def hay_danos(self):
        
        return self._hay_danos

    @hay_danos.setter
    def hay_danos(self, value):
        
        if not isinstance(value, bool):
            raise ValueError("La información de daños debe ser True o False.")
        self._hay_danos = value

    @property
    def descripcion_dano(self):
       
        return self._descripcion_dano

    @descripcion_dano.setter
    def descripcion_dano(self, value):
        
        if getattr(self, "_hay_danos", False):
            if not value.strip():
                raise ValueError("La descripción del daño no puede estar vacía si hay daños.")
        self._descripcion_dano = value

    @property
    def costo_danos(self):
       
        return self._costo_danos

    @costo_danos.setter
    def costo_danos(self, value):
        
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("El costo de daños debe ser un número mayor o igual que 0.")
        self._costo_danos = value

    @property
    def total(self):
        
        return self._total

    @total.setter
    def total(self, value):
        
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("El total debe ser un número mayor o igual que 0.")
        self._total = value