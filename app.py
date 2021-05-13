import constants
import copy

copied_players = copy.deepcopy(constants.PLAYERS)

for player in copied_players:
    int(player['height'][0:2])

    if player['experience'] == 'YES':
        player['experience'] = True
    else:
        player['experience'] = False
