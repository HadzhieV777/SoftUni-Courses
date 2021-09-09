# 01. World Tour
all_stops = input()
commands = input()

is_valid = False

while not commands == "Travel":
    command = commands.split(":")[0]

    if command == "Add Stop":
        index = int(commands.split(":")[1])
        string = commands.split(":")[2]
        if 0 <= index < len(all_stops):
            left_side = all_stops[:index]
            right_side = all_stops[index:]
            all_stops = left_side + string + right_side
            is_valid = True

    elif command == "Remove Stop":
        start_index = int(commands.split(":")[1])
        end_index = int(commands.split(":")[2])
        if 0 <= start_index < len(all_stops) and 0 <= end_index < len(all_stops):
            left_side = all_stops[:start_index]
            middle = all_stops[start_index:end_index + 1]
            all_stops = all_stops.replace(middle, "", 1)
            is_valid = True

    elif command == "Switch":
        old_string = commands.split(":")[1]
        new_string = commands.split(":")[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
            is_valid = True

    if is_valid:
        print(all_stops)
    commands = input()

print(f"Ready for world tour! Planned stops: {all_stops}")