from flask import Blueprint, request

from degre import degre

degre_blueprint = Blueprint('degre_blueprint', __name__)


@degre_blueprint.route('/degre/addDegre', methods=['POST'])
def add_degre():
    data = request.json
    degre.add_degre(data['id'], data['mark'],data['notes'], data['subject'])
    return ''
