from flask import Blueprint, render_template

from parents import parents

parents_blueprint = Blueprint('parents_blueprint', __name__)

@parents_blueprint.route('/parents')
def index():
    return render_template('parents.html')

@parents_blueprint.route('/parents/getAllParents')
def get_all_parents():
    return parents.get_all_parent()