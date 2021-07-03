from datetime import datetime
from app import db, ma


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'created_on')


user_schema = UsersSchema()
