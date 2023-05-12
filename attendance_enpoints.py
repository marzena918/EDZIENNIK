from flask import Blueprint, render_template

from attendance import attendance

attendance_blueprint = Blueprint('attendance_blueprint', __name__)

@attendance_blueprint.route('/attendance')
def init():
    return render_template("attendance.html")

@attendance_blueprint.route('/attendance/getDayAndClasses/<day>/<classes>')
def get_sub_hour(day, classes):
    return attendance.get_sub_hour(day,classes)