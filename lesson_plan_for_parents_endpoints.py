from flask import Blueprint, render_template

lesson_plan_for_parents_blueprint = Blueprint('lesson_plan_for_parents_blueprint', __name__)


@lesson_plan_for_parents_blueprint.route('/LessonPlanForParents')
def index():
    return render_template('lesson_plan_for_parents.html')
# 1. wybierz dziecko
# 2. plan lekcji wyswietlic
# 3.obecnosc per miesiac przy kazdej nieobecnosci checkbox z mozliwoscia zaznaczenia i ponizej przycisk "usprawiedliw"
