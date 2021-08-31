# 02. A Miner Task
resources = input()
dictionary = {}

while not resources == "stop":
    quantity = int(input())

    if resources not in dictionary:
        dictionary[resources] = quantity
    else:
        dictionary[resources] += quantity

    resources = input()

for key, value in dictionary.items():
    print(f"{key} -> {value}")