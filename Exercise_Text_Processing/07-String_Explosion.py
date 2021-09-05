# 07. String Explosion
data = input()
total_strength = 0

i = 0
while i < len(data):
    if data[i] == ">":
        strength_of_explosion = int(data[i + 1])
        total_strength += strength_of_explosion
    else:
        # abv>1>1>2>2asdasd
        if total_strength > 0:
            data = data[:i] + data[i + 1:]
            i -= 1
            total_strength -= 1

    i += 1

print(data)