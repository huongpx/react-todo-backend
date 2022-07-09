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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __init__(self, title, completed, user_id):
        self.title = title
        self.completed = completed
        self.user_id = user_id
        
    def __repr__(self):
        return f'{self.title} - {self.completed}'
    

class User(db.Model):
    """
    User model
    """

    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hashed = db.Column(db.String)
    
    def __repr__(self):
        return f'User: {self.username}'
    
    @classmethod
    def is_existed(cls, **kwargs):
        user = cls.query.filter_by(**kwargs).first()
        if user:
            return True
        return False
