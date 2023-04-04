from flask import Flask

from class_endpoints import class_blueprint
from configuration_hours_endpoints import configuration_hours_blueprint
from degre_endpoints import degre_blueprint
from mark_endopoints import marks_blueprint
from student_endpoints import student_blueprint
from subject_endpoints import subject_blueprint
from teacher_endpoints import teacher_blueprint

app = Flask(__name__)


app.register_blueprint(student_blueprint, url_prefix='/')
app.register_blueprint(subject_blueprint, url_prefix='/')
app.register_blueprint(teacher_blueprint, url_prefix='/')
app.register_blueprint(class_blueprint, url_prefix='/')
app.register_blueprint(marks_blueprint, url_prefix='/')
app.register_blueprint(degre_blueprint, url_prefix='/')
app.register_blueprint(configuration_hours_blueprint, url_prefix='/')

app.run(port=4000)
