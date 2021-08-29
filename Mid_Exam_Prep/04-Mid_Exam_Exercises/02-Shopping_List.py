# 02. Shopping List
groceries_list = [el for el in input().split("!")]
command_types = input()


def check_item_exist(items_list, item_searched):
    return True if item_searched in items_list else False


while not command_types == "Go Shopping!":
    command = command_types.split()[0]
    if command == "Urgent":
        item = command_types.split()[1]
        if not check_item_exist(groceries_list, item):
            groceries_list.insert(0, item)

    elif command == "Unnecessary":
        item = command_types.split()[1]
        if check_item_exist(groceries_list, item):
            groceries_list.remove(item)

    elif command == "Correct":
        old_item = command_types.split()[1]
        new_item = command_types.split()[2]
        if check_item_exist(groceries_list, old_item):
            current_index = groceries_list.index(old_item)
            groceries_list[current_index] = new_item

    elif command == "Rearrange":
        item = command_types.split()[1]
        if check_item_exist(groceries_list, item):
            groceries_list.remove(item)
            groceries_list.append(item)

    command_types = input()

print(", ".join(groceries_list))