from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    name = db.Column(db.String(50))
    id = db.Column(db.String(4), primary_key=True)
    age = db.Column(db.Integer)
    program = db.Column(db.String(30))
    password = db.Column(db.String(30))


class Course(db.Model):
    code = db.Column(db.String(15), primary_key=True)
    credits = db.Column(db.Integer)
    name = db.Column(db.String(60))

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    course_code = db.Column(db.String(10), db.ForeignKey("course.code"))

    grade = db.Column(db.Numeric(4, 1))

    student = db.relationship("Student", backref="grades")
    course = db.relationship("Course", backref="grades")

class Staff(db.Model):
    name = db.Column(db.String(50))
    id = db.Column(db.String(4), primary_key=True)
    password = db.Column(db.String(30))


