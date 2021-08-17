# 02. Multiples List
factor = int(input())
count = int(input())
list_size = factor * count
outp_list = []

for number in range(1, list_size + 1):
    if number % factor == 0:
        outp_list.append(number)
print(outp_list)