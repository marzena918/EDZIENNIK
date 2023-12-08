from flask import Blueprint, render_template


lesson_plan_for_parents_blueprint = Blueprint('lesson_plan_for_parents_blueprint', __name__)

@lesson_plan_for_parents_blueprint.route('/lessonPlanForParents')
def index():
    return render_template('lesson_plan_for_parents.html')