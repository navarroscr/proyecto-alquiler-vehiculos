from pymongo import MongoClient

def obtener_base_datos():
    """conectamos a MongoDB se devuelve la base de datos del proyecto"""
    cliente = MongoClient("mongodb://localhost:27017/")
    base_datos = cliente["autotrust"]
    return base_datos

#prueba de conexion a base de datos 
if __name__ == "__main__":
    db = obtener_base_datos()
    print("Conexión exitosa a MongoDB")
    print("Base de datos:", db.name)