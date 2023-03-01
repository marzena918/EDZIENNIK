from flask import render_template, Blueprint

subject_blueprint = Blueprint('subject_blueprint', __name__)
from classes import classes


@subject_blueprint.route('/subject')
def index():
    return render_template('subjects.html')

@subject_blueprint.route('/subject/add/<subject>', methods=['POST'])
def add(subject):
    classes.add(subject)
    return ""

@subject_blueprint.route('/subject/get_all')
def get_all():
    return classes.get_all()

@subject_blueprint.route('/subject/remove/<subject>', methods=['DELETE'])
def remove(subject):
    classes.remove(subject)
    return ''
# @app.route('/subject')
# def get_subject():
#     return render_template('nauczyciele.html')
#
# @app.route('/subject/get_all')
# def get_all_subject():
#     return classes.get_all()
