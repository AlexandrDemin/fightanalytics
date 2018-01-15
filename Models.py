from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

fighters_to_fights = db.Table('fightersToFights',
    db.Column('fighter_id', db.Integer, db.ForeignKey('fighter.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True),
    db.Column('fight_id', db.Integer, db.ForeignKey('fight.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
)

class Fighter(db.Model):
    """Fighter profile"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    sport = db.Column(db.String, nullable=False)
    country = db.Column(db.String(120), nullable=False)
    picture_url = db.Column(db.Text, nullable=False)
    weight_class = db.Column(db.Integer, nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    
    def toDic(self):
        return {
            "id": self.id,
            "name": self.name,
            "sport": self.sport,
            "country": self.country,
            "picture_url": self.picture_url,
            "weight_class": self.weight_class,
            "birth_year": self.birth_year
        }

    def __init__(self, name, sport, country, picture_url, weight_class, birth_year):
        self.name = name
        self.sport = sport
        self.country = country
        self.picture_url = picture_url
        self.weight_class = weight_class
        self.birth_year = birth_year

class Fight(db.Model):
    """Fight"""
    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(120), nullable=False)
    sport = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    result = db.Column(db.Integer, nullable=False)
    winner_id = db.Column(db.Integer, nullable=True)
    fighters = db.relationship('Fighter', secondary=fighters_to_fights, lazy='subquery',
        backref=db.backref('fights', lazy=True))
    attacks = db.relationship('Attack', backref='fight', lazy=True)
    defences = db.relationship('Defence', backref='fight', lazy=True)
    maneuvers = db.relationship('Maneuver', backref='fight', lazy=True)
    tricks = db.relationship('Trick', backref='fight', lazy=True)
    forbidden = db.relationship('Forbidden', backref='fight', lazy=True)
    missed = db.relationship('Missed', backref='fight', lazy=True)

    def toDic(self):
        fighterIds = []
        for fighter in self.fighters:
            fighterIds.append(fighter.id)
        return {
            "id": self.id,
            "place": self.place,
            "sport": self.sport,
            "date": self.date,
            "result": self.result,
            "winner_id": self.winner_id,
            "fighters": fighterIds
        }
    
    def __init__(self, date, place, sport, result, winner_id):
        self.date = date
        self.place = place
        self.sport = sport
        self.result = result
        self.winner_id = winner_id

class Attack(db.Model):
    """Attack action"""
    id = db.Column(db.Integer, primary_key=True)
    fight_id = db.Column(db.Integer, db.ForeignKey('fight.id'),
        nullable=False)
    fighter_id = db.Column(db.Integer, db.ForeignKey('fighter.id'),
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

    def toDic(self):
        return {
            "id": self.id,
            "fight_id": self.fight_id,
            "fighter_id": self.fighter_id,
            "fight_round": self.fight_round,
            "round_minute": self.round_minute,
            "round_second": self.round_second,
            "on_target": self.on_target,
            "direction": self.direction,
            "target": self.target,
            "counterattack_type": self.counterattack_type,
            "strike_type": self.strike_type,
            "strike_character": self.strike_character,
            "in_combination": self.in_combination
        }

    def __init__(self, fight_id, fighter_id, fight_round, round_minute, round_second,
                 on_target, direction, target, counterattack_type, strike_type,
                 strike_character, in_combination):
        self.fight_id = fight_id
        self.fighter_id = fighter_id
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
    fighter_id = db.Column(db.Integer, db.ForeignKey('fighter.id'),
        nullable=False)
    fight_round = db.Column(db.Integer, nullable=False)
    round_minute = db.Column(db.Integer, nullable=False)
    round_second = db.Column(db.Integer, nullable=False)
    success = db.Column(db.Boolean, nullable=False)
    defence_type = db.Column(db.Integer, nullable=False)
    defence_character = db.Column(db.Integer, nullable=False)

    def toDic(self):
        return {
            "id": self.id,
            "fight_id": self.fight_id,
            "fighter_id": self.fighter_id,
            "fight_round": self.fight_round,
            "round_minute": self.round_minute,
            "round_second": self.round_second,
            "success": self.success,
            "defence_type": self.defence_type,
            "defence_character": self.defence_character
        }

    def __init__(self, fight_id, fighter_id, fight_round, round_minute, round_second,
                 success, defence_type, defence_character):
        self.fight_id = fight_id
        self.fighter_id = fighter_id
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
    fighter_id = db.Column(db.Integer, db.ForeignKey('fighter.id'),
        nullable=False)
    fight_round = db.Column(db.Integer, nullable=False)
    round_minute = db.Column(db.Integer, nullable=False)
    round_second = db.Column(db.Integer, nullable=False)
    is_long_distance = db.Column(db.Boolean, nullable=False)
    direction = db.Column(db.Integer, nullable=False)

    def toDic(self):
        return {
            "id": self.id,
            "fight_id": self.fight_id,
            "fighter_id": self.fighter_id,
            "fight_round": self.fight_round,
            "round_minute": self.round_minute,
            "round_second": self.round_second,
            "is_long_distance": self.is_long_distance,
            "direction": self.direction
        }

    def __init__(self, fight_id, fighter_id, fight_round, round_minute, round_second,
                 is_long_distance, direction):
        self.fight_id = fight_id
        self.fighter_id = fight_id
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
    fighter_id = db.Column(db.Integer, db.ForeignKey('fighter.id'),
        nullable=False)
    fight_round = db.Column(db.Integer, nullable=False)
    round_minute = db.Column(db.Integer, nullable=False)
    round_second = db.Column(db.Integer, nullable=False)
    trick_type = db.Column(db.Integer, nullable=False)

    def toDic(self):
        return {
            "id": self.id,
            "fight_id": self.fight_id,
            "fighter_id": self.fighter_id,
            "fight_round": self.fight_round,
            "round_minute": self.round_minute,
            "round_second": self.round_second,
            "trick_type": self.trick_type
        }

    def __init__(self, fight_id, fighter_id, fight_round, round_minute, round_second,
                 trick_type):
        self.fight_id = fight_id
        self.fighter_id = fighter_id
        self.fight_round = fight_round
        self.round_minute = round_minute
        self.round_second = round_second
        self.trick_type = trick_type

class Forbidden(db.Model):
    """Forbidden action"""
    id = db.Column(db.Integer, primary_key=True)
    fight_id = db.Column(db.Integer, db.ForeignKey('fight.id'),
        nullable=False)
    fighter_id = db.Column(db.Integer, db.ForeignKey('fighter.id'),
        nullable=False)
    fight_round = db.Column(db.Integer, nullable=False)
    round_minute = db.Column(db.Integer, nullable=False)
    round_second = db.Column(db.Integer, nullable=False)
    forbidden_type = db.Column(db.Integer, nullable=False)

    def toDic(self):
        return {
            "id": self.id,
            "fight_id": self.fight_id,
            "fighter_id": self.fighter_id,
            "fight_round": self.fight_round,
            "round_minute": self.round_minute,
            "round_second": self.round_second,
            "forbidden_type": self.forbidden_type
        }

    def __init__(self, fight_id, fighter_id, fight_round, round_minute, round_second,
                 forbidden_type):
        self.fight_id = fight_id
        self.fighter_id = fighter_id
        self.fight_round = fight_round
        self.round_minute = round_minute
        self.round_second = round_second
        self.forbidden_type = forbidden_type

class Missed(db.Model):
    """Missed action"""
    id = db.Column(db.Integer, primary_key=True)
    fight_id = db.Column(db.Integer, db.ForeignKey('fight.id'),
        nullable=False)
    fighter_id = db.Column(db.Integer, db.ForeignKey('fighter.id'),
        nullable=False)
    fight_round = db.Column(db.Integer, nullable=False)
    round_minute = db.Column(db.Integer, nullable=False)
    round_second = db.Column(db.Integer, nullable=False)
    target = db.Column(db.Integer, nullable=False)
    missed_type = db.Column(db.Integer, nullable=False)

    def toDic(self):
        return {
            "id": self.id,
            "fight_id": self.fight_id,
            "fighter_id": self.fighter_id,
            "fight_round": self.fight_round,
            "round_minute": self.round_minute,
            "round_second": self.round_second,
            "target": self.target,
            "missed_type": self.missed_type
        }

    def __init__(self, fight_id, fighter_id, fight_round, round_minute, round_second,
                 target, missed_type):
        self.fight_id = fight_id
        self.fighter_id = fighter_id
        self.fight_round = fight_round
        self.round_minute = round_minute
        self.round_second = round_second
        self.target = target
        self.missed_type = missed_type
