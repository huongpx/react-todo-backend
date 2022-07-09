from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    """
    Todo model
    """
    
    __tablename__ = 'todos'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    completed = db.Column(db.Boolean)
    
    def __init__(self, title, completed):
        self.title = title
        self.completed = completed
        
    def __repr__(self):
        return f'{self.title} - {self.completed}'
    

# class User(db.Model):
#     """
#     User model
#     """
    
