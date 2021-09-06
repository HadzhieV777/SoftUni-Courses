# 08. Letters Change Numbers
alphabet = {chr(el + 97): el + 1 for el in range(26)}

data = input().split()
sum_of_all = 0

for el in data:
    first_letter = el[0]
    last_letter = el[-1]
    number = int(el[1:-1])

    if first_letter.isupper():
        number /= alphabet[first_letter.lower()]
    elif first_letter.islower():
        number *= alphabet[first_letter]

    if last_letter.isupper():
        number -= alphabet[last_letter.lower()]
    elif last_letter.islower():
        number += alphabet[last_letter]

    sum_of_all += number

print(f"{sum_of_all:.2f}")