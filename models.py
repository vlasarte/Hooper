from app import db
from sqlalchemy import orm


class Player(db.Model):
    __tablename__ = 'Player'
    name = db.Column('player_name', db.String(100))
    team_id = db.Column('team_id', db.Integer, primary_key=True)
    player_id = db.Column('player_id', db.Integer, primary_key=True)
    season = db.Column('season', db.Integer, primary_key=True)
    age = db.Column('age', db.Integer)
    position = db.Column('position', db.String(1))

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
