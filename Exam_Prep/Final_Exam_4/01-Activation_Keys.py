# 01. Activation Keys
raw_activation_key = input()
strings_with_instructions = input()

while not strings_with_instructions == "Generate":
    commands = strings_with_instructions.split(">>>")[0]

    if commands == "Contains":
        substring = strings_with_instructions.split(">>>")[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif commands == "Flip":
        subcommand = strings_with_instructions.split(">>>")[1]
        start_index = int(strings_with_instructions.split(">>>")[2])
        end_index = int(strings_with_instructions.split(">>>")[3])
        piece_to_change = raw_activation_key[start_index:end_index]
        first_half = raw_activation_key[:start_index]
        second_half = raw_activation_key[end_index:]

        if subcommand == "Upper":
            raw_activation_key = first_half + piece_to_change.upper() + second_half
        elif subcommand == "Lower":
            raw_activation_key = first_half + piece_to_change.lower() + second_half
        print(raw_activation_key)

    elif commands == "Slice":
        start_index = int(strings_with_instructions.split(">>>")[1])
        end_index = int(strings_with_instructions.split(">>>")[2])
        first_half = raw_activation_key[:start_index]
        second_half = raw_activation_key[end_index:]
        raw_activation_key = first_half + second_half

        print(raw_activation_key)

    strings_with_instructions = input()

print(f"Your activation key is: {raw_activation_key}")