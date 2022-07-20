"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db,Users,Personajes,Planetas,FavoritosPj,FavoritosPl
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_users():
    usuarios= Users.query.all()

    lista_usuarios= list(map(lambda Us: Us.serialize(),usuarios))   

    return jsonify(lista_usuarios), 200

@app.route("/people" , methods=["GET"])
def get_personajes():
    personajes = Personajes.query.all()

    lista_personajes = List(map(lambda Pjs: Pjs.serialize().personajes))

    return jsonify (lista_personajes), 200

@app.route("/people/<int:people_id>", methods=["GET"])
def get_personajes_id():
    personajes_id=Personajes.query.all(id)

    pjs=personajes_id.serilize()

    return jsonify(pjs), 200

@app.route('/planets', methods=['GET'])
def get_planetas():
    planetas= Planetas.query.all()

    lista_planetas = list(map(lambda Pla:Pla.serialize(),planetas))

    return jsonify(lista_planetas), 200

@app.route("/planets/<int:planet_id>", methods=["GET"])
def get_planetas_id(id):
    planetas_id = Planetas.query.all(id)

    lista_planetas_id = planetas_id.serialize()

    return jsonify(lista_planetas_id), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
