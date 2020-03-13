from app import db
from sqlalchemy import orm


class Players(db.Model):
    __tablename__ = 'Player'
    name = db.Column('player_name', db.String(100))
    team_id = db.Column('team_id', db.Integer, primary_key=True)
    player_id = db.Column('player_id', db.Integer, primary_key=True)
    season = db.Column('season', db.Integer, primary_key=True)
    age = db.Column('age', db.Integer)
    position = db.Column('position', db.String(1))

class Standings(db.Model):
    __tablename__ = 'Standings'
    team_id = db.Column('team_id', db.Integer, primary_key=True)
    league_id = db.Column('league_id', db.Integer, primary_key=True)
    season_id = db.Column('season_id', db.Integer, primary_key=True)
    standings_date = db.Column('standingsdate', db.Date, primary_key=True)
    conference = db.Column('conference', db.String(4))
    team = db.Column('team', db.String(30))
    gp = db.Column('gp', db.Integer)
    w = db.Column('w', db.Integer)
    l = db.Column('l', db.Integer)
    w_pct = db.Column('w_pct', db.Numeric(4, 3))
    home_record = db.Column('home_record', db.String(15))
    away_record = db.Column('away_record', db.String(15))

class Teams(db.Model):
    __tablename__ = 'Teams'
    team_id = db.Column('team_id', db.Integer, primary_key=True)
    league_id = db.Column('league_id', db.Integer, primary_key=True)
    min_year = db.Column('min_year', db.Integer)
    max_year = db.Column('max_year', db.Integer)
    abbreviation = db.Column('abbreviation', db.String(3))
    nickname = db.Column('nickname', db.String(50))
    year_founded = db.Column('year_founded', db.Integer)
    city = db.Column('city', db.String(50))
    arena = db.Column('arena', db.String(100))
    arena_capacity = db.Column('arena_capacity', db.Integer)
    owner = db.Column('owner', db.String(100))
    general_manager = db.Column('general_manager', db.String(100))
    head_coach = db.Column('head_coach', db.String(100))
    g_league_affiliation = db.Column('g_league_affiliation', db.String(100))

class Games(db.Model):
    __tablename__ = 'Game'
    game_date_est = db.Column('player_name', db.DateTime)
    game_id = db.Column('game_id', db.Integer, primary_key=True)
    game_status_text = db.Column('game_status_text', db.Integer)
    home_team_id = db.Column('home_team_id', db.Integer)
    visitor_team_id = db.Column('visitor_team_id', db.Integer)
    season = db.Column('season', db.Integer)
    team_id_home = db.Column('team_id_home', db.Integer)
    pts_home = db.Column('pts_home', db.Numeric(4, 1))
    fg_pct_home = db.Column('fg_pct_home', db.Numeric(4, 3))
    ft_pct_home = db.Column('ft_pct_home', db.Numeric(4, 3))
    fg3_pct_home = db.Column('fg3_pct_home', db.Numeric(4, 3))
    ast_home = db.Column('ast_home', db.Numeric(4, 1))
    reb_home = db.Column('reb_home', db.Numeric(4, 1))
    team_id_away = db.Column('team_id_away', db.Integer)
    pts_away = db.Column('pts_away', db.Numeric(4, 1))
    fg_pct_away = db.Column('fg_pct_away', db.Numeric(4, 3))
    ft_pct_away = db.Column('ft_pct_away', db.Numeric(4, 3))
    fg3_pct_away = db.Column('fg3_pct_away', db.Numeric(4, 3))
    ast_away = db.Column('ast_away', db.Numeric(4, 1))
    reb_away = db.Column('reb_away', db.Numeric(4, 1))
    home_team_wins = db.Column('home_team_wins', db.Boolean)

