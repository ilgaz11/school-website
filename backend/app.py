from flask import Flask, render_template, request, url_for, redirect, session, flash
from school_data import find_id, verify_staff, course_list, verify_student, sch, find_course
from announcements import dates
from flask_sqlalchemy import SQLAlchemy
from models import db, Student, Course, Staff, Grade
import os

#create flask app
app = Flask(__name__, template_folder="../templates", static_folder="../static")

#secret key flash messages
app.secret_key = "secret-key"

# --------------
#set database uri and initialize
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, "school.db")
db.init_app(app)

os.makedirs(app.instance_path, exist_ok=True)

with app.app_context():
    db.create_all()
    # students = Student.query.all()
# --------------


#main route
@app.route("/")
def home():
    return render_template("index.html", dates=dates)

#check if webpage is running
@app.route("/ping")
def ping():
    return "pong"

#student page
@app.route("/student", methods=["POST", "GET"])
def submit():

    if request.method == "POST":
        #get from requests of id and password
        student_id = request.form.get("student-id")
        student_pass = request.form.get("student-pass")
        #get student from database
        student = Student.query.filter_by(id=student_id).first()
        # print(student.name)
        #check if id or password is wrong
        if not student or (student.password != student_pass):
            flash("Invalid ID or password", "error")
            return redirect(url_for("home"))
        #create session id
        session["id"] = student_id
        return render_template("result.html", s_data=student, grades=student.grades, courses=course_list)
    
    #print("4")
    stud = Student.query.get(session["id"])
    # avg_grades = stud.avg_grades()
    # print(stud.grades)
    # print(session["data"])
    return render_template("result.html", s_data=stud, grades=stud.grades, courses=course_list)



#add course action
@app.route("/course", methods=["POST"])
def add_course():
    #get inputted course code and add/drop choice
    course_code = request.form.get("course-code")
    choice = request.form.get("sub-button")
    st_id = session["id"]
    #check student's current amount of enrolled courses
    count = Grade.query.filter_by(student_id=st_id).count()
    #flash error if too many courses or course does not exist

    course = Course.query.get(course_code)
    if not course:
        flash("Unknown course code", "error")
        return redirect(url_for("submit"))
    #check if student is already enrolled
    already_enrolled = Grade.query.filter_by(student_id=st_id, course_code=course.code).first()
    print(already_enrolled)
    if choice == "add":
        if count >= 7:
            flash("Reached maximum course limit", "error")
            return redirect(url_for("submit"))
        if already_enrolled:
            flash(f"Already enrolled to {course.code}", "error")
        #if not, then add now row to database
        else:
            new_grade = Grade(student_id=st_id, course_code=course.code, grade=-1)
            db.session.add(new_grade)
            db.session.commit()
            
    #if user chooses to drop a course, delete the row from database
    elif choice == "delete":
        if not already_enrolled:
            flash(f"Not enrolled to {course.code}", "error")
        else:
            #already enrolled contains the grade if it exists, so just delete it
            db.session.delete(already_enrolled)
            db.session.commit()

    
    return redirect(url_for("submit"))

#staff page
@app.route("/staff", methods=["POST", "GET"])
def staff_page():
    staff_id = request.form.get("staff-id").strip()
    staff_password = request.form.get("staff-pass")
    staff = Staff.query.filter_by(id=staff_id).first()
    # staff = verify_staff(staff_id, staff_password)
    print(Staff.query.all())
    print(type(staff_password)) 
    print(type(staff_id))
    print(staff)
    if not staff or staff.password != staff_password.strip():
        flash("Invalid ID or password", "error")
        return redirect(url_for("home"))
    session["staff_name"] = staff.name
    return render_template("staff.html", name=staff.name, id=staff.id, school=sch)


#delete this when ready
@app.route("/staff/<course_code>/students")
def view_students(course_code):
    course = find_course(course_code)
    students = course.students

    return { "students": [ {'name': s.name, "id": s.id} for s in students] }

#course list in staff page
@app.route("/staff/course-list")
def view_course_list():
    return render_template("staff_course_list.html", school=sch, name=session["staff_name"])

#student list in staff page
@app.route("/staff/student-list")
def view_student_list():
    return render_template("staff_student_list.html", school=sch, name=session["staff_name"])

#grade enter page in staff page
@app.route("/staff/enter-grades")
def enter_grades():
    student_id = request.args.get("id")

    student = find_id(student_id)
    avg_grades=None
    if student:
        avg_grades = student.avg_grades()
        session["chosen_student_id"] = student.id
    

    return render_template("staff_enter_grades.html", school=sch, name=session["staff_name"], stud=student, grades=avg_grades)

#enter grades action
@app.route("/add-new-grades", methods=["POST", "GET"])
def add_new_grades():
    #check if new grade is valid
    try:
        added_grade = int(request.form.get("new-grade"))
    except ValueError:
        added_grade = None
    course_code = request.form.get("course-code")
    student = find_id(session["chosen_student_id"])
    #only add new grade if it is a valid integer
    if added_grade:
        student.enter_grade(course_code, added_grade)
    avg_grades=student.avg_grades()
    print(added_grade, course_code)
    return render_template("staff_enter_grades.html", school=sch, name=session["staff_name"], stud=student, grades=avg_grades)





if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
    pass