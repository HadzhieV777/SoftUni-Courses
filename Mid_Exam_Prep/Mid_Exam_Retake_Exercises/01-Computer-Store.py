# 01. Computer Store
prices = input()
total_price = 0

while not (prices == "special" or prices == "regular"):
    current_price = float(prices)
    if current_price <= 0:
        print("Invalid price!")
    else:
        total_price += current_price
    prices = input()

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    taxes = total_price * 0.2
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    total = total_price + taxes
    if prices == "special":
        total -= total * 0.1
    print(f"Total price: {total:.2f}$")