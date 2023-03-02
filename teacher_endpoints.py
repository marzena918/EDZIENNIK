from flask import render_template, Blueprint

from teachers import teachers

teacher_blueprint = Blueprint('teacher_blueprint', __name__)

@teacher_blueprint.route('/teacher')
def index():
    return render_template('nauczyciele.html')

@teacher_blueprint.route('/teacher/get_all_subjects')
def get_all():
    return teachers.get_all()
