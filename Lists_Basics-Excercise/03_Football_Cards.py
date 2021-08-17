# 03. Football Cards
team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
players_input = input().split()

is_terminated = False


for player in players_input:
    card_info = player.split("-")
    player_team = card_info[0]
    player_number = int(card_info[1])

    if player_team == 'A' and player_number in team_a:
        team_a.remove(player_number)
    elif player_team == 'B' and player_number in team_b:
        team_b.remove(player_number)
    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if is_terminated:
    print('Game was terminated')