from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    name = db.Column(db.String(80))
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    program = db.Column(db.String(30))


