# 05. Faro Shuffle
cards = input().split()
n = int(input())

half_cards = len(cards) // 2

for i in range(0, n):
    left_half = cards[0:half_cards]
    right_half = cards[half_cards:]

    faro_cards = []

    for j in range(len(left_half)):
        faro_cards.append(left_half[j])
        faro_cards.append(right_half[j])
        cards = faro_cards
print(cards)