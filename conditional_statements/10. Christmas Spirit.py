# 10. Christmas Spirit
allowed_quantity = int(input())
days_left = int(input())
total_spirit = 0
total_sum = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

for current_day in range(1, days_left+1):
    if current_day % 11 == 0:
        allowed_quantity += 2
    if current_day % 2 == 0:
        total_sum += allowed_quantity * ornament_set_price
        total_spirit += 5
    if current_day % 3 == 0:
        total_sum += (tree_skirt_price + tree_garlands_price) * allowed_quantity
        total_spirit += 13
    if current_day % 5 == 0:
        total_sum += tree_lights_price * allowed_quantity
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_sum += tree_skirt_price + tree_garlands_price + tree_lights_price
if days_left % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_sum}")
print(f"Total spirit: {total_spirit}")