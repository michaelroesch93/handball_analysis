from Player import Player
from Team import Team


team = Team("CVJM Walddorf")

player1 = Player("Tom", "Gaiser", 14)
player2 = Player("Noah", "Neuschler", 10)

team.add_player(player1)
team.add_player(player2)

print(team)

team.remove_player(player2)

print(team)