from flask import Blueprint, render_template, request

marks_for_parents_blueprint = Blueprint('marks_for_parents_blueprint', __name__)

@marks_for_parents_blueprint.route('/marks_for_parents')
def index():
    return render_template('marksForParents.html')