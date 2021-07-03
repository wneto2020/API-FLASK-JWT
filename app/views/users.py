from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema


def post_user():
    username = request.json['username']
    password = request.json['password']
    pass_hash = generate_password_hash(password)
    user = Users(username, pass_hash)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': "Successfully registered", 'data': result}), 201

    except:
        return jsonify({'message': 'Unable to create', 'data': {}}), 500


def update_user():
    username = request.json['username']
    password = request.json['password']
    user = Users.query.filter(Users.username == username).one()

    if not user:
        return jsonify({"message": "user don't exist"})

    pass_hash = generate_password_hash(password)
    try:
        user.username = username
        user.password = pass_hash
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': "Successfully updated", 'data': result}), 201

    except:
        return jsonify({'message': 'Unable to update', 'data': {}}), 500


def get_user(username):
    user = Users.query.filter(Users.username == username).one()

    if user:
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully request', 'data': result}), 201

    return jsonify({'message': 'Unable to request', 'data': {}}), 500


def delete_user():
    username = request.json['username']

    user = Users.query.filter(Users.username == username).one()
    if not user:
        return jsonify({'message': "User don't exist", 'data': {}}), 500

    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'message': 'successfully request', 'data': result}), 201

        except:
            return jsonify({'message': 'Unable to request', 'data': {}}), 500


def user_by_username(username):
    try:
        return Users.query.filter(Users.username == username).one()

    except:
        return None





