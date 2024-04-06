cards_string = input()
count_of_faro_shuffles = int(input())

cards_list = cards_string.split()

half_cards = len(cards_list) // 2

for _ in range(count_of_faro_shuffles):
    shuffled_cards = []
    left_side = cards_list[:half_cards]
    right_side = cards_list[half_cards:]
    for card in range(len(left_side)):
        shuffled_cards.append(left_side[card])
        shuffled_cards.append(right_side[card])

    cards_list = shuffled_cards

print(shuffled_cards)
