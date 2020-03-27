from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import models
import forms
import urllib.parse

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view-players')
def view_players():
    players = db.session.query(models.Players).all()
    return render_template('view-all-players.html', players=players)

@app.route('/view-standings')
def view_standings():
    west_standings = db.session.query(models.Teams)\
        .filter(models.Teams.conference == "West") \
        .order_by(models.Teams.w_pct.desc())\
        .all()
    east_standings = db.session.query(models.Teams) \
        .filter(models.Teams.conference == "East") \
        .order_by(models.Teams.w_pct.desc()) \
        .all()
    return render_template('view-standings.html', west_standings=west_standings, east_standings=east_standings)

@app.route('/view-team/<team_id>')
def view_teams(team_id):
    all_teams = db.session.query(models.Teams)\
        .order_by(models.Teams.nickname)\
        .all()
    team = db.session.query(models.Teams) \
        .filter(models.Teams.team_id == team_id).first()
    players_on_roster = db.session.query(models.Rosters, models.Players) \
        .filter(models.Rosters.team_id == team.team_id)\
        .filter(models.Rosters.player_id == models.Players.player_id) \
        .all()

    return render_template('view-team.html', team=team, all_teams=all_teams, players_on_roster=players_on_roster)

@app.route('/view-game')
def view_games():
    games = db.session.query(models.Games).all()
    return render_template('view-all-games.html', entries=games)

@app.route('/view-performance')
def view_performance():
    performances = db.session.query(models.Teams).all()
    return render_template('view-all-performances.html', entries=performances)

@app.route('/edit-player/<name>', methods=['GET', 'POST'])
def edit_player(name):
    player = db.session.query(models.Players)\
        .filter(models.Players.name == name).first()
    form = forms.PlayerEditFormFactory.form(player)
    if form.validate_on_submit():
        try:
            form.errors.pop('database', None)
            player.age = form.age.data
            db.session.commit()
            return redirect(url_for('view_players'))
        except BaseException as e:
            form.errors['database'] = str(e)
            return render_template('edit-player.html', player=player, form=form)
    else:
        return render_template('edit-player.html', player=player, form=form)

@app.route('/drinker/<name>')
def drinker(name):
    drinker = db.session.query(models.Drinker)\
        .filter(models.Drinker.name == name).one()
    return render_template('drinker.html', drinker=drinker)

@app.route('/serves', methods=['GET', 'POST'])
def serves():
    beers = db.session.query(models.Beer).all()
    beer_names = [beer.name for beer in beers]
    form = forms.ServingsFormFactory.form(beer_names)
    if form.validate_on_submit():
        return render_template('/servings/' + form.beer_sel.data)
    return render_template('serves.html', form=form)

@app.route('/servings/<beer_name>', methods=['GET', 'POST'])
def servings_for(beer_name):
    selected_beer = request.args.get('list_status')
    results = db.session.query(models.Serves, models.Bar) \
                .filter(models.Serves.beer == beer_name) \
                .filter(models.Serves.bar == models.Bar.name) \
                .all()
    return render_template('servings_for.html', beer_name=beer_name, data=results)

@app.route('/edit-drinker/<name>', methods=['GET', 'POST'])
def edit_drinker(name):
    drinker = db.session.query(models.Drinker)\
        .filter(models.Drinker.name == name).one()
    beers = db.session.query(models.Beer).all()
    bars = db.session.query(models.Bar).all()
    form = forms.DrinkerEditFormFactory.form(drinker, beers, bars)
    if form.validate_on_submit():
        try:
            form.errors.pop('database', None)
            models.Drinker.edit(name, form.name.data, form.address.data,
                                form.get_beers_liked(), form.get_bars_frequented())
            return redirect(url_for('drinker', name=form.name.data))
        except BaseException as e:
            form.errors['database'] = str(e)
            return render_template('edit-drinker.html', drinker=drinker, form=form)
    else:
        return render_template('edit-drinker.html', drinker=drinker, form=form)

@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
    return singular if number in (0, 1) else plural

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
