# 05. Print Part of the ASCII Table
first_character = int(input())
last_character = int(input())

for i in range(first_character - 1, last_character):
    i += 1
    if i != [-1]:
        print(chr(i), end=' ')
    else:
        print(chr(i), end='')