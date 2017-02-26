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
#         "current": t/f
#         }

@main_blueprint.route('/')
def home():
    if 'current' not in session:
        #TODO: encrypt session so not readable
        game = new_game(8,8,10)
        session.update(game)

    return render_template('main/home.html', **session)

@main_blueprint.route('/buttonClick', methods=['POST'])
def buttonClick():
    if session.get("current", False):
        id_btn = int(request.form['id'])
        grid = session['grid']

        # Uncover button
        covered = session['covered'].copy()
        covered[id_btn] = 0
        session['covered'] = covered
        #TODO: the above is super safe. maybe unnecessary to copy

        print(grid[id_btn])

        if grid[id_btn] == '*':
            session['current'] = False

        return json.dumps({'value': grid[id_btn]})
    return '{}'

@main_blueprint.route('/newGame', methods=['POST'])
def newGame():
    m = int(request.form.get("rows-input", 8))
    n = int(request.form.get("cols-input", 8))
    k = int(request.form.get("mines-input", 10))
    #TODO: Validate input (currenly validated on client only)

    game = new_game(m, n, k)
    session.update(game)
    return redirect('/')
