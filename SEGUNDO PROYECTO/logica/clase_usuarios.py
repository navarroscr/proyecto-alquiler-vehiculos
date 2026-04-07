# Archivo: clase_usuario.py

class Usuario:
    """Clase usuarios."""

    def __init__(self, id_usuario, nombre_usuario, contrasena, tipo_usuario, estado):
        """Constructor que inicializa los atributos del usuario."""
        self._id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario  
        self.contrasena = contrasena  
        self.tipo_usuario = tipo_usuario  
        self.estado = estado 

    @property
    def id_usuario(self):
        
        return self._id_usuario

    @property
    def nombre_usuario(self):
        
        return self._nombre_usuario

    @nombre_usuario.setter
    def nombre_usuario(self, valor):
        
        if not valor.strip():
            raise ValueError("El nombre de usuario no puede estar vacío.")
        self._nombre_usuario = valor

    @property
    def contrasena(self):
       
        return self._contrasena

    @contrasena.setter
    def contrasena(self, valor):
       
        if not valor.strip():
            raise ValueError("La contraseña no puede estar vacía.")
        self._contrasena = valor

    @property
    def tipo_usuario(self):
       
        return self._tipo_usuario

    @tipo_usuario.setter
    def tipo_usuario(self, valor):
        
        valor = valor.strip().lower()  
        if valor not in ["cliente", "funcionario"]:
            raise ValueError("El tipo de usuario debe ser 'cliente' o 'funcionario'.")
        self._tipo_usuario = valor

    @property
    def estado(self):
       
        return self._estado

    @estado.setter
    def estado(self, valor):
       
        valor = valor.strip().lower() 
        if valor not in ["activo", "inactivo"]:
            raise ValueError("El estado debe ser 'activo' o 'inactivo'.")
        self._estado = valor