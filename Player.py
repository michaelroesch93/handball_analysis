
class Player():

    def __init__(self, first_name, last_name, number):

        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.id     = id(self)

    def __str__(self):

        return f"Player - {self.first_name} {self.last_name}, {self.number}"

    def rename(self, new_first_name, new_last_name):

        self.first_name = new_first_name
        self.last_name = new_last_name

    def assign_team(self, team):

        self.team = team

    

