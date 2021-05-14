import constants
import copy

def stats(team, team2):
    total_players = len(team2)
    experienced = 1
    inexperienced = 1
    average_height = 2
    player_names_list = []
    guardians = 4

    for player in team2:
        player_names_list.append(player['name'])

    for player in player_names_list:
        player_names_string = ", ".join(player_names_list)

    print(f'''
    --------------------
    Team: {team} Stats
    --------------------\n
    Total players: {total_players}
    Total experienced: {experienced}
    Total inexperienced: {inexperienced}
    Average height: {average_height}\n
    Players on Team: {player_names_string}\n
    Guardians: {guardians}\n''')

copied_players = copy.deepcopy(constants.PLAYERS)
copied_teams = copy.deepcopy(constants.TEAMS)

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

teams = [panthers, bandits, warriors]

print('''--------------------------
BASKETBALL TEAM STATS TOOL
--------------------------\n
    ----MENU----\n''')
while True:
    print(
'''Here are your choices:\n
    1) Display Team Stats
    2) Quit''')
    try:
        answer = input('\nEnter an option > ')
        answer = int(answer)
        if answer == 1:
            print('''
    1) Panthers
    2) Bandits
    3) Warriors''')
            while True:
                try:
                    answer = input('\nEnter an option > ')
                    answer = int(answer)
                    if answer == 1:
                        stats(constants.TEAMS[0], panthers)
                        break
                    elif answer == 2:
                        print('yoo2')
                    elif answer == 3:
                        print('yoo3')
                    else:
                        print('\nPlease answer only 1, 2, or 3.')
                        continue
                except ValueError:
                    print('\nPlease answer only 1, 2, or 3.')
                    continue
            break
        elif answer == 2:
            print('''
    ------------
    TOOL CLOSING
    ------------\n''')
            exit()
        else:
            print('\nPlease answer only 1 or 2.\n')
            continue
    except ValueError:
        print('\nPlease answer only 1 or 2.\n')
        continue
