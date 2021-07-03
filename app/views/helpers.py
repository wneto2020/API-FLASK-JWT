from app import app
from werkzeug.security import check_password_hash
from flask import jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from ..views.users import user_by_username
from datetime import datetime, timedelta

jwt = JWTManager(app)


def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "Could not verify"}), 401

    user = user_by_username(auth.username)
    if not user:
        return jsonify({"message": "User not found", "data": {}}), 401

    if user and check_password_hash(user.password, auth.password):
        token = create_access_token(identity=user.username, expires_delta=timedelta(minutes=20))

        return jsonify({"message": "Authentication Successfully", "token": token,
                        "exp": datetime.now() + timedelta(minutes=20)})

    return jsonify({"message": "Could not verify"}), 401