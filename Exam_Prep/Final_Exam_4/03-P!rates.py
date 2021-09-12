# 03. P!rates
cities_info = input()

cities = {}

while not cities_info == "Sail":
    city = cities_info.split("||")[0]
    population = int(cities_info.split("||")[1])
    gold = int(cities_info.split("||")[2])

    if city not in cities:
        cities[city] = {"population": 0, "gold": 0}
    cities[city]["population"] += population
    cities[city]["gold"] += gold

    cities_info = input()

events = input()

while not events == "End":
    command = events.split("=>")[0]

    if command == "Plunder":
        town_name = events.split("=>")[1]
        town_citizens = int(events.split("=>")[2])
        town_gold = int(events.split("=>")[3])
        cities[town_name]["population"] -= town_citizens
        cities[town_name]["gold"] -= town_gold
        print(f"{town_name} plundered! {town_gold} gold stolen, {town_citizens} citizens killed.")

        if cities[town_name]["population"] <= 0 or cities[town_name]["gold"] <= 0:
            del cities[town_name]
            print(f"{town_name} has been wiped off the map!")

    elif command == "Prosper":
        town_name = events.split("=>")[1]
        town_gold = int(events.split("=>")[2])
        if town_gold < 0:
            print("Gold added cannot be a negative number!")
            events = input()
            continue
        else:
            cities[town_name]["gold"] += town_gold
            print(f"{town_gold} gold added to the city treasury. {town_name} now has {cities[town_name]['gold']} gold.")

    events = input()

if not cities:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    sorted_cities = sorted(cities.items(), key=lambda tkvp: (-tkvp[1]['gold'], tkvp[0]))
    print(f"Ahoy, Captain! There are {len(sorted_cities)} wealthy settlements to go to:")
    for city, data in sorted_cities:
        print(f"{city} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")