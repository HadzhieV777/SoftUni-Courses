# 02.  Drink Something
age_control = int(input())
drinks = ""

if age_control <= 14:
    drinks = "toddy"
elif age_control <= 18:
    drinks = "coke"
elif age_control <= 21:
    drinks = "beer"
elif age_control > 21:
    drinks = "whisky"
else:
    pass

print(f"drink {drinks}")