from werkzeug.security import generate_password_hash
from app import db
from flask import jsonify, make_response
from ..models.users import Users, user_schema
from flask_jwt_extended import get_jwt_identity


def post_user(username, password):
    pass_hash = generate_password_hash(password)
    user_exist = False
    try:
        user_exist = Users.query.filter(Users.username == username).one()
    except:
        pass
    user = Users(username, pass_hash)

    if not user_exist:
        try:
            db.session.add(user)
            db.session.commit()

            return {"message": "Successfully registered"}, 201

        except:
            return jsonify({'message': 'Unable to create', 'data': {}}), 500
    return jsonify({'message': f"user {username} already exists"}), 500


def update_user(username, password):

    if username == get_jwt_identity():
        user = Users.query.filter(Users.username == username).one()

        if not user:
            return jsonify({"message": "user don't exist"})

        pass_hash = generate_password_hash(password)
        try:
            user.password = pass_hash
            db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'message': "Successfully updated", 'data': result}), 201

        except:
            return jsonify({'message': 'Unable to update', 'data': {}}), 500

    return jsonify({"message": "You don't have authorization"})


def delete_user(username):
    if username == get_jwt_identity():
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

    return jsonify({"message": "You don't have authorization"})


def user_by_username(username):
    try:
        return Users.query.filter(Users.username == username).one()

    except:
        return None





