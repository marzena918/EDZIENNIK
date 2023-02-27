from flask import render_template

from classes import classes
from main import app

@app.route('/subject')
def get_subject():
    return render_template('oceny.html')

@app.route('/subject/get_all')
def get_all_subject():
    return classes.get_all()



