# 02. Mu_Online
max_health = 100
initial_bitcoins = 0
dungeon_rooms = [el for el in input().split("|")]
best_room = 1
win = True
initial_health = max_health

for room in dungeon_rooms:
    command = room.split()[0]
    best_room += 1

    if command == "potion":
        potion_amount = int(room.split()[1])
        if initial_health + potion_amount > max_health:
            potion_amount = max_health - initial_health
            initial_health = max_health
        else:
            initial_health += potion_amount
        print(f"You healed for {potion_amount} hp.")
        print(f"Current health: {initial_health} hp.")


    elif command == "chest":
        bitcoin_amount = int(room.split()[1])
        initial_bitcoins += bitcoin_amount
        print(f"You found {bitcoin_amount} bitcoins.")

    else:
        attack_of_monster = int(room.split()[1])
        initial_health -= attack_of_monster

        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room - 1}")
            win = False
            break

if best_room >= len(dungeon_rooms):
    if win:
        print(f"You've made it!\n"
              f"Bitcoins: {initial_bitcoins}\n"
              f"Health: {initial_health}")