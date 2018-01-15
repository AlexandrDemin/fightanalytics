from Models import (Fight, Fighter, Attack, Defence, Maneuver, Trick, Forbidden, Missed)

def getFighterFromJson(data):
    name = data['name']
    sport = data['sport']
    country = data['country']
    picture_url = data['picture_url']
    weight_class = data['weight_class']
    birth_year = data['birth_year']
    return Fighter(name, sport, country, picture_url, weight_class, birth_year)

def getFightFromJson(data):
    place = data['place']
    sport = data['sport']
    date = data['date']
    result = data['result']
    winner_id = data['winner_id']
    return Fight(date, place, sport, result, winner_id)
