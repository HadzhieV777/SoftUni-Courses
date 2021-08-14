# 04. Sum of Chars
n = int(input())
single_element = 0

for i in range(0, n):
    single_element += ord(input())
print(f"The sum equals: {single_element}")