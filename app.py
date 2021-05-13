import constants
import copy

print('BASKETBALL TEAM STATS TOOL\n\n----MENU----\n\nHere are your choices:\n 1) Display Team Stats\n 2) Quit')
# input("\nEnter an option > ")

copied_players = copy.deepcopy(constants.PLAYERS)

for player in copied_players:
    int(player['height'][0:2])

    if player['experience'] == 'YES':
        player['experience'] = True
    else:
        player['experience'] = False

panthers = [
copied_players[0],
copied_players[1],
copied_players[2],
copied_players[3],
copied_players[4],
copied_players[6],
]

bandits = [
copied_players[5],
copied_players[7],
copied_players[8],
copied_players[9],
copied_players[10],
copied_players[11],
]

warriors = [
copied_players[12],
copied_players[13],
copied_players[14],
copied_players[15],
copied_players[16],
copied_players[17],
]

print(panthers)
