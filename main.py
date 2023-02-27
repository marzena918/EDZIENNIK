from flask import Flask
from flask import request, render_template

from student import Student
from student_endpoints import student_blueprint

app = Flask(__name__)


app.register_blueprint(student_blueprint, url_prefix='/')
app.run(port=4000)
