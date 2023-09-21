from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    first_name = db.Column(db.String(80), primary_key=True)
    second_name = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String, nullable=False)
