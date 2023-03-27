from flask import Blueprint, render_template

marks_blueprint = Blueprint('student_blueprint', __name__)

@marks_blueprint.route('/marks')
def index():
    return render_template('mark.html')