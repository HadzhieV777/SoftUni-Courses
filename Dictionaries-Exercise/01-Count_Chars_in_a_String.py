# 01. Count Chars in a String
str_input = map(str, input())
dictionary = {}

for char in str_input:
    if char not in dictionary:
        dictionary[char] = 0
    dictionary[char] += 1

for key, value in dictionary.items():
    if not key == " ":
        print(f"{key} -> {value}")
