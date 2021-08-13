# 09. Easter Cozonacs
budget = float(input())
flour_kilo_price = float(input())
colored_eggs = 0
cozonacs_count = 0

egg_price = flour_kilo_price * 0.75
liter_milk_price = flour_kilo_price * 1.25
milk_for_one_cozonac = liter_milk_price * 0.25
cozonac_price = flour_kilo_price + egg_price + milk_for_one_cozonac

while budget - cozonac_price > 0:
    budget -= cozonac_price
    colored_eggs += 3
    cozonacs_count += 1
    if cozonacs_count % 3 == 0:
        colored_eggs -= cozonacs_count - 2
print(f"You made {cozonacs_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
