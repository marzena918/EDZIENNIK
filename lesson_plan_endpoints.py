from flask import Blueprint, render_template

from classs import classs

lesson_plan_blueprint = Blueprint('lesson_plan_blueprint', __name__)

@lesson_plan_blueprint.route('/lessonPlan')
def index():
    return render_template('lesson_plan.html')

@lesson_plan_blueprint.route('/get_all_names_class')
def get_all_name_class():
    return classs.get_all()
