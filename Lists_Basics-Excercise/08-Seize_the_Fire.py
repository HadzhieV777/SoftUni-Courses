# 08. Seize the Fire
fires_with_cells = [el for el in input().split("#")]
water = int(input())
total_effort = 0
total_fire = 0
valid_cells = []

for i in range(len(fires_with_cells)):
    fires_with_cells[i] = str(fires_with_cells[i]).split(" = ")

for el in fires_with_cells:
    type_of_fire = str(el[0])
    cell = int(el[1])
    if water < cell:
        continue
    if type_of_fire == "High" and 81 <= cell <= 125:
        water -= cell
        total_effort += (cell * 0.25)
        total_fire += cell
        valid_cells.append(cell)
    elif type_of_fire == "Medium" and 51 <= cell <= 80:
        water -= cell
        total_effort += (cell * 0.25)
        total_fire += cell
        valid_cells.append(cell)
    elif type_of_fire == "Low" and 1 <= cell <= 50:
        water -= cell
        total_effort += (cell * 0.25)
        total_fire += cell
        valid_cells.append(cell)

print("Cells:")
for cells in valid_cells:
    print(f" - {cells}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire:.0f}")