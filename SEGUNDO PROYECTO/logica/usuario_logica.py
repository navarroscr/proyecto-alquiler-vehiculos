from logica.clase_usuarios import Usuario
import datos.usuarios_datos as usuarios_datos


# Crea un objeto Usuario como diccionario
def crear_usuario(id_usuario, nombre_usuario, contrasena, tipo_usuario):
    nuevo_usuario = Usuario(id_usuario, nombre_usuario, contrasena, tipo_usuario)

    usuario_diccionario = {
        "id_usuario": nuevo_usuario.id_usuario,
        "nombre_usuario": nuevo_usuario.nombre_usuario,
        "contrasena": nuevo_usuario.contrasena,
        "tipo_usuario": nuevo_usuario.tipo_usuario,
        "estado": nuevo_usuario.estado
    }

    usuarios_datos.insertar_usuario(usuario_diccionario)
    print("Usuario creado correctamente:", nombre_usuario)


# Obtiene todos los usuarios guardados en la base de datos
def obtener_todos_los_usuarios():
    lista = usuarios_datos.obtener_usuarios()
    return lista


# Busca un usuario por su id_usuario
def buscar_usuario(id_usuario):
    usuario = usuarios_datos.buscar_usuario_por_id(id_usuario)
    return usuario


# Busca un usuario por su nombre de usuario
def buscar_usuario_nombre(nombre_usuario):
    usuario = usuarios_datos.buscar_usuario_por_nombre(nombre_usuario)
    return usuario


# Actualiza los datos de un usuario según su id_usuario
def actualizar_usuario(id_usuario, nuevos_datos):
    usuarios_datos.actualizar_usuario(id_usuario, nuevos_datos)
    print("Usuario actualizado correctamente")


# Elimina un usuario según su id_usuario
def eliminar_usuario(id_usuario):
    usuarios_datos.eliminar_usuario(id_usuario)
    print("Usuario eliminado correctamente")