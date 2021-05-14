import constants
import copy

def balance_teams(team):
    true_count = 0
    false_count = 0
    while len(team) != 6:
        for player in copied_players:
            if true_count != 3 and player['experience'] == True:
                team.append(player)
                copied_players.remove(player)
                true_count += 1
            if false_count != 3 and player['experience'] == False:
                team.append(player)
                copied_players.remove(player)
                false_count += 1

def stats(team_name, team_content):
    total_players = len(team_content)
    experienced = 0
    inexperienced = 0
    total_height = 0
    player_names_list = []
    guardians_list = []

    for player in team_content:
        if player['experience'] == True:
            experienced += 1
        else:
            inexperienced += 1

        total_height += player['height']
        player_names_list.append(player['name'])
        guardians_list.append(player['guardians'])

    average_height = total_height / total_players

    for player in player_names_list:
        player_names_string = ', '.join(player_names_list)

    for guardian in guardians_list:
        guardians_string = ', '.join(guardians_list)

    guardians_list = guardians_string.split('and ')

    for guardian in guardians_list:
        guardians_string = ', '.join(guardians_list)

    print(f'''
    --------------------
    Team: {team_name} Stats
    --------------------\n
    Total players: {total_players}
    Total experienced: {experienced}
    Total inexperienced: {inexperienced}
    Average height: {int(average_height)} inches\n
    Players on Team: {player_names_string}\n
    Guardians: {guardians_string}''')

copied_players = copy.deepcopy(constants.PLAYERS)

player_height = 0
true_count = 0
false_count = 0
panthers = []
bandits = []
warriors = []

for player in copied_players:
    if player['experience'] == 'YES':
        player['experience'] = True
    else:
        player['experience'] = False
    player_height = int(player['height'][0:2])
    player['height'] = player_height

balance_teams(panthers)
balance_teams(bandits)
balance_teams(warriors)

print('''--------------------------
BASKETBALL TEAM STATS TOOL
--------------------------\n
    ----MENU----''')
while True:
    print(
'''\nHere are your choices:\n
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
                        stats(constants.TEAMS[1], bandits)
                        break
                    elif answer == 3:
                        stats(constants.TEAMS[2], warriors)
                        break
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
    while True:
        answer = input('\nPress C to continue... ')
        if answer.upper() == 'C':
            break
        else:
            continue
    continue
