# 07. Water Overflow
num_of_lines = int(input())
tank_capacity = 255
capacity = 0

for i in range(0, num_of_lines):
    liters = int(input())
    if (capacity + liters) <= tank_capacity:
        capacity += liters
    else:
        print("Insufficient capacity!")
print(capacity)