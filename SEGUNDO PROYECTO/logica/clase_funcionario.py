class Funcionario:

    # Constructor 
    def __init__(self, id_funcionario, nombre, cedula, telefono, correo, puesto, estado="activo"):
        self.id_funcionario = id_funcionario
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo
        self.puesto = puesto
        self.estado = estado

    
    @property
    def id_funcionario(self):
        return self._id_funcionario

    @id_funcionario.setter
    def id_funcionario(self, valor):
        if valor == "" or valor is None:
            print("Error: el id del funcionario no puede estar vacío")
        else:
            self._id_funcionario = valor

   
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor == "" or valor is None:
            print("Error: el nombre no puede estar vacío")
        else:
            self._nombre = valor

    
    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        if valor == "" or valor is None:
            print("Error: la cédula no puede estar vacía")
        else:
            self._cedula = valor

    
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if valor == "" or valor is None:
            print("Error: el teléfono no puede estar vacío")
        else:
            self._telefono = valor

    
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if valor == "" or valor is None:
            print("Error: el correo no puede estar vacío")
        else:
            self._correo = valor

  
    @property
    def puesto(self):
        return self._puesto

    @puesto.setter
    def puesto(self, valor):
        if valor == "" or valor is None:
            print("Error: el puesto no puede estar vacío")
        else:
            self._puesto = valor

  
    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        estados_validos = ["activo", "inactivo"]
        if valor not in estados_validos:
            print("Error: el estado solo puede ser 'activo' o 'inactivo'")
        else:
            self._estado = valor