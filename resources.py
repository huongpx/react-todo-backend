from flask_restful import Resource, Api, fields, marshal, reqparse
from models import db
from models import Todo


parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, location='json')
parser.add_argument('completed', type=bool, required=True, location='json')


todo_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'completed': fields.Boolean
}


class TodoResource(Resource):
    """
    Todo resource
    """
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
