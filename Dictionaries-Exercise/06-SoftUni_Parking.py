# 06. SoftUni Parking
n = int(input())

parking = {}

for i in range(n):
    args = input().split()
    command = args[0]
    username = args[1]

    if command == "register":
        license_plate_number = args[2]

        if username in parking:
            print(f"ERROR: already registered with plate number {license_plate_number}")
            continue
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif command == "unregister":

        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            parking.pop(username)
            print(f"{username} unregistered successfully")

for (user, plate) in parking.items():
    print(f"{user} => {plate}")