from flask import Flask, render_template, request, url_for, redirect, session, flash
from school_data import find_id, verify_staff, course_list, verify_student, sch, find_course
from announcements import dates

app = Flask(__name__)

app.secret_key = "secret-key"

@app.route("/")
def home():
    return render_template("index.html")

#check if webpage is running
@app.route("/ping")
def ping():
    return "pong"

@app.route("/student", methods=["POST", "GET"])
def submit():
    #print("1")
    if request.method == "POST":
        #print("2")
        student_id = request.form.get("student-id")
        student_pass = request.form.get("student-pass")
        student = find_id(student_id)
        #check if id or password is wrong
        if not student or not verify_student(student, student_pass):
            flash("Invalid ID or password", "error")
            return redirect(url_for("home"))
        avg_grades = student.avg_grades()
        session["id"] = student_id
        return render_template("result.html", s_data=student, grades=avg_grades, courses=course_list)
    
    #print("4")
    stud = find_id(session['id'])
    avg_grades = stud.avg_grades()
    # print(stud.grades)
    # print(session["data"])
    return render_template("result.html", s_data=stud, grades=avg_grades, courses=course_list)




@app.route("/course", methods=["POST"])
def add_course():
    course_code = request.form.get("course-code")
    choice = request.form.get("sub-button")
    #print(choice)
    st_id = session["id"]
    st = find_id(st_id)
    print(st.course_data)
    if choice == "add":
        success = st.enroll_class(course_code)
    elif choice == "delete":
        success = st.drop_class(course_code)
    if not success:
        flash("Unknown course code", "error")
    elif success == 1:
        pass
    elif success == 2:
        flash("Reached maximum course limit", "error")
    print(st.course_data)

    return redirect(url_for("submit"))

@app.route("/staff", methods=["POST", "GET"])
def staff_page():
    staff_id = request.form.get("staff-id")
    staff_password = request.form.get("staff-pass")
    staff = verify_staff(staff_id, staff_password)
    if not staff:
        flash("Invalid ID or password", "error")
        return render_template("index.html")
    session["staff_name"] = staff.name
    return render_template("staff.html", name=staff.name, id=staff.id, school=sch)


#delete this when ready
@app.route("/staff/<course_code>/students")
def view_students(course_code):
    course = find_course(course_code)
    students = course.students

    return { "students": [ {'name': s.name, "id": s.id} for s in students] }

@app.route("/staff/course-list")
def view_course_list():
    return render_template("staff_course_list.html", school=sch, name=session["staff_name"])

@app.route("/staff/student-list")
def view_student_list():
    return render_template("staff_student_list.html", school=sch, name=session["staff_name"])

@app.route("/staff/enter-grades")
def enter_grades():
    return render_template("staff_enter_grades.html", school=sch, name=session["staff_name"] )




if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)