# 03. Inventory
list_of_items = [el for el in input().split(", ")]
commands_string = input()

while not commands_string == "Craft!":
    command = commands_string.split()[0]


    if command == "Collect":
        item = commands_string.split()[2]
        if item not in list_of_items:
            list_of_items.append(item)

    if command == "Drop":
        item = commands_string.split()[2]
        if item in list_of_items:
            list_of_items.remove(item)

    if command == "Combine":
        item = commands_string.split(":")[0]
        old_item = item.split(" ")[3]
        new_item = commands_string.split(":")[1]
        if old_item in list_of_items:
            index_old_item = list_of_items.index(old_item)
            index_new_item = index_old_item + 1
            list_of_items.insert(index_new_item, new_item)

    if command == "Renew":
        item = commands_string.split()[2]
        if item in list_of_items:
            list_of_items.remove(item)
            list_of_items.append(item)

    commands_string = input()

print(", ".join(list_of_items))