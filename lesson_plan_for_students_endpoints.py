from flask import Blueprint, render_template
lesson_plan_for_students_blueprint = Blueprint('lesson_plan_for_students_blueprint', __name__)


@lesson_plan_for_students_blueprint.route('/LessonPlanForStudents')
def index():
    return render_template('lessonPlanForStudent.html')