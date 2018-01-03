"""Actions in a fight"""

from ActionType import ActionType

class FightAction():
    """Base action in a fight"""
    def __init__(self, fighter_id, fight_id, fight_round, round_minute, round_second, action_type):
        self.fighter_id = fighter_id
        self.fight_id = fight_id
        self.fight_round = fight_round
        self.round_minute = round_minute
        self.round_second = round_second
        self.action_type = action_type

class Attack(FightAction):
    """Attack action"""
    def __init__(self, fighter_id, fight_id, fight_round, round_minute, round_second,
                 on_target, direction, target, counterattack_type, strike_type,
                 strike_character, in_combination):
        action_type = ActionType.ATTACK
        super().__init__(fighter_id, fight_id, fight_round, round_minute, round_second, action_type)
        self.on_target = on_target
        self.direction = direction
        self.target = target
        self.counterattack_type = counterattack_type
        self.strike_type = strike_type
        self.strike_character = strike_character
        self.in_combination = in_combination

class Defence(FightAction):
    """Defence action"""
    def __init__(self, fighter_id, fight_id, fight_round, round_minute, round_second,
                 success, defence_type, defence_character):
        action_type = ActionType.DEFENCE
        super().__init__(fighter_id, fight_id, fight_round, round_minute, round_second, action_type)
        self.success = success
        self.defence_type = defence_type
        self.defence_character = defence_character

class Maneuver(FightAction):
    """Maneuver action"""
    def __init__(self, fighter_id, fight_id, fight_round, round_minute, round_second,
                 is_long_distance, direction):
        action_type = ActionType.MANEUVER
        super().__init__(fighter_id, fight_id, fight_round, round_minute, round_second, action_type)
        self.is_long_distance = is_long_distance
        self.direction = direction

class Trick(FightAction):
    """Trick action"""
    def __init__(self, fighter_id, fight_id, fight_round, round_minute, round_second,
                 trick_type):
        action_type = ActionType.TRICK
        super().__init__(fighter_id, fight_id, fight_round, round_minute, round_second, action_type)
        self.trick_type = trick_type

class Forbidden(FightAction):
    """Forbidden action"""
    def __init__(self, fighter_id, fight_id, fight_round, round_minute, round_second,
                 forbidden_type):
        action_type = ActionType.FORBIDDEN
        super().__init__(fighter_id, fight_id, fight_round, round_minute, round_second, action_type)
        self.forbidden_type = forbidden_type

class Missed(FightAction):
    """Missed action"""
    def __init__(self, fighter_id, fight_id, fight_round, round_minute, round_second,
                 target, missed_type):
        action_type = ActionType.MISSED
        super().__init__(fighter_id, fight_id, fight_round, round_minute, round_second, action_type)
        self.target = target
        self.missed_type = missed_type
