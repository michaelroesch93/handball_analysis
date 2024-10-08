from enum import Enum

class Position(Enum):

    LEFT_WING = 0
    RIGHT_WING = 1
    LEFT_BACK = 2
    LEFT_BREAKTHROUGH = 3
    CENTER_BACK = 4
    CENTER_BREAKTHROUGH = 5
    RIGHT_BACK = 6
    RIGHT_BREAKTHROUGH = 7
    PIVOT_CENTER = 8
    PIVOT_LEFT = 9
    PIVOT_RIGHT = 10

class GoalArea(Enum):

    TOP_RIGHT       = 0
    TOP_CENTER      = 1
    TOP_LEFT        = 2
    HALF_RIGHT      = 3
    HALF_CENTER     = 4
    HALF_LEFT       = 5
    BOTTOM_RIGH     = 6
    BOTTOM_CENTER   = 7
    BOTTOM_LEFT     = 8

class GoalType(Enum):

    FASTBREAK = 0
    FAST_SETPLAY = 1
    SET_PLAY = 2
    PENALTy = 3