db = db.getSiblingDB('autotrust');
db.createCollection('clientes');
db.createCollection('funcionarios');
db.createCollection('usuarios');
db.createCollection('vehiculos');
db.usuarios.insertOne({
    id_usuario: '001',
    nombre_usuario: 'admin',
    contrasena: '1234',
    tipo_usuario: 'funcionario',
    estado: 'activo'
});
print('Listo');