class Performance(db.Model):
    __tablename__ = 'Performance'
    game_id = db.Column('game_id', db.Integer, primary_key=True)
    team_id = db.Column('team_id', db.Integer, primary_key=True)
    team_abbreviation = db.Column('team_abbreviation', db.String(3))
    team_city = db.Column('team_city', db.String(50))
    player_id = db.Column('player_id', db.Integer, primary_key=True)
    player_name = db.Column('player_name', db.String(50))
    start_position = db.Column('start_position', db.String(1))
    comment = db.Column('comment', db.String(100))
    minutes = db.Column('minutes', db.String(5))
    fgm = db.Column('fgm', db.Integer)
    fga = db.Column('fga', db.Integer)
    fg_pct = db.Column('fg_pct', db.Numeric(3, 1))
    fg3m = db.Column('fg3m', db.Integer)
    fg3a = db.Column('fg3a', db.Integer)
    fg3_pct = db.Column('fg3_pct', db.Numeric(3, 1))
    ftm = db.Column('ftm', db.Integer)
    fta = db.Column('fta', db.Integer)
    ft_pct = db.Column('ft_pct', db.Numeric(3, 1))
    offensive_rebounds = db.Column('offensive_rebounds', db.Integer)
    defensive_rebounds = db.Column('defensive_rebounds', db.Integer)
    rebounds = db.Column('rebounds', db.Integer)
    assists = db.Column('assists', db.Integer)
    steals = db.Column('steals', db.Integer)
    blocks = db.Column('blocks', db.Integer)
    turnovers = db.Column('turnovers', db.Integer)
    personal_fouls = db.Column('personal_fouls', db.Integer)
    points = db.Column('points', db.Integer)
    plus_minus = db.Column('plus_minus', db.Integer)











class Drinker(db.Model):
    __tablename__ = 'drinker'
    name = db.Column('name', db.String(20), primary_key=True)
    address = db.Column('address', db.String(20))
    likes = orm.relationship('Likes')
    frequents = orm.relationship('Frequents')
    @staticmethod
    def edit(old_name, name, address, beers_liked, bars_frequented):
        try:
            db.session.execute('DELETE FROM likes WHERE drinker = :name',
                               dict(name=old_name))
            db.session.execute('DELETE FROM frequents WHERE drinker = :name',
                               dict(name=old_name))
            db.session.execute('UPDATE drinker SET name = :name, address = :address'
                               ' WHERE name = :old_name',
                               dict(old_name=old_name, name=name, address=address))
            for beer in beers_liked:
                db.session.execute('INSERT INTO likes VALUES(:drinker, :beer)',
                                   dict(drinker=name, beer=beer))
            for bar, times_a_week in bars_frequented:
                db.session.execute('INSERT INTO frequents'
                                   ' VALUES(:drinker, :bar, :times_a_week)',
                                   dict(drinker=name, bar=bar,
                                        times_a_week=times_a_week))
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

class Beer(db.Model):
    __tablename__ = 'beer'
    name = db.Column('name', db.String(20), primary_key=True)
    brewer = db.Column('brewer', db.String(20))

class Bar(db.Model):
    __tablename__ = 'bar'
    name = db.Column('name', db.String(20), primary_key=True)
    address = db.Column('address', db.String(20))
    serves = orm.relationship('Serves')

class Likes(db.Model):
    __tablename__ = 'likes'
    drinker = db.Column('drinker', db.String(20),
                        db.ForeignKey('drinker.name'),
                        primary_key=True)
    beer = db.Column('beer', db.String(20),
                     db.ForeignKey('beer.name'),
                     primary_key=True)

class Serves(db.Model):
    __tablename__ = 'serves'
    bar = db.Column('bar', db.String(20),
                    db.ForeignKey('bar.name'),
                    primary_key=True)
    beer = db.Column('beer', db.String(20),
                     db.ForeignKey('beer.name'),
                     primary_key=True)
    price = db.Column('price', db.Float())

class Frequents(db.Model):
    __tablename__ = 'frequents'
    drinker = db.Column('drinker', db.String(20),
                        db.ForeignKey('drinker.name'),
                        primary_key=True)
    bar = db.Column('bar', db.String(20),
                    db.ForeignKey('bar.name'),
                    primary_key=True)
    times_a_week = db.Column('times_a_week', db.Integer())
