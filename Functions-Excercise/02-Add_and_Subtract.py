# 02. Add and Subtract
one = int(input())
two = int(input())
three = int(input())

sum_one_and_two = lambda a, b: a + b
sum_numbers = sum_one_and_two(one, two)

subtract_num = lambda a, b: a - b
subtract = subtract_num(sum_numbers, three)

print(subtract)