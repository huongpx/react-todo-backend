from flask_restful import Resource, Api, fields, marshal, reqparse
from models import db
from models import Todo

from decorators import token_required

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
    @token_required
    def get(self, current_user):
        todos = Todo.query.filter_by(user_id=current_user.id).all()
        return [marshal(todo, todo_fields) for todo in todos]
    
    @token_required
    def post(self, current_user):
        args = parser.parse_args()
        args["user_id"] = current_user.id
        new_todo = Todo(**args)
        db.session.add(new_todo)
        db.session.commit()
        return marshal(new_todo, todo_fields)


class TodoDetailResource(Resource):
    """
    Todo detail resource
    """
    @token_required
    def get(self, current_user, id):
        todo = Todo.query.filter_by(id=id, user_id=current_user.id).first()
        if not todo:
            return 'Todo not found', 404
        return marshal(todo, todo_fields)
    
    @token_required
    def put(self, current_user, id):
        todo = Todo.query.filter_by(id=id, user_id=current_user.id).first()
        if not todo:
            return 'Todo not found', 404
        args = parser.parse_args()
        todo.title = args['title']
        todo.completed = args['completed']
        db.session.add(todo)
        db.session.commit()
        return marshal(todo, todo_fields)
    
    @token_required
    def delete(self, current_user, id):
        todo = Todo.query.filter_by(id=id, user_id=current_user.id).first()
        if not todo:
            return 'Todo not found', 404
        db.session.delete(todo)
        db.session.commit()
        return 'Deleted Todo'
