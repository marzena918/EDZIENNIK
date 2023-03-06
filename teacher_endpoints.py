from flask import render_template, Blueprint, request

from teachers import teachers

teacher_blueprint = Blueprint('teacher_blueprint', __name__)

@teacher_blueprint.route('/teacher')
def index():
    return render_template('nauczyciele.html')

@teacher_blueprint.route('/teacher/get_all_subjects')
def get_all():
    return teachers.get_all()

@teacher_blueprint.route('/teacher/check_pesel/<pesel>')
def check_pesel(pesel):
    return '1' if teachers.is_pesel_exist(pesel) else '0'

@teacher_blueprint.route('/teacher/add', methods= ['POST'])
def add():
    data = request.json
    teachers.add_teacher(data['name'], data['last_name'], data['pesel'], data['subjects'])
    return ''

@teacher_blueprint.route('/teacher/get_all_teacher')
def get_all_teachers():
    return teachers.get_all_teacher()

@teacher_blueprint.route('/teacher/subjectsOfTeacher/<id>')
def subjects_of_teacher(id):
    return teachers.subjects_of_teacher(id)

@teacher_blueprint.route('/teacher/delete_subject_for_teacher/<id>/<subject>', methods=['DELETE'])
def delete_subject_for_teacher(id,subject):
    teachers.delete_subject_for_teacher(id,subject)
    return ''