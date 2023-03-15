from flask import Flask
from flask import request, render_template

from class_endpoints import class_blueprint
from student import Student
from student_endpoints import student_blueprint
from subject_endpoints import subject_blueprint
from teacher_endpoints import teacher_blueprint

app = Flask(__name__)


app.register_blueprint(student_blueprint, url_prefix='/')
app.register_blueprint(subject_blueprint, url_prefix='/')
app.register_blueprint(teacher_blueprint, url_prefix='/')
app.register_blueprint(class_blueprint, url_prefix='/')

app.run(port=4000)
