from app import app
from models import db, Student

students = [
    Student(name="Nolan", id=2222, age=23, program="Engineering"),
    Student(name="Anne", id=3845, age=19, program="Finance"),
    Student(name="Morgan", id=9654, age=22, program="Economics"),
]

with app.app_context():
    Student.query.delete()
    db.session.add_all(students)
    db.session.commit()

print("Students added!")