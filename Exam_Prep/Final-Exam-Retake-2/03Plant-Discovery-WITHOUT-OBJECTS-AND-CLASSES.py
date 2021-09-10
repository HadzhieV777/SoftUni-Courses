# 03. Plant Discovery-WITHOUT OBJECTS AND CLASSES
n = int(input())

plant_book = {}
plant_rating = {}

for _ in range(n):
    information = input().split('<->')
    plant = information[0]
    rarity = int(information[1])
    if plant not in plant_book:
        plant_book[plant] = []
        plant_book[plant].append(rarity)
    else:
        plant_book[plant][0] += rarity

commands = input()

while not commands == "Exhibition":
    command = commands.split(": ")[0]
    command_splited = commands.split(": ")[1]
    plant_name = command_splited.split(" - ")[0]

    if command == "Rate":
        if plant_name not in plant_book:
            print("error")
        else:
            rating = int(command_splited.split(" - ")[1])
            if plant_name not in plant_rating:
                plant_rating[plant_name] = []
            plant_rating[plant_name].append(rating)

    elif command == "Update":
        new_rarity = int(command_splited.split(" - ")[1])
        if plant_name not in plant_book:
            print("error")
        else:
            plant_book[plant_name][0] = new_rarity

    elif command == "Reset":
        if plant_name not in plant_rating:
            print("error")
        else:
            plant_rating[plant_name] = []
    else:
        print("error")

    commands = input()

for plant in plant_book.keys():
    if plant not in plant_rating:
        average_rating = 0
    else:
        if len(plant_rating[plant]) > 0:
            average_rating = sum(plant_rating[plant]) / len(plant_rating[plant])
        else:
            average_rating = 0
    plant_book[plant].append(average_rating)

sorted_plants = sorted(plant_book.items(), key=lambda kvp: ([-kvp[1][0]], -kvp[1][1]))
print("Plants for the exhibition:")
for plant, info in sorted_plants:
    print(f"- {plant}; Rarity: {info[0]}; Rating: {info[1]:.2f}")