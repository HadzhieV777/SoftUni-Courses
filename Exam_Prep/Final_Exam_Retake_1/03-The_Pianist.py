# 03. The Pianist
n = int(input())

music_organizer = {}

for _ in range(n):
    musical_pieces = input()
    music_piece = musical_pieces.split("|")[0]
    music_composer = musical_pieces.split("|")[1]
    music_key = musical_pieces.split("|")[2]
    music_organizer[music_piece] = {'composer': music_composer, 'key': music_key}

commands = input()

while not commands == "Stop":
    command = commands.split("|")[0]
    pieces = commands.split("|")[1]

    if command == "Add":
        composers = commands.split("|")[2]
        keys = commands.split("|")[3]
        if pieces in music_organizer:
            print(f"{pieces} is already in the collection!")
        else:
            music_organizer[pieces] = {'composer': composers, 'key': keys}
            print(f"{pieces} by {composers} in {keys} added to the collection!")

    elif command == "Remove":
        if pieces in music_organizer:
            del music_organizer[pieces]
            print(f"Successfully removed {pieces}!")
        else:
            print(f"Invalid operation! {pieces} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = commands.split("|")[2]

        if pieces in music_organizer:
            music_organizer[pieces]['key'] = new_key
            print(f"Changed the key of {pieces} to {new_key}!")
        else:
            print(f"Invalid operation! {pieces} does not exist in the collection.")

    commands = input()


for key, value in sorted(music_organizer.items(), key=lambda x: (x[0], x[1]['composer'])):
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")