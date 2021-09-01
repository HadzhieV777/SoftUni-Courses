# 04. Legendary Farming with Functions
def material_filter(material_name, material_quantity, items_dict):
    if material_name in items_dict:
        items_dict[material_name] += material_quantity
    else:
        items_dict[material_name] = 0
        items_dict[material_name] += material_quantity


legendary_item = ""
key_items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}

while legendary_item == "":
    materials = input().split()

    for index in range(0, len(materials), 2):
        quantity = int(materials[index])
        material = materials[index + 1].lower()

        if material == "shards":
            material_filter(material, quantity, key_items)

        elif material == "fragments":
            material_filter(material, quantity, key_items)

        elif material == "motes":
            material_filter(material, quantity, key_items)

        else:
            material_filter(material, quantity, junk_items)

        if material == "shards" and key_items[material] >= 250:
            key_items[material] -= 250
            legendary_item = "Shadowmourne"
            break

        elif material == "fragments" and key_items[material] >= 250:
            key_items[material] -= 250
            legendary_item = "Valanyr"
            break

        elif material == "motes" and key_items[material] >= 250:
            key_items[material] -= 250
            legendary_item = "Dragonwrath"
            break

print(f"{legendary_item} obtained!")

for item, qty in sorted(key_items.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{item}: {qty}")

for jun, junk_qty in sorted(junk_items.items(), key=lambda kvp: kvp[0]):
    print(f"{jun}: {junk_qty}")
