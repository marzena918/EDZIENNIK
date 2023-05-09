from flask import Blueprint, render_template, request

from configuration_hours import configuration_of_hours

configuration_hours_blueprint = Blueprint('configuration_hours_blueprint', __name__)


@configuration_hours_blueprint.route('/configuration_hours')
def index():
    return render_template('configurationHours.html')

@configuration_hours_blueprint.route('/configuration_hours/getAllTime')
def get_all():
    return configuration_of_hours.get_all()

@configuration_hours_blueprint.route('/configurationHours/saveHours', methods=['POST'])
def saveHours():
    data = request.json
    configuration_of_hours.save_hours(data['inputFrom'], data['inputUntil'], data['lp'])
    return ''
