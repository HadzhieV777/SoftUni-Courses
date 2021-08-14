# 03. Elevator
num_of_people = int(input())
capacity = int(input())
courses = 0

while num_of_people > 0:
    num_of_people -= capacity
    courses += 1
print(courses)