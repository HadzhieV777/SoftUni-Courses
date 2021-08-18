# 10. Bread Factory
initial_energy = 100
initial_coins = 100

daily_events = [el for el in input().split("|")]

day_complete = True

for element in daily_events:
    event = element.split("-")[0]
    number = int(element.split("-")[1])

    if event == "rest":
        initial_energy += number
        if (initial_energy + number) > 100:
            number = 100 - initial_energy
            initial_energy = 100
        if number < 0:
            print(f"You gained 0 energy.")
        else:
            print(f"You gained {number} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event == "order":

        if initial_energy - 30 >= 0:
            initial_coins += number
            initial_energy -= 30
            print(f"You earned {number} coins.")
        else:
            initial_energy += 50
            print(f"You had to rest!")

    else:
        initial_coins -= number
        if initial_coins > 0:
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            day_complete = False
            break

if day_complete:
    print(f"Day completed!\n"
          f"Coins: {initial_coins}\n"
          f"Energy: {initial_energy}")
