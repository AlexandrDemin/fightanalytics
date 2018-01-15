from Models import (db, Fight, Fighter, Attack, Defence, Maneuver, Trick, Forbidden, Missed)
from CounterattackType import CounterattackType
from DefenceCharacter import DefenceCharacter
from DefenceType import DefenceType
from FightActionDirection import FightActionDirection
from ForbiddenType import ForbiddenType
from MissedType import MissedType
from Sports import Sports
from StrikeCharacter import StrikeCharacter
from StrikeTarget import StrikeTarget
from StrikeType import StrikeType
from TrickType import TrickType
from WeightClass import WeightClass
from flask import Flask, request, url_for, render_template, abort, make_response, redirect, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from Config import ProductionConfig
from Config import DevelopmentConfig
import json
import logging
from Helpers import getFighterFromJson, getFightFromJson

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

@app.route('/api/')
def api():
    return "Here will be API description"

@app.route('/api/fighters/')
def fighters():
    fighters = Fighter.query.all()
    res = []
    for fighter in fighters:
        res.append(fighter.toDic())
    return jsonify(res)

@app.route('/api/fighter/<id>', methods=['POST','GET'])
def fighter(id):
    try:
        id = int(id)
    except:
        resp = jsonify({
            "result": "Error",
            "description": "Invalid id: {}".format(id)
        })
        resp.status_code = 500
        return resp
    if request.method == 'POST':
        data = request.get_json()
        if int(id) > 0:
            try:
                fighter = Fighter.query.get(id)
            except:
                resp = jsonify({
                    "result": "Error",
                    "description": "No fighter found with id {}".format(id)
                })
                resp.status_code = 500
                return resp
            fighter.name = data['name']
            fighter.sport = data['sport']
            fighter.country = data['country']
            fighter.picture_url = data['picture_url']
            fighter.weight_class = data['weight_class']
            fighter.birth_year = data['birth_year']
        else:
            fighter = getFighterFromJson(data)
            db.session.add(fighter)
        db.session.commit()
        resp = jsonify({
            "result": "Success",
            "data": fighter.toDic()
        })
        resp.status_code = 200
        return resp
    elif request.method == 'GET':
        if int(id) > 0:
            try:
                fighter = Fighter.query.get(id)
            except:
                resp = jsonify({
                    "result": "Error",
                    "description": "No fighter found with id {}".format(id)
                })
                resp.status_code = 500
                return resp
            if fighter != None:
                resp = jsonify(fighter.toDic())
                resp.status_code = 200
                return resp
            else:
                resp = jsonify({
                    "result": "Error",
                    "description": "No fighter found with id {}".format(id)
                })
                resp.status_code = 500
                return resp
        else:
            resp = jsonify({
                "result": "Error",
                "description": "No fighter id present"
            })
            resp.status_code = 500
            return resp

@app.route('/api/fights/')
def fights():
    fights = Fight.query.all()
    res = []
    for fight in fights:
        res.append(fight.toDic())
    return jsonify(res)

@app.route('/api/fight/<id>', methods=['POST','GET'])
def fight(id):
    try:
        id = int(id)
    except:
        resp = jsonify({
            "result": "Error",
            "description": "Invalid id: {}".format(id)
        })
        resp.status_code = 500
        return resp
    if request.method == 'POST':
        data = request.get_json()
        if int(id) > 0:
            try:
                fight = Fight.query.get(id)
            except:
                resp = jsonify({
                    "result": "Error",
                    "description": "No fight found with id {}".format(id)
                })
                resp.status_code = 500
                return resp
            fight.place = data['place']
            fight.sport = data['sport']
            fight.date = data['date']
            fight.result = data['result']
            fight.winner_id = data['winner_id']
            new_fighters = data['fighters']
            fight.fighters = []
            for fighter_id in fighters:
                try:
                    fighter = Fighter.query.get(fighter_id)
                    fight.fighters.append(fighter)
                except:
                    db.session.rollback()
                    resp = jsonify({
                        "result": "Error",
                        "description": "No fighter found with id {}".format(fighter_id)
                    })
                    resp.status_code = 500
                    return resp
        else:
            fight = getFightFromJson(data)
            fighters = data['fighters']
            for fighter_id in fighters:
                try:
                    fighter = Fighter.query.get(fighter_id)
                    fight.fighters.append(fighter)
                except:
                    db.session.rollback()
                    resp = jsonify({
                        "result": "Error",
                        "description": "No fighter found with id {}".format(fighter_id)
                    })
                    resp.status_code = 500
                    return resp
            db.session.add(fight)
        db.session.commit()
        resp = jsonify({
            "result": "Success",
            "data": fight.toDic()
        })
        resp.status_code = 200
        return resp
    elif request.method == 'GET':
        if int(id) > 0:
            try:
                fight = Fight.query.get(id)
            except:
                resp = jsonify({
                    "result": "Error",
                    "description": "No fight found with id {}".format(id)
                })
                resp.status_code = 500
                return resp
            if fight != None:
                resp = jsonify(fight.toDic())
                resp.status_code = 200
                return resp
            else:
                resp = jsonify({
                    "result": "Error",
                    "description": "No fight found with id {}".format(id)
                })
                resp.status_code = 500
                return resp
        else:
            resp = jsonify({
                "result": "Error",
                "description": "No fight id present"
            })
            resp.status_code = 500
            return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
