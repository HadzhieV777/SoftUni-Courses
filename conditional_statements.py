# 01. Jenny Secret Message
# user_name = input()
#
# if user_name == "Johnny":
#     print("Hello, my love!")
# else:
#     print(f"Hello, {user_name}!")


# 02.  Drink Something
# age_control = int(input())
# drinks = ""
#
# if age_control <= 14:
#     drinks = "toddy"
# elif age_control <= 18:
#     drinks = "coke"
# elif age_control <= 21:
#     drinks = "beer"
# elif age_control > 21:
#     drinks = "whisky"
# else:
#     pass
#
# print(f"drink {drinks}")


# 03. Leonardo DiCaprio Oscars
# integer = int(input())
# string = ""
#
# if integer == 88:
#     string = "Leo finally won the Oscar! Leo is happy"
# elif integer == 86:
#     string = "Not even for Wolf of Wall Street?!"
# elif integer < 88 and integer != 86:
#      string = "When will you give Leo an Oscar?"
# elif integer > 88:
#      string = "Leo got one already!"
#
# print(string)

# 04. Double Char
# string = input()
#
# for char in string:
#    print(char * 2, end="")


# 05. Can't Sleep? Count Sheep
# number = int(input())
#
# i = 1
# while ( i <= number):
#     print (str(i) + " sheep...", end = '')
#     i = i + 1


# 06. Next Happy Year
# current_year = int(input())
#
# while True:
#     current_year += 1
#     current_year_str = str(current_year)
#     if len(current_year_str) == len(set(current_year_str)):
#         print(current_year_str)
#         break


# 07. Maximum Multiple
# divisor = int(input())
# bound = int(input())
# max_multiplier = 0
#
# for current_number in range(divisor + 1, bound + 1):
#     if current_number % divisor == 0:
#         max_multiplier = current_number
# print(max_multiplier)

# 08. Mutate String
# first_string = input()
# second_string = input()
# last_string = first_string
#
# for symbol in range(len(first_string)):
#     left_part = second_string[:symbol + 1]
#     right_part = first_string[symbol + 1:]
#     current_string = left_part + right_part
#     if current_string == last_string:
#         continue
#     print(current_string)
#     last_string = current_string

# 09. Easter Cozonacs
# budget = float(input())
# flour_kilo_price = float(input())
# colored_eggs = 0
# cozonacs_count = 0
#
# egg_price = flour_kilo_price * 0.75
# liter_milk_price = flour_kilo_price * 1.25
# milk_for_one_cozonac = liter_milk_price * 0.25
# cozonac_price = flour_kilo_price + egg_price + milk_for_one_cozonac
#
# while budget - cozonac_price > 0:
#     budget -= cozonac_price
#     colored_eggs += 3
#     cozonacs_count += 1
#     if cozonacs_count % 3 == 0:
#         colored_eggs -= cozonacs_count - 2
# print(f"You made {cozonacs_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


# 10. Christmas Spirit
# allowed_quantity = int(input())
# days_left = int(input())
# total_spirit = 0
# total_sum = 0
#
# ornament_set_price = 2
# tree_skirt_price = 5
# tree_garlands_price = 3
# tree_lights_price = 15
#
# for current_day in range(1, days_left+1):
#     if current_day % 11 == 0:
#         allowed_quantity += 2
#     if current_day % 2 == 0:
#         total_sum += allowed_quantity * ornament_set_price
#         total_spirit += 5
#     if current_day % 3 == 0:
#         total_sum += (tree_skirt_price + tree_garlands_price) * allowed_quantity
#         total_spirit += 13
#     if current_day % 5 == 0:
#         total_sum += tree_lights_price * allowed_quantity
#         total_spirit += 17
#         if current_day % 3 == 0:
#             total_spirit += 30
#     if current_day % 10 == 0:
#         total_spirit -= 20
#         total_sum += tree_skirt_price + tree_garlands_price + tree_lights_price
# if days_left % 10 == 0:
#     total_spirit -= 30
# print(f"Total cost: {total_sum}")
# print(f"Total spirit: {total_spirit}")

