# 02. Character Multiplier
data = input().split()

first_word = data[0]
second_word = data[1]

smaller_word = min(len(first_word), len(second_word))
total_sum = 0

for index in range(smaller_word):
    total_sum += (ord(first_word[index]) * ord(second_word[index]))

bigger_word = first_word

if len(second_word) > len(first_word):
    bigger_word = second_word

for i in range(smaller_word, len(bigger_word)):
    total_sum += ord(bigger_word[i])

print(total_sum)