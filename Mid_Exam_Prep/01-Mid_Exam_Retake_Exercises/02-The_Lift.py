# 02. The Lift
number_of_waiting_people = int(input())
lift = [int(el) for el in input().split()]
MAX_SEATS_PER_WAGON = 4

for index in range(len(lift)):
    while not lift[index] == MAX_SEATS_PER_
        if number_of_waiting_people > 0:
            lift[index] += 1
            number_of_waiting_people -= 1
        else:
            break

all_seats = len(lift) * MAX_SEATS_PER_WAGON
taken_seats = sum(lift)
if number_of_waiting_people == 0 and taken_
    print("The lift has empty spots!")
elif number_of_waiting_people > 0 and taken
    print(f"There isn't enough space! {numb
print(' '.join([str(el) for el in lift]))