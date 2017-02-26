# project/server/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, request
import json


################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################


@main_blueprint.route('/')
def home():
    return render_template('main/home.html')

@main_blueprint.route('/buttonClick', methods=['POST'])
def buttonClick():
    print(request.form)
    return json.dumps({'value': 5})
