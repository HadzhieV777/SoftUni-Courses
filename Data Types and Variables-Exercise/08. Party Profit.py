# 08. Party Profit
party_size = int(input())
days = int(input())
day = 0
coins = 0
coin_per_comp = 0

for day in range(days):
    day += 1
    coins += 50
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    coins -= party_size * 2
    if day % 3 == 0:
        coins -= party_size * 3
    if day % 5 == 0:
        coins += party_size * 20
        if day % 3 == 0:
            coins -= party_size * 2

coin_per_comp = coins // party_size

print(f"{party_size} companions received {coin_per_comp} coins each.")
