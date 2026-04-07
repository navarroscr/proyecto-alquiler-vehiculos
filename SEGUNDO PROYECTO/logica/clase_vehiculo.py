# Archivo: clase_vehiculo.py

class Vehiculo:
    """Clase que representa un vehículo en el sistema de gestión de alquiler de vehículos."""

    def __init__(self, id_vehiculo, marca, tipo, placa, numero_motor, transmision,
                 combustible, color, cantidad_pasajeros, costo_diario, cantidad_maletas,
                 imagen, estado):
        """Constructor"""
        self._id_vehiculo = id_vehiculo
        self.marca = marca  
        self.tipo = tipo 
        self.placa = placa  
        self.numero_motor = numero_motor  
        self.transmision = transmision  
        self.combustible = combustible  
        self.color = color  
        self.cantidad_pasajeros = cantidad_pasajeros  
        self.costo_diario = costo_diario  
        self.cantidad_maletas = cantidad_maletas  
        self.imagen = imagen  
        self.estado = estado  

    @property
    def id_vehiculo(self):
        
        return self._id_vehiculo

    @property
    def marca(self):
        
        return self._marca

    @marca.setter
    def marca(self, valor):
        
        if not valor.strip():
            raise ValueError("La marca no puede estar vacía.")
        self._marca = valor

    @property
    def tipo(self):
       
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
       
        if not valor.strip():
            raise ValueError("El tipo no puede estar vacío.")
        self._tipo = valor

    @property
    def placa(self):
        
        return self._placa

    @placa.setter
    def placa(self, valor):
        
        if not valor.strip():
            raise ValueError("La placa no puede estar vacía.")
        self._placa = valor

    @property
    def numero_motor(self):
       
        return self._numero_motor

    @numero_motor.setter
    def numero_motor(self, valor):
       
        if not valor.strip():
            raise ValueError("El número de motor no puede estar vacío.")
        self._numero_motor = valor

    @property
    def transmision(self):
       
        return self._transmision

    @transmision.setter
    def transmision(self, valor):
        
        valor = valor.lower() 
        if valor not in ["manual", "automatico"]:
            raise ValueError("La transmisión debe ser 'manual' o 'automatico'.")
        self._transmision = valor

    @property
    def combustible(self):
        
        return self._combustible

    @combustible.setter
    def combustible(self, valor):
       
        valor = valor.strip().lower() 
        if valor not in ["gasolina", "diesel", "electrico"]:
            raise ValueError("El combustible debe ser 'gasolina', 'diesel' o 'electrico'.")
        self._combustible = valor

    @property
    def color(self):
        
        return self._color

    @color.setter
    def color(self, valor):
       
        if not valor.strip():
            raise ValueError("El color no puede estar vacío.")
        self._color = valor

    @property
    def cantidad_pasajeros(self):
       
        return self._cantidad_pasajeros

    @cantidad_pasajeros.setter
    def cantidad_pasajeros(self, valor):
       
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("La cantidad de pasajeros debe ser un número entero mayor que 0.")
        self._cantidad_pasajeros = valor

    @property
    def costo_diario(self):
       
        return self._costo_diario

    @costo_diario.setter
    def costo_diario(self, valor):
       
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El costo diario debe ser un número mayor que 0.")
        self._costo_diario = valor

    @property
    def cantidad_maletas(self):
       
        return self._cantidad_maletas

    @cantidad_maletas.setter
    def cantidad_maletas(self, valor):
       
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La cantidad de maletas debe ser un número entero igual o mayor que 0.")
        self._cantidad_maletas = valor

    @property
    def imagen(self):
      
        return self._imagen

    @imagen.setter
    def imagen(self, valor):
       
        if not valor.strip():
            raise ValueError("La imagen no puede estar vacía.")
        self._imagen = valor

    @property
    def estado(self):
        
        return self._estado

    @estado.setter
    def estado(self, valor):
      
        valor = valor.strip().lower()
        if valor not in ["disponible", "reservado", "en prestamo", "inactivo"]:
            raise ValueError("El estado debe ser 'disponible', 'reservado', 'en prestamo' o 'inactivo'.")
        self._estado = valor