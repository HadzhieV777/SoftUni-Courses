# 04. Number Beggars
string_input = [int(el) for el in input().split(", ")]
beggars_count = int(input())
beggars = []

for i in range(beggars_count):
    beggars.append(0)

index = 0


for number in string_input:
    beggars[index] += number
    index += 1

    if index == beggars_count:
        index = 0
print(beggars)