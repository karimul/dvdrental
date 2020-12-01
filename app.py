from flask import Flask, jsonify, json
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw' : 'Hahaha123',
    'db' : 'dvdrental',
    'host' : 'localhost',
    'port' : '5432'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)
ma = Marshmallow(app)
from models import Actor, ActorSchema




@app.route('/index', methods=['GET'])
def index():
    return 'Hello World'

@app.route('/actor', methods=['GET'])
def get_actors():
    try:
        actors = Actor.query.all()
        actors_schema = ActorSchema(many=True)
        return jsonify(data=actors_schema.dump(actors))
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

