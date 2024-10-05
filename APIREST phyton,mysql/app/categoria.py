from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# APLICACIÓN
app = Flask(__name__)
# Cadena de conexión -> mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/cursoapi?charset=utf8mb4'
# para que no salga alertas o warnings de la conexión
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#inicializar SQL alchemy e instanciarlo con esta aplicación
db = SQLAlchemy(app)
ma = Marshmallow(app)

#Crear clase entrada que tambien será nuestra tabla
class Entrada(db.Model):
     id = db.Column(db.Integer,primary_key=True)
     titulo = db.Column(db.String(100))
     mensaje = db.Column(db.String(250))
    #declara el constructor para que cada vez que se instancie la clase reciba los datos
     def __init__(self,titulo,mensaje):
         self.titulo=titulo
         self.mensaje=mensaje
        
# Crear la tabla dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# Crear un schema para que se mas sencillo acceder a los datos y estructura de la tabla
class EntradaSchema(ma.Schema):
    #aqui se declara los campos
    class Meta:
        fields = ('id','titulo','mensaje')

#Inicializar nuestro schema para una sola respuesta
entrada_schema = EntradaSchema()
#Inicializar nuestro schema para muchas respuestas
entradas_schema = EntradaSchema(many=True)

#Usar schemas con el método GET
@app.route('/entrada',methods=['GET'])
def get_entradas():
    all_entradas= Entrada.query.all()
    result = entradas_schema.dump(all_entradas)
    return jsonify(result)

#Usar el schema con parametros por el método GET
@app.route('/entrada/<id>',methods=['GET'])
def get_entrada_x_id(id):
    entrada= Entrada.query.get(id)
    result = entrada_schema.dump(entrada)
    return jsonify(result)

#Usar el schema con el método POST
@app.route('/entrada',methods=['POST'])
def insert_entrada():
    #Forzar los datos que se reciben como JSON
    # data = request.get_json(force=True)
    #Declarar campos que se van a enviar a la DB
    # titulo = data['titulo']
    # mensaje = data['mensaje']
    # Verificar el tipo de contenido de la solicitud
    if request.content_type == 'application/json':
        data = request.get_json(force=True)
        # Declarar campos que se van a enviar a la DB
        titulo = data['titulo']
        mensaje = data['mensaje']
    elif request.content_type == 'application/x-www-form-urlencoded' or request.content_type == 'multipart/form-data':
        titulo = request.form['titulo']
        mensaje = request.form['mensaje']
    else:
        return jsonify({'error': 'Unsupported Media Type'}), 415

    #La clase entrada recibe y crea el titulo y el mensaje de la nueva entrada
    nuevo_registro=Entrada(titulo,mensaje)
    #Insertar en la base de datos los nuevos registros
    db.session.add(nuevo_registro)
    db.session.commit()
    #Retornar respuesta
    return entrada_schema.jsonify(nuevo_registro)

#Usar el schema con el método PUT
@app.route('/entrada/<id>',methods=['PUT'])
def update_entrada(id):
    actualizarEntrada = Entrada.query.get(id)
    
    # Verificar el tipo de contenido de la solicitud
    if request.content_type == 'application/json':
        data = request.get_json(force=True)
        # Declarar campos que se van a enviar a la DB
        titulo = data['titulo']
        mensaje = data['mensaje']
    elif request.content_type == 'application/x-www-form-urlencoded' or request.content_type == 'multipart/form-data':
        titulo = request.form['titulo']
        mensaje = request.form['mensaje']
    else:
        return jsonify({'error': 'Unsupported Media Type'}), 415

    actualizarEntrada.titulo = titulo
    actualizarEntrada.mensaje = mensaje

    db.session.commit()

    return entrada_schema.jsonify(actualizarEntrada)

#Usar el schema con el método DELETE (No recomendado)
@app.route('/entrada/<id>',methods=['DELETE'])
def delete_entrada(id):
    eliminarEntrada = Entrada.query.get(id)
    db.session.delete(eliminarEntrada)
    db.session.commit()
    return entradas_schema.jsonify(eliminarEntrada)

# Ventana de bienvenida e inicializacion
@app.route('/',methods=['GET'])
def index():
    # retornar mensaje como un objeto
    return jsonify({'Mensaje':'Hola mundo'})
# Iniciar la aplicación
if __name__=='__main__':
    # Ejecutar
    # el debug true equivale a npm start en node
    app.run(debug=True)