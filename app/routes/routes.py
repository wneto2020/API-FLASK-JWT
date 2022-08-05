from app import app
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..views import users, helpers


@app.route("/", methods=["GET"])
@jwt_required()
def hello():
    return jsonify({"message": f"Hello {get_jwt_identity()}"})


@app.route('/users', methods=['POST'])
def post_user():
    return users.post_user(request.json['username'], request.json['password'])


@app.route('/users', methods=['PUT'])
@jwt_required()
def update_user():
    return users.update_user(request.json['username'], request.json['password'])


@app.route('/users', methods=['DELETE'])
@jwt_required()
def delete_user():
    return users.delete_user(request.json['username'])


@app.route('/auth', methods=['POST'])
def authenticate():
    return helpers.auth()
