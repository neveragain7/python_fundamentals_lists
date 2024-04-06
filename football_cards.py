cards = input()

match_is_terminated = False

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards_list = cards.split()

for card in cards_list:
    card_elements = card.split("-")
    team = card_elements[0]
    player = int(card_elements[1])

    if team == "A":
        if player in team_a:
            team_a.remove(player)
    elif team == "B":
        if player in team_b:
            team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        match_is_terminated = True
        break

if not match_is_terminated:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
    print("Game was terminated")
