from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

from models import db
from resources import TodoResource, TodoDetailResource
from auth import auth_user

app = Flask(__name__)
CORS(app)
app.config.from_object('config')

db.init_app(app)
Migrate(app, db)
api = Api(app)

app.register_blueprint(auth_user)

api.add_resource(TodoResource, '/api/todos')
api.add_resource(TodoDetailResource, '/api/todos/<int:id>')
