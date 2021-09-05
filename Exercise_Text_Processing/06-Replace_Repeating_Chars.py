# 06. Replace Repeating Chars
text = input()

index = 0
while index < len(text) - 1:
    if text[index] == text[index + 1]:
        pair = f"{text[index]}{text[index + 1]}"
        text = text.replace(pair, text[index])
        index = 0
    else:
        index += 1
print(text)