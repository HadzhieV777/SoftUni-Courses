# 05. Emoticon Finder
text = input()

emojis = [f"{text[index]}{text[index + 1]}"
          for index in range(0, len(text))
          if text[index] == ":"
          ]

print("\n".join(emojis))