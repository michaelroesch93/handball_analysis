from Player import Player

class Team():

    def __init__(self, name):

        self.name = name
        self.players = []

    def __str__(self):

        # set up string

        return_string = f"Team - {self.name} \n"

        for player in self.players:

            return_string += "    " + player.__str__() + "\n"

        return return_string

    def add_player(self, player_to_add: Player):

        self.players.append(player_to_add)

    def remove_player(self, player_to_remove: Player):

        for i, player in enumerate(self.players):
            if player.id is player_to_remove.id:
                del self.players[i]
                break  # Exit after removing the first match


