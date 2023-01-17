from app import app, db
from models import User

from functools import wraps
from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request, current_app, Response

import jwt

from dotenv import load_dotenv
import os

load_dotenv()

@app.route('/register/', methods=('POST',))
def register():
    data = request.get_json()
    user = User.User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@app.route('/login/', methods=('POST',))
def login():
    data = request.get_json()
    user = User.User.authenticate(**data)

    if not user:
        return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401

    token = jwt.encode({
        'sub': user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        os.environ.get('SECRET_KEY'))
    # return jsonify({ 'token': token.decode('UTF-8') })    
    return jsonify({ 'token': token }) 

@app.route('/login/checkuser', methods=('POST',))
def checkUser():
    try:
        auth_headers = request.headers.get('Authorization', '').split()
        token = auth_headers[0]
        data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
        # print('data => ', data)
        user = User.User.query.filter_by(email=data['sub']).first()
        # print('USER EMAIL => ', user.email)
        if user.email == 'kcs.kanan@gmail.com':
            return jsonify(True)
        return jsonify(False)

    except Exception as e:
        # print('ERROR => ', e)
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, os.environ.get('SECRET_KEY'))
            user = User.User.query.filter_by(email=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify