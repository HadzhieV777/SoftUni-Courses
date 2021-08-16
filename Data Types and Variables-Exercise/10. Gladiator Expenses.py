# 10. Gladiator Expenses
lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
lost_fights_count = 0
budget = 0
shield_damage = 0


for lost_fights_count in range(0, lost_fights):
    lost_fights_count += 1
    if lost_fights_count % 2 == 0:
        budget += helmet_price
    if lost_fights_count % 3 == 0:
        budget += sword_price
    if lost_fights_count % 2 == 0 and lost_fights_count % 3 == 0:
        budget += shield_price
        shield_damage += 1
        if shield_damage % 2 == 0:
            budget += armor_price
print(f'Gladiator expenses: {budget:.2f} aureus')