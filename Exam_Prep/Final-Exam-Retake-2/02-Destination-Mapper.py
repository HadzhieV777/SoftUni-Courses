# 02. Destination Mapper
import re
pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'

data = input()
valid_destinations = []
travel_points = 0


for _ in re.finditer(pattern, data):
    destinations = _.group(2)
    travel_points += len(destinations)
    valid_destinations.append(destinations)

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")