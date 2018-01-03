"""Type of action in a fight enum"""

from enum import Enum
class ActionType(Enum):
    """Type of action in a fight"""
    ATTACK = 1
    DEFENCE = 2
    MANEUVER = 3
    TRICK = 4
    FORBIDDEN = 5
    MISSED = 6
