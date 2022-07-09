from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from models import db
from resources import TodoResource, TodoDetailResource

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
Migrate(app, db)
api = Api(app)

api.add_resource(TodoResource, '/todos')
api.add_resource(TodoDetailResource, '/todos/<int:id>')
