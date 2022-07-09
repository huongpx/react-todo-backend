from functools import wraps

from flask import request, jsonify, current_app
import jwt

from models import User


def token_required(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            
        if not token:
            return jsonify({'message': 'Missing token'})
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except Exception as e:
            return jsonify({'message': 'token not valid'})
        
        return fn(*args, current_user, **kwargs)
    
    return decorator
