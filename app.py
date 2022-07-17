from flask import Blueprint, Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

from models import db
from resources import TodoResource, TodoDetailResource
from auth import auth_user

app = Flask(__name__)
app.config.from_object('config')
cors = CORS(app, supports_credentials=True)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

db.init_app(app)
Migrate(app, db)

api.add_resource(TodoResource, '/api/todos/')
api.add_resource(TodoDetailResource, '/api/todos/<int:id>')

app.register_blueprint(auth_user)
app.register_blueprint(api_bp)
