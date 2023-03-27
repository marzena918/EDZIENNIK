from flask import Blueprint, render_template

from marks import marks

marks_blueprint = Blueprint('marks_blueprint', __name__)

@marks_blueprint.route('/marks')
def index():
    return render_template('marks.html')
()
@marks_blueprint.route('/getAllSubjects')
def get_all_subjects():
    return marks.get_all_subjects()

@marks_blueprint.route('getAllClasses')
def getAllClasses():
    return marks.getAllClasses()