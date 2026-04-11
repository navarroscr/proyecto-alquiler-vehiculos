from logica.clase_funcionario import Funcionario
import datos.funcionarios_datos as funcionarios_datos


# Crea un objeto Funcionario en diccionario
def crear_funcionario(id_funcionario, nombre, cedula, telefono, correo, puesto):
    nuevo_funcionario = Funcionario(id_funcionario, nombre, cedula, telefono, correo, puesto)

    funcionario_diccionario = {
        "id_funcionario": nuevo_funcionario.id_funcionario,
        "nombre": nuevo_funcionario.nombre,
        "cedula": nuevo_funcionario.cedula,
        "telefono": nuevo_funcionario.telefono,
        "correo": nuevo_funcionario.correo,
        "puesto": nuevo_funcionario.puesto,
        "estado": nuevo_funcionario.estado
    }

    funcionarios_datos.insertar_funcionario(funcionario_diccionario)
    print("Funcionario creado correctamente:", nombre)


# Obtiene todos los funcionarios guardados en la base de datos
def obtener_todos_los_funcionarios():
    lista = funcionarios_datos.obtener_funcionarios()
    return lista


# Busca un funcionario por su id_funcionario
def buscar_funcionario(id_funcionario):
    funcionario = funcionarios_datos.buscar_funcionario_por_id(id_funcionario)
    return funcionario


# Actualiza los datos de un funcionario según su id_funcionario
def actualizar_funcionario(id_funcionario, nuevos_datos):
    funcionarios_datos.actualizar_funcionario(id_funcionario, nuevos_datos)
    print("Funcionario actualizado correctamente")


# Elimina un funcionario según su id_funcionario
def eliminar_funcionario(id_funcionario):
    funcionarios_datos.eliminar_funcionario(id_funcionario)
    print("Funcionario eliminado correctamente")