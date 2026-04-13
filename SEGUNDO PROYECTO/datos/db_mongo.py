from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["autotrust"]

vehiculos = db["vehiculos"]

def insertar_vehiculo(data):
    vehiculos.insert_one(data)

def obtener_vehiculos():
    return list(vehiculos.find({}, {"_id": 0}))

def actualizar_estado_vehiculo(placa, estado):
    vehiculos.update_one(
        {"placa": placa},
        {"$set": {"estado": estado}}
    )

def obtener_vehiculo_por_placa(placa):
    return vehiculos.find_one({"placa": placa}, {"_id": 0})