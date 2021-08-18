# 09. Hello, France
list = input().split("|")
budget = float(input())
needed_money = 150

new_price_list = []
profit = 0
new_budget = 0

for position in list:
    list_info = position.split("->")
    item = list_info[0]
    purchasing_price = float(list_info[1])
    if (item == "Clothes") and (purchasing_price <= 50.00) and (budget >= purchasing_price):
        sale_price = (purchasing_price * 1.4)
        new_budget += sale_price
        new_price_list.append(sale_price)
        budget -= purchasing_price
        profit += sale_price - purchasing_price
    elif (item == "Shoes") and (purchasing_price <= 35.00) and (budget >= purchasing_price):
        sale_price = (purchasing_price * 1.4)
        new_budget += sale_price
        new_price_list.append(sale_price)
        budget -= purchasing_price
        profit += sale_price - purchasing_price
    elif (item == "Accessories") and (purchasing_price <= 20.50) and (budget >= purchasing_price):
        sale_price = (purchasing_price * 1.4)
        new_budget += sale_price
        new_price_list.append(sale_price)
        budget -= purchasing_price
        profit += sale_price - purchasing_price

if (budget + new_budget) >= needed_money:
    for el in new_price_list:
        print(f"{el:.2f}", end=' ')
    print(f"\nProfit: {profit:.2f}")
    print("Hello, France!")
else:
    for el in new_price_list:
        print(f"{el:.2f}", end=' ')
    print(f"\nProfit: {profit:.2f}")
    print(f"Time to go.")
