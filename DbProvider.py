from Models import (db, Fight, Fighter, Attack, Defence, Maneuver, Trick, Forbidden, Missed)

def getFighters(sport):
    fighters = Fighter.query.filter_by(sport=sport).all()
    return fighters

def saveFighter(fighter):
    db.session.add(fighter)
    db.session.commit()

def getFights(fighter_ids):
    pass

def saveFight(fight):
    pass

def saveActions(actions):
    pass

def removeActions(actions):
    pass

def getActions(fight_id):
    pass
