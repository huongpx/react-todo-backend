import os

from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Resource, Api, fields, marshal, reqparse

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)
Migrate(app, db)

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, location='json')
parser.add_argument('completed', type=bool, required=True, location='json')

# model for Todo
class Todo(db.Model):
    
    __tablename__ = 'todos'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    completed = db.Column(db.Boolean)
    
    def __init__(self, title, completed):
        self.title = title
        self.completed = completed
        
    def __repr__(self):
        return f'{self.title} - {self.completed}'
    

# Marshal fields
todo_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'completed': fields.Boolean
}


# Api resource for Todo
class TodoResource(Resource):
    def get(self):
        todos = Todo.query.all()
        return [marshal(todo, todo_fields) for todo in todos]
    
    def post(self):
        args = parser.parse_args()
        new_todo = Todo(**args)
        db.session.add(new_todo)
        db.session.commit()
        return 'Create new Todo', 201
        
    
class TodoDetailResource(Resource):
    def get(self, id):
        todo = Todo.query.get_or_404(id, description='Todo not found')
        return marshal(todo, todo_fields)
    
    def put(self, id):
        todo = Todo.query.get_or_404(id, description='Todo not found')
        args = parser.parse_args()
        todo.title = args['title']
        todo.completed = args['completed']
        db.session.add(todo)
        db.session.commit()
        return 'Updated Todo'
    
    def delete(self, id):
        todo = Todo.query.get_or_404(id, description='Todo not found')
        db.session.delete(todo)
        db.session.commit()
        return 'Deleted Todo'
    

api.add_resource(TodoResource, '/todos')
api.add_resource(TodoDetailResource, '/todos/<int:id>')
