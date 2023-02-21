import flask as flask
from flask import Flask
from flask import request, render_template

from student import Student

app = Flask(__name__)
uczniowie = Student()
@app.route('/')
def index():
    return render_template('index.html')

#
# @app.route('/listaUczniow', methods='POST')
# def dodaj():
#     data = request
#     uczniowie.dodaj(data['name'],data['surname'], data['pesel'])
#     return ''
#
#
# @app.route('/listaUczniow/<int:id>', methods='DELETE')
# def usun(id):
#     uczniowie.usun(id)
#     return ''
#
# @app.route('/listaUczniow/<int:id>', methods='PUT')
# def update(id):
#     data = request
#     uczniowie.update(data["name"],data["surname"], data["pesel"])
#     return ''
@app.route('/student')
def get_all():
    return uczniowie.get_all()

app.run(port=4000)