from flask import Blueprint, render_template

attendance_blueprint = Blueprint('attendance_blueprint', __name__)

@attendance_blueprint.route('/attendance')
def init():
    return render_template("attendance.html")