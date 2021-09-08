# 01. The Imitation Game
encrypted_message = input()

instructions = input()

while not instructions == "Decode":
    command = instructions.split("|")[0]

    if command == "Move":
        number_of_letters = int(instructions.split("|")[1])
        letters_to_move = encrypted_message[:number_of_letters]
        rest_of_the_message = encrypted_message[number_of_letters:]
        encrypted_message = rest_of_the_message + letters_to_move

    elif command == "Insert":
        index = int(instructions.split("|")[1])
        value = instructions.split("|")[2]

        if 0 <= index <= len(encrypted_message):
            left_side = encrypted_message[:index]
            right_side = encrypted_message[index:]
            encrypted_message = left_side + value + right_side

    elif command == "ChangeAll":
        substring = instructions.split("|")[1]
        replacement = instructions.split("|")[2]

        if substring in encrypted_message:
            encrypted_message = encrypted_message.replace(substring, replacement)

    instructions = input()

print(f"The decrypted message is: {encrypted_message}")