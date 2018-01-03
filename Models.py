from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Config import ProductionConfig
from Config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

fighters_to_fights = db.Table('fightersToFights',
    db.Column('fighter_id', db.Integer, db.ForeignKey('fighter.id'), primary_key=True),
    db.Column('fight_id', db.Integer, db.ForeignKey('fight.id'), primary_key=True)
)

class Fighter(db.Model):
    """Fighter profile"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    sports = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(120), nullable=False)
    picture_url = db.Column(db.Text, nullable=False)
    weight_class = db.Column(db.Integer, nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    fights = db.relationship('Fight', secondary=fighters_to_fights, lazy='subquery',
        backref=db.backref('fighters', lazy=True))

    def __init__(self, name, sports, country, picture_url, weight_class, birth_year):
        self.name = name
        self.sports = sports
        self.country = country
        self.picture_url = picture_url
        self.weight_class = weight_class
        self.birth_year = birth_year

class Fight(db.Model):
    """Fight"""
    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(120), nullable=False)
    sport = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    attacks = db.relationship('Attack', backref='fight', lazy=True)
    defences = db.relationship('Defence', backref='fight', lazy=True)
    maneuvers = db.relationship('Maneuver', backref='fight', lazy=True)
    tricks = db.relationship('Trick', backref='fight', lazy=True)
    forbidden = db.relationship('Forbidden', backref='fight', lazy=True)
    missed = db.relationship('Missed', backref='fight', lazy=True)

    def __init__(self, date, place, sport):
        self.date = date
        self.place = place
        self.sport = sport

class Attack(db.Model):
    """Attack action"""
    id = db.Column(db.Integer, primary_key=True)
    fight_id = db.Column(db.Integer, db.ForeignKey('fight.id'),
        nullable=False)
    fight_round = db.Column(db.Integer, nullable=False)
    round_minute = db.Column(db.Integer, nullable=False)
    round_second = db.Column(db.Integer, nullable=False)
    on_target = db.Column(db.Boolean, nullable=False)
    direction = db.Column(db.Integer, nullable=False)
    target = db.Column(db.Integer, nullable=False)
    counterattack_type = db.Column(db.Integer, nullable=False)
    strike_type = db.Column(db.Integer, nullable=False)
    strike_character = db.Column(db.Integer, nullable=False)
    in_combination = db.Column(db.Boolean, nullable=False)

    def __init__(self, fight_id, fight_round, round_minute, round_second,
                 on_target, direction, target, counterattack_type, strike_type,
                 strike_character, in_combination):
        self.fight_id = fight_id
        self.fight_round = fight_round
        self.round_minute = round_minute
        self.round_second = round_second
        self.on_target = on_target
        self.direction = direction
        self.target = target
        self.counterattack_type = counterattack_type
        self.strike_type = strike_type
        self.strike_character = strike_character
        self.in_combination = in_combination

class Defence(db.Model):
    """Defence action"""
    id = db.Column(db.Integer, primary_key=True)
    fight_id = db.Column(db.Integer, db.ForeignKey('fight.id'),
        nullable=False)
    fight_round = db.Column(db.Integer, nullable=False)
    round_minute = db.Column(db.Integer, nullable=False)
    round_second = db.Column(db.Integer, nullable=False)
    success = db.Column(db.Boolean, nullable=False)
    defence_type = db.Column(db.Integer, nullable=False)
    defence_character = db.Column(db.Integer, nullable=False)

    def __init__(self, fight_id, fight_round, round_minute, round_second,
                 success, defence_type, defence_character):
        self.fight_id = fight_id
        self.fight_round = fight_round
        self.round_minute = round_minute
        self.round_second = round_second
        self.success = success
        self.defence_type = defence_type
        self.defence_character = defence_character

class Maneuver(db.Model):
    """Maneuver action"""
    id = db.Column(db.Integer, primary_key=True)
    fight_id = db.Column(db.Integer, db.ForeignKey('fight.id'),
        nullable=False)
    fight_round = db.Column(db.Integer, nullable=False)
    round_minute = db.Column(db.Integer, nullable=False)
    round_second = db.Column(db.Integer, nullable=False)
    is_long_distance = db.Column(db.Boolean, nullable=False)
    direction = db.Column(db.Integer, nullable=False)

    def __init__(self, fight_id, fight_round, round_minute, round_second,
                 is_long_distance, direction):
        self.fight_id = fight_id
        self.fight_round = fight_round
        self.round_minute = round_minute
        self.round_second = round_second
        self.is_long_distance = is_long_distance
        self.direction = direction

class Trick(db.Model):
    """Trick action"""
    id = db.Column(db.Integer, primary_key=True)
    fight_id = db.Column(db.Integer, db.ForeignKey('fight.id'),
        nullable=False)
    fight_round = db.Column(db.Integer, nullable=False)
    round_minute = db.Column(db.Integer, nullable=False)
    round_second = db.Column(db.Integer, nullable=False)
    trick_type = db.Column(db.Integer, nullable=False)

    def __init__(self, fight_id, fight_round, round_minute, round_second,
                 trick_type):
        self.fight_id = fight_id
        self.fight_round = fight_round
        self.round_minute = round_minute
        self.round_second = round_second
        self.trick_type = trick_type

class Forbidden(db.Model):
    """Forbidden action"""
    id = db.Column(db.Integer, primary_key=True)
    fight_id = db.Column(db.Integer, db.ForeignKey('fight.id'),
        nullable=False)
    fight_round = db.Column(db.Integer, nullable=False)
    round_minute = db.Column(db.Integer, nullable=False)
    round_second = db.Column(db.Integer, nullable=False)
    forbidden_type = db.Column(db.Integer, nullable=False)

    def __init__(self, fight_id, fight_round, round_minute, round_second,
                 forbidden_type):
        self.fight_id = fight_id
        self.fight_round = fight_round
        self.round_minute = round_minute
        self.round_second = round_second
        self.forbidden_type = forbidden_type

class Missed(db.Model):
    """Missed action"""
    id = db.Column(db.Integer, primary_key=True)
    fight_id = db.Column(db.Integer, db.ForeignKey('fight.id'),
        nullable=False)
    fight_round = db.Column(db.Integer, nullable=False)
    round_minute = db.Column(db.Integer, nullable=False)
    round_second = db.Column(db.Integer, nullable=False)
    target = db.Column(db.Integer, nullable=False)
    missed_type = db.Column(db.Integer, nullable=False)

    def __init__(self, fight_id, fight_round, round_minute, round_second,
                 target, missed_type):
        self.fight_id = fight_id
        self.fight_round = fight_round
        self.round_minute = round_minute
        self.round_second = round_second
        self.target = target
        self.missed_type = missed_type
