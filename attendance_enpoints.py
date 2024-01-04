from flask import Blueprint, render_template, request

from attendance import attendance

attendance_blueprint = Blueprint('attendance_blueprint', __name__)

@attendance_blueprint.route('/attendance')
def init():
    return render_template("attendance.html")

@attendance_blueprint.route('/attendance/getDayAndClasses/<day>/<classes>')
def get_sub_hour(day, classes):
    return attendance.get_sub_hour(day,classes)

@attendance_blueprint.route('/attendance/getAllHour')
def get_all_hour():
    return attendance.get_all_hour()

@attendance_blueprint.route('/attendance/saveAttendance', methods=['POST'])
def save_attendance():
    body = request.json
    print(body)
    attendance.save(body['student_id'], body['hour'], body['subject'], body['classes'], body['date'],
                    body['inputPresent'], body['inputLate'], body['inputNoPresent'])
    return ''

@attendance_blueprint.route('/attendance/upDate/', methods=['PUT'])
def update_attendance():
    body = request.json
    print(body)
    attendance.update(body)
    return ''
@attendance_blueprint.route('/attendance/listOfAllCheckbox')
def allCheckbox():
    return attendance.all_checkbox()

@attendance_blueprint.route('/attendance/summary/<int:student_id>')
def summary(student_id):
    return attendance.summary(student_id)

@attendance_blueprint.route('/attendance/getAttendanceWithDateAndStudent/<date>/<int:student_id>')
def get_attendance_with_date_and_student(student_id: int, date: str):
    return attendance.get_attendance_with_date_and_student(int(date.split("-")[0]), int(date.split("-")[1]), student_id)
