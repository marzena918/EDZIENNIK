import flask as flask
from flask import Flask
from flask import request, render_template

from student import Student

app = Flask(__name__)
uczniowie = Student()
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/student', methods=['POST'])
def dodaj():
    data = request.json
    uczniowie.dodaj(data['name'],data['last_name'], data['pesel'])
    return ''

@app.route('/student/<pesel>', methods=['POST'])
def is_pesel_exist(pesel):
    return '1' if uczniowie.is_pesel_exist(pesel) else '0'

@app.route('/student/<int:id>', methods=['DELETE'])
def usun(id):
    uczniowie.usun(id)
    return ''

@app.route('/student/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    uczniowie.update(data["name"],data["surname"], data["pesel"])
    return ''
@app.route('/student')
def get_all():
    return uczniowie.get_all()

app.run(port=4000)