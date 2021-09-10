# 03. Plant Discovery
class Plant:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.ratings = []

    def rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return 0


n = int(input())

plants_book = {}

for i in range(n):
    plants_info = input()
    plant_name = plants_info.split("<->")[0]
    plant_rarity = int(plants_info.split("<->")[1])
    plants_book[plant_name] = Plant(plant_name, int(plant_rarity))


commands = input()
ratings_count = 0

while not commands == "Exhibition":
    command = commands.split(": ")[0]
    second_part = commands.split(": ")[1]
    plant_name = second_part.split(" - ")[0]

    if plant_name not in plants_book:
        print('error')

    elif command == "Rate":
        rating = int(second_part.split(" - ")[1])
        plants_book[plant_name].ratings.append(int(rating))

    elif command == "Update":
        new_rarity = int(second_part.split(" - ")[1])
        plants_book[plant_name].rarity = new_rarity

    elif command == "Reset":
        plants_book[plant_name].ratings.clear()

    commands = input()

sorted_plants = sorted(plants_book.values(), key=lambda p: (p.rarity, p.rating()), reverse=True)

print(f'Plants for the exhibition:')
for plant in sorted_plants:
    print(f'- {plant.name}; Rarity: {plant.rarity}; Rating: {plant.rating():.2f}')