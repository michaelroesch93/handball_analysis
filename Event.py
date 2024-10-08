from datetime import datetime
from Player import Player
from Team import Team
from enumerations import Position

class Event():

    def __init__(self):

        self.time_stamp = datetime.now

class Goal(Event):

    def __init__(self, team_scoring: Team, player_scoring: Player, position: Position):
        
        super().__init__()
        self.team_scoring   = team_scoring
        self.player_scoring = player_scoring
        self.position       = position


