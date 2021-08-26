# 03. Memory Game
sequence_of_elements = input().split()
count_moves = 0
command = input()
while not command == "end":
    count_moves += 1
    index1 = int(command.split()[0])
    index2 = int(command.split()[1])
    if index1 == index2 or index1 < 0 or index2
        sequence_of_elements.insert(int(len(sequ
        sequence_of_elements.insert(int(len(sequ
        print("Invalid input! Adding additional
    elif sequence_of_elements[index1] == sequenc
        print(f"Congrats! You have found matchin
        x = sequence_of_elements.pop(index1)
        sequence_of_elements.remove(x)
    elif sequence_of_elements[index1] != sequenc
        print("Try again!")
    if len(sequence_of_elements) == 0:
        print(f"You have won in {count_moves} tu
        break
    command = input()
if command == "end":
    print("Sorry you lose :(\n"                 
          f"{' '.join(sequence_of_elements)}")