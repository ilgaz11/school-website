from app import app
from models import db, Student, Course, Grade, Staff


students = [
    Student(name="Jack Mooney", id="1234", age=19, program="Engineering", password="test"),
    Student(name="Sally Coleman", id="2349", age=20, program="Engineering", password="test"),
    Student(name="Bob Robertson", id="9999", age=18, program="Commerce", password="test"),
    Student(name="Don Rosales", id="3465", age=21, program="Engineering", password="test"),
    Student(name="Laura Spencer", id="8918", age=19, program="Medicine", password="test"),
    Student(name="Javier Pineda", id="3432", age=22, program="Commerce", password="test"),
    Student(name="Sarah Riggs", id="8700", age=18, program="Business", password="test"),
    Student(name="Jodi Waters", id="7654", age=21, program="Humanities", password="test"),
    Student(name="Paul Yu", id="3331", age=18, program="Engineering", password="test"),
    Student(name="Daniel Ferguson", id="0987", age=23, program="Business", password="test"),
    Student(name="Amy Lau", id="6790", age=20, program="Science", password="test"),
    Student(name="George Benton", id="9901", age=18, program="Medicine", password="test"),
    Student(name="Maria Jimenez", id="1267", age=22, program="Science", password="test"),
    Student(name="Ruth Mclaughlin", id="3210", age=18, program="Business", password="test"),
    Student(name="Marty Byrde", id="8888", age=23, program="Commerce", password="test"),
    Student(name="Eve Lyons", id="1002", age=20, program="Engineering", password="test"),
    Student(name="Adam Forster", id="0001", age=20, program="Economics", password="test"),
    Student(name="Patrick Star", id="9201", age=24, program="Science", password="test"),
    Student(name="Sandy Burton", id="8121", age=18, program="Business", password="test"),
    Student(name="Jon Winters", id="2718", age=21, program="Economics", password="test"),
    Student(name="Nolan Dark", id="2222", age=23, program="Engineering", password="test"),
    Student(name="Anne Hathens", id="3845", age=19, program="Finance", password="test"),
    Student(name="Morgan Arthur", id="9654", age=22, program="Economics", password="test"),
]

courses = [
    Course(code="COMP-202", credits=3, name="Foundations of Programming"),
    Course(code="COMP-206", credits=3, name="Introduction to Software Systems"),
    Course(code="COMP-230", credits=3, name="Logic and Computability"),
    Course(code="COMP-310", credits=4, name="Operating Systems"),
    Course(code="ECON-208", credits=3, name="Microeconomic Analysis and Applications"),
    Course(code="ECON-308", credits=3, name="Governmental Policy Towards Business"),
    Course(code="ECSE-200", credits=3, name="Electric Circuits 1"),
    Course(code="ECSE-205", credits=3, name="Probability and Statistics for Engineers"),
    Course(code="ECSE-206", credits=3, name="Introduction to Signals and Systems"),
    Course(code="ECSE-210", credits=3, name="Electric Circuits 2"),
    Course(code="ECSE-211", credits=3, name="Design Principles and Methods"),
    Course(code="ECSE-222", credits=3, name="Digital Logic"),
    Course(code="ECSE-223", credits=3, name="Model-Based Programming"),
    Course(code="ECSE-250", credits=3, name="Fundamentals of Software Development"),
    Course(code="ECSE-324", credits=4, name="Computer Organization"),
    Course(code="FACC-100", credits=1, name="Introduction to the Engineering Profession"),
    Course(code="MATH-240", credits=3, name="Discrete Structures"),
    Course(code="MATH-262", credits=3, name="Intermediate Calculus"),
    Course(code="MATH-263", credits=3, name="Ordinary Differential Equations for Engineers"),
]

grades = [
    Grade(student_id="1234", course_code="MATH-262", grade=82.5),
    Grade(student_id="1234", course_code="MATH-263", grade=77.0),
    Grade(student_id="3465", course_code="MATH-262", grade=92.1),
    Grade(student_id="3465", course_code="MATH-263", grade=88.0),
    Grade(student_id="9999", course_code="MATH-240", grade=66.7),
    Grade(student_id="1234", course_code="MATH-263", grade=74.8)

]

staff = [
    Staff(name="Ilgaz", id="0011", password="hello"),
    Staff(name="Gustavious", id="1001", password="third"),
    Staff(name="John Doe", id="4321", password="none")
]

with app.app_context():
    Student.query.delete()
    Staff.query.delete()
    Course.query.delete()
    Grade.query.delete()
    db.session.add_all(students)
    db.session.add_all(courses)
    db.session.add_all(grades)
    db.session.add_all(staff)
    db.session.commit()

print("Students added!")
print("Courses added!")