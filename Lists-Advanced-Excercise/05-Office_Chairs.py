# 05. Office Chairs
number_of_rooms = int(input())
chairs_left = 0
needed_chairs = []
in_room = []
chairs_are_enough = True

for i in range(0, number_of_rooms):
    info = input().split()
    chairs = info[0]
    visitors = int(info[1])
    if len(chairs) >= visitors:
        chairs_left += (len(chairs) - visitors)
    if len(chairs) < visitors:
        needed = visitors - len(chairs)
        needed_chairs.append(needed)
        in_room.append(i + 1)
        chairs_are_enough = False

if not chairs_are_enough:
    for i in range(len(needed_chairs)):
        print(f"{needed_chairs[i]} more chairs needed in room {in_room[i]}")
else:
    print(f"Game On, {chairs_left} free chairs left")