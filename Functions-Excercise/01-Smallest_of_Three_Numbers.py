# 01. Smallest of Three Numbers
one = int(input())
two = int(input())
three = int(input())


def compare_numbers(a, b, c):
    if a < b and a < c:
        return a
    if b < a and b < c:
        return b
    if c < a and c < b:
        return c


print(compare_numbers(one, two, three))