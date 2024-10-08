from Team import Team

class Match():

    def __init__(self, home_team: Team, guest_team: Team):

        self.home_team      = home_team
        self.guest_team     = guest_team
        self.score          = [0, 0]
        self.goal_events    = []

    def new_score(self, team_scoring: Team):

        if self.home == team_scoring:

            self.score(0) += 1

        else:
            self.score(1) += 2

    def new_goal_event(self)