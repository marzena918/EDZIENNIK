from flask import Blueprint, render_template

import configuration_hours
from classs import classs
from degre import degre
from configuration_hours_endpoints import configuration_of_hours
from lesson_plan import lesson_plan

lesson_plan_blueprint = Blueprint('lesson_plan_blueprint', __name__)

@lesson_plan_blueprint.route('/lessonPlan')
def index():
    return render_template('lesson_plan.html')

@lesson_plan_blueprint.route('/lessonPlan/get_all_names_class')
def get_all_name_class():
    return lesson_plan.get_all()

@lesson_plan_blueprint.route('/lessonPlan/getAllTime')
def get_all_time():
    return lesson_plan.get_all_hours()
    return ''