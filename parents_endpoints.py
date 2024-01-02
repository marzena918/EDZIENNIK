from flask import Blueprint, render_template, request

from parents import parents

parents_blueprint = Blueprint('parents_blueprint', __name__)

@parents_blueprint.route('/parents')
def index():
    return render_template('parents.html')

@parents_blueprint.route('/parents/getAllParents')
def get_all_parents():
    return parents.get_all_parent()

@parents_blueprint.route('/parents/<id_parent>', methods=['DELETE'])
def delete(id_parent):
    parents.delete(id_parent)
    return ''

@parents_blueprint.route('/parents/add',  methods=['POST'])
def add():
    data = request.json
    parents.dodaj(data['name'], data['last_name'], data['pesel'])
    return ''

@parents_blueprint.route('/parents/check_pesel/<pesel>', methods=['GET'])
def is_pesel_exist(pesel):
    return '1' if parents.is_pesel_exist(pesel) else '0'

@parents_blueprint.route('/parents/update/<int:id_student>', methods=['PUT'])
def update(id_student):
    data = request.json
    parents.update(id_student, data['name'], data['last_name'], data['pesel'])
    return ''

@parents_blueprint.route('/parents/getParent/<int:id_parent>')
def get_parent(id_parent):
    return parents.get_parent(id_parent)