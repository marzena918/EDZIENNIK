from flask import render_template, Blueprint, request

from classs import classs

class_blueprint = Blueprint('class_blueprint', __name__)


@class_blueprint.route('class')
def index():
    return render_template('class.html')


@class_blueprint.route('/class/get_all')
def get_all():
    return classs.get_all()


@class_blueprint.route('/class/get_all_teacher')
def get_all_teacher():
    return classs.get_all_teacher()


@class_blueprint.route('/class/add_class', methods=['POST'])
def add_class():
    data = request.json
    classs.add_class(data['name'], data['tutor'], data['students'])
    return ''


@class_blueprint.route('/class/update', methods=['POST'])
def update():
    data = request.json
    classs.update(data['name'], data['tutor'], data['id'])
    return ''


@class_blueprint.route('/class/listStudentInThisClass/<id>')
def list_student_of_class(id):
    return classs.list_of_student_for_class(id)

@class_blueprint.route('/class/listStudentInClass')
def list_of_students_endpoint():
    return classs.list_of_students()

@class_blueprint.route('/class/studentWithoutClass')
def students_without_class():
    return classs.students_without_class()