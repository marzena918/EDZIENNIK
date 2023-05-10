from flask import Blueprint, render_template, request
from lesson_plan import lesson_plan

lesson_plan_blueprint = Blueprint('lesson_plan_blueprint', __name__)

@lesson_plan_blueprint.route('/lessonPlan')
def index():
    return render_template('lesson_plan.html')

@lesson_plan_blueprint.route('/lessonPlan/save/<clases>', methods=['POST'])
def save(clases):
    data = request.json
    lesson_plan.save(clases,data)
    return ''