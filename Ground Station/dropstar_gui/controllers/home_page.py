import datetime

from flask import render_template

info = {  # FIXME: This info needs to be updated
    'team_name': 'Info',
    # 'team_members': ['Maria', 'Iraklis', 'Alex', 'Kostas', 'Eirini', 'Konstantina', 'Dimitris', 'Chrysa', 'Jimmys', 'Elli', 'Apostolis', 'Vasw', 'Georgia', 'Tasos', 'Giwrgos'],
    'project_desc': 'This is a project for the REXUS/BEXUS Cycle 14 programme. ' +
                    'It aims to study the effects of microgravity conditions on the coalescence events of an oil to water emulsion. ',
    'current_stage': 'The project is currently on the integration phase. ',
    # FIXME: This needs to be updated in real time (perhaps do it in JS)
    'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}


def render():
    return render_template('base.j2', info=info)
