# 03. Find Occurrences of Word in Sentence
import re

data = input()
searched_word = input()

pattern = f"\\b{searched_word}\\b"

word_count = []

match = re.findall(pattern, data, re.IGNORECASE)

for el in match:
    word_count.append(el)
print(len(word_count))