from flask import Blueprint, render_template

from lesson_plan_for_parents import lesson_plan_for_parents

lesson_plan_for_parents_blueprint = Blueprint('lesson_plan_for_parents_blueprint', __name__)


@lesson_plan_for_parents_blueprint.route('/LessonPlanForParents')
def index():
    return render_template('lesson_plan_for_parents.html')
@lesson_plan_for_parents_blueprint.route('/lessonPlanForParents/lessonPlanWithAttendance/<student_id>/<month>')
def get_attendance(student_id,month):
    return lesson_plan_for_parents.lesson_plan_with_attendance(student_id,month)
