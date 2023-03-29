from flask import Blueprint, request

from degre import degre

degre_blueprint = Blueprint('degre_blueprint', __name__)


@degre_blueprint.route('/degre/addDegre', methods=['POST'])
def add_degre():
    data = request.json
    degre.add_degre(data['studentId'], data['mark'], data['notes'], data['subject'])
    return ''


@degre_blueprint.route('/degre/degreWithThisSubjectForThisStudent/<subject>/<student_id>')
def degreWithThisSubjectForThisStudent(subject, student_id):
    return degre.findDegreForStudentWithSubject(subject, student_id)


@degre_blueprint.route('/degre/degreForDelete/<int:degre_for_delete_id>', methods=['DELETE'])
def remove_degre(degre_for_delete_id):
    degre.remove_degre(degre_for_delete_id)
    return ''
