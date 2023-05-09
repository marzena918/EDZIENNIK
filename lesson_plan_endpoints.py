from flask import Blueprint, render_template

lesson_plan_blueprint = Blueprint('lesson_plan_blueprint', __name__)

@lesson_plan_blueprint.route('/lessonPlan')
def index():
    return render_template('lesson_plan.html')