# 01. Counter Strike
initial_energy = int(input())
enemy_distance = input()
won_battles = 0
win = True

while initial_energy >= 0 or not enemy_distance == "End of battle":
    if enemy_distance.isnumeric():
        needed_distance = int(enemy_distance)

        if initial_energy < needed_distance:
            print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
            win = False
            break
        else:
            initial_energy -= needed_distance
            won_battles += 1
        if won_battles % 3 == 0:
            initial_energy += won_battles

        enemy_distance = input()

if win:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")