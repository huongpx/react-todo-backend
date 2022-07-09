import uuid
from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash

from models import db, User

auth_user = Blueprint('auth_user', __name__)

@auth_user.route('/api/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    email = data['email']
    if User.is_existed(username=username):
        return jsonify({'message': 'username already exists'})
    if User.is_existed(email=email):
        return jsonify({'message': 'email already exists'})
    
    password_hashed = generate_password_hash(data['password'])
    
    new_user = User(public_id=str(uuid.uuid4()), 
                    username=username, email=email, 
                    password_hashed=password_hashed)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': f'Registration successful with username "{username}"'})
