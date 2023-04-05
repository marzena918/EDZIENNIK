from flask import Blueprint, render_template, request

from configuration_hours import configuration_hours_py

configuration_hours_blueprint = Blueprint('configuration_hours_blueprint', __name__)


@configuration_hours_blueprint.route('/configuration_hours')
def index():
    return render_template('configurationHours.html')

@configuration_hours_blueprint.route('/configuration_hours/getAllTime')
def get_all():
    return configuration_hours_py.get_all()

@configuration_hours_blueprint.route('/configurationHours/saveHours', methods=['POST'])
def saveHours():
    data = request.json
    configuration_hours_py.save_hours(data['inputFrom'], data['inputUntil'], data['lp'])
    return ''
