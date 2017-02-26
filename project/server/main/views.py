# project/server/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, request, session, redirect
import json
from project.server.main.minesweeper import new_game


################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################

# game = {"rows": m,
#         "cols": n,
#         "grid": grid,
#         "covered": covered,
#         }

@main_blueprint.route('/')
def home():
    if 'grid' not in session:
        #TODO: encrypt session so not readable
        game = new_game(8,8,10)
        session.update(game)

    return render_template('main/home.html', 
            rows=session["rows"],
            cols=session["cols"],
            grid=session["grid"],
            covered=session["covered"])
    #TODO: pass kwargs as **session to get fancy

@main_blueprint.route('/buttonClick', methods=['POST'])
def buttonClick():
    id_btn = int(request.form['id'])
    grid = session['grid']
    covered = session['covered'].copy()
    covered[id_btn] = 0
    session['covered'] = covered
    return json.dumps({'value': grid[id_btn]})

@main_blueprint.route('/newGame', methods=['POST'])
def newGame():
    m = int(request.form.get("rows-input", 8))
    n = int(request.form.get("cols-input", 8))
    k = int(request.form.get("mines-input", 10))
    #TODO: Validate input (currenly validated on client only)

    game = new_game(m, n, k)
    session.update(game)
    return redirect('/')
