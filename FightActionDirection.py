"""Fight action direction enum"""

from enum import Enum
class FightActionDirection(Enum):
    """
    Fight action direction.
    For example attack from the left or from the right,
    step to the left, to the right, to the front or to the back.
    Counts from the perspective of the fighter.
    """
    LEFT = 1
    RIGHT = 2
    FRONT = 3
    BACK = 4
