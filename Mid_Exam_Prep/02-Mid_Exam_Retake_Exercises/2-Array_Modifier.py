# 02. Array Modifier
array = [int(el) for el in input().split()]
command_string = input()

while not command_string == "end":
    command = command_string.split()[0]

    if command == "swap":
        first_index = int(command_string.split()[1])
        second_index = int(command_string.split()[2])
        array[first_index], array[second_index] = array[second_index], array[first_index]
    if command == "multiply":
        first_index = int(command_string.split()[1])
        second_index = int(command_string.split()[2])
        multyplied = array[first_index] * array[second_index]
        array.pop(first_index)
        array.insert(first_index, multyplied)
    if command == "decrease":
        array = [x - 1 for x in array]

    command_string = input()

array_str = [str(element) for element in array]

print(", ".join(array_str))