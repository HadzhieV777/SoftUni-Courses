# 03. Moving Target
sequence_of_targets = [int(el) for el in input().split()]
command_strings = input()

while not command_strings == "End":
    command = command_strings.split()[0]
    index = int(command_strings.split()[1])

    if command == "Shoot":
        power = int(command_strings.split()[2])
        if index in range(len(sequence_of_targets)):
            sequence_of_targets[index] -= power
            if sequence_of_targets[index] <= 0:
                sequence_of_targets.pop(index)

    if command == "Add":
        value = int(command_strings.split()[2])
        if index in range(len(sequence_of_targets)):
            sequence_of_targets.insert(index, value)
        else:
            print("Invalid placement!")

    if command == "Strike":
        radius = int(command_strings.split()[2])
        left_index = index - radius
        right_index = index + radius
        if left_index >= 0 and right_index < len(sequence_of_targets):
            left_part = sequence_of_targets[:left_index]
            right_part = sequence_of_targets[right_index + 1:]
            sequence_of_targets = left_part + right_part
        else:
            print("Strike missed!")

    command_strings = input()

str_of_targets = [str(el) for el in sequence_of_targets]
print("|".join(str_of_targets))