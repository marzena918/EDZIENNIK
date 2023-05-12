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
    attendance.save(body['student_id'], body['hour'], body['subject'], body['classes'], body['date'],
                    body['inputPresent'], body['inputLate'])
    return ''
