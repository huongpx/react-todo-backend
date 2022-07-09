from crypt import methods
import datetime
import json
import uuid
from flask import Blueprint, current_app, jsonify, make_response, request
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

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


@auth_user.route('/api/auth/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'Authentication': 'Login required'})
    
    user = User.query.filter_by(username=auth.username).first()
    if check_password_hash(user.password_hashed, auth.password):
        token = jwt.encode(payload={'public_id': user.public_id,
                                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
                           key=current_app.config['SECRET_KEY'],
                           algorithm="HS256")
        
        return jsonify({'token': token})
    
    return make_response('Could not verify', 401, {'Authentication': 'Login required'})
