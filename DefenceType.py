"""Defence type enum"""

from enum import Enum
class DefenceType(Enum):
    """Defence type enum"""
    FULLVERTICAL = 1
    FULLHORIZONTAL = 2
    BYBODY = 3
    DIVE = 4
    TILTLEFT = 5
    TILTRIGHT = 6
    LEFTPALM = 7
    RIGHTPALM = 8
    LEFTELBOW = 9
    RIGHTELBOW = 10
    LEFTSHOULDER = 11
    RIGHTSHOULDER = 12
    LEFTBEATOFF = 13
    RIGHTBEATOFF = 14
    MOVEBACK = 15
    MOVESIDE = 16
