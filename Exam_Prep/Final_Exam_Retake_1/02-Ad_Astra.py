# 02. Ad Astra
import re

pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2,2}/\d{2,2}/\d{2,2})\1(\d{1,5})\1'

data = input()

sum_of_calories = 0
all_the_products = []

for match in re.finditer(pattern, data):
    product = match.group(2)
    expiration_date = match.group(3)
    calories = int(match.group(4))
    all_the_products.append([product, expiration_date, calories])
    sum_of_calories += calories

days_to_survive = sum_of_calories // 2000
print(f"You have food to last you for: {days_to_survive} days!")

for product_info in all_the_products:
    print(f"Item: {product_info[0]}, Best before: {product_info[1]}, Nutrition: {product_info[2]}")
