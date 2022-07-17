from functools import wraps

from flask import request, jsonify, current_app
import jwt

from models import User


def token_required(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        auth_token = None
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
            
        if not auth_token:
            return {'error': 'Missing token'}, 401
        try:
            data = jwt.decode(auth_token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except Exception as e:
            return {'error': 'token not valid'}, 401
        
        return fn(*args, current_user, **kwargs)
    
    return decorator
