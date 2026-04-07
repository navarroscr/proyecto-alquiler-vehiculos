# Archivo: clase_funcionario.py

class Funcionario:
    """Clase funcionarios"""

    def __init__(self, id_funcionario, nombre, cedula, telefono, correo, direccion, fecha_ingreso, estado):
        """Constructor"""
        self._id_funcionario = id_funcionario
        self.nombre = nombre  
        self.cedula = cedula  
        self.telefono = telefono  
        self.correo = correo  
        self.direccion = direccion  
        self.fecha_ingreso = fecha_ingreso  
        self.estado = estado  

    @property
    def id_funcionario(self):
     
        return self._id_funcionario

    @property
    def nombre(self):
       
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
       
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    @property
    def cedula(self):
       
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        
        if not valor.strip():
            raise ValueError("La cédula no puede estar vacía.")
        self._cedula = valor

    @property
    def telefono(self):
       
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        
        if not str(valor).isdigit():
            raise ValueError("El teléfono debe contener solo números.")
        self._telefono = valor

    @property
    def correo(self):
        
        return self._correo

    @correo.setter
    def correo(self, valor):
        
        if "@" not in valor:
            raise ValueError("El correo debe contener '@'.")
        self._correo = valor

    @property
    def direccion(self):
        
        return self._direccion

    @direccion.setter
    def direccion(self, valor):
       
        if not valor.strip():
            raise ValueError("La dirección no puede estar vacía.")
        self._direccion = valor

    @property
    def fecha_ingreso(self):
       
        return self._fecha_ingreso

    @fecha_ingreso.setter
    def fecha_ingreso(self, valor):
       
        if not valor.strip():
            raise ValueError("La fecha de ingreso no puede estar vacía.")
        self._fecha_ingreso = valor

    @property
    def estado(self):
       
        return self._estado

    @estado.setter
    def estado(self, valor):
        
        if valor.lower() not in ["activo", "inactivo"]:
         raise ValueError("El estado debe ser 'activo' o 'inactivo'.")
        self._estado = valor.lower()