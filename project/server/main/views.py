# project/server/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, request, session
import json


################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################

# game_metrics = {"rows": m,
#         "cols": n,
#         "grid": grid,
#         "covered": covered,
#         "current": True}

@main_blueprint.route('/')
def home():
    return render_template('main/home.html')

@main_blueprint.route('/buttonClick', methods=['POST'])
def buttonClick():
    return json.dumps({'value': 5})

@main_blueprint.route('/newGame', methods=['POST'])
def newGame():
    return json.dumps({'value': 5})
