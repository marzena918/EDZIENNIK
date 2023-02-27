from flask import Blueprint, request, render_template

from student import Student

student_blueprint = Blueprint('student_blueprint', __name__)

uczniowie = Student()

@student_blueprint.route('/student/oceny/<id>')
def oceny(id):
    return uczniowie.get_all_grades(id)
# @student_blueprint.route('/student/oceny')
# def index():
#     return render_template('studen-oceny.html')

@student_blueprint.route('/student/daneStudenta/<id>')
def student_data(id):
    return uczniowie.student_data(id)

@student_blueprint.route('/student')
def index():
    return render_template('index.html')


@student_blueprint.route('/student', methods=['POST'])
def dodaj():
    data = request.json
    uczniowie.dodaj(data['name'], data['last_name'], data['pesel'])
    return ''


@student_blueprint.route('/student/check_pesel/<pesel>', methods=['GET'])
def is_pesel_exist(pesel):
    return '1' if uczniowie.is_pesel_exist(pesel) else '0'


@student_blueprint.route('/student/<int:id_student_for_delete>', methods=['DELETE'])
def usun(id_student_for_delete):
    uczniowie.usun(id_student_for_delete)
    return ''


@student_blueprint.route('/student/<int:id_student>', methods=['PUT'])
def update(id_student):
    data = request.json
    uczniowie.update(id_student,data['name'], data['last_name'], data['pesel'])
    return ''


@student_blueprint.route('/student/all')
def get_all():
    return uczniowie.get_all()