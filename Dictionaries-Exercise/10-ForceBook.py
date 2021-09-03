# 10. ForceBook
def pipe(user, side, sides_data):
    users = [u for s in sides_data for u in sides_data[s]]

    if side not in sides_data and user not in users:
        sides_data[side] = [user]
    elif user not in users:
        sides_data[side].append(user)
    return sides_data


def arrow(user, side, sides_data):
    if side not in sides_data:
        sides_data[side] = []

    for s in sides_data:
        if user in sides_data[s]:
            user_index = sides_data[s].index(user)
            sides_data[side].append(sides_data[s].pop(user_index))
            return sides_data

    sides_data[side].append(user)
    return sides_data


sides = {}

command = input()
while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        sides = pipe(force_user, force_side, sides)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        sides = arrow(force_user, force_side, sides)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for current_side, members in sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(members) > 0:
        print(f"Side: {current_side}, Members: {len(members)}")
        for m in sorted(members):
            print(f"! {m}")