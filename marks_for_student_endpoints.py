from flask import Blueprint, render_template, request

marks_for_students_blueprint = Blueprint('marks_for_students_blueprint', __name__)

@marks_for_students_blueprint.route('/marksForStudents')
def index():
    return render_template('marksForStudent.html')