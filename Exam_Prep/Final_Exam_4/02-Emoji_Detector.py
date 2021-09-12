# 02. Emoji Detector
import re

pattern = r"(?P<deli>\:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=deli)"
pattern_nums = r"\d"

cool_treshold = 1

data = input()

str_nums = re.findall(pattern_nums, data)
numbers = [int(el) for el in str_nums]
for number in numbers:
    cool_treshold *= number

emojis = re.finditer(pattern, data)
print(f"Cool threshold: {cool_treshold}")

emojis_to_print = []
emojis_count = 0

for match in emojis:
    emojis_count += 1
    emoji_data = match.groupdict()
    emoji = emoji_data['emoji']
    emoji_cool_bar = sum([ord(letter) for letter in emoji])

    if emoji_cool_bar >= cool_treshold:
        emojis_to_print.append(f"{emoji_data['deli']}{emoji_data['emoji']}{emoji_data['deli']}")


print(f"{emojis_count} emojis found in the text. The cool ones are:")
# print("\n".join(emojis_to_print))
for emoji in emojis_to_print:
    print(emoji)