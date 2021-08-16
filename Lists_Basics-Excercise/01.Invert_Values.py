# 01. Invert Values
n = input()
n_list = n.split()
negative_list = []

for element in n_list:
    negative_el = int(element) * -1
    negative_list.append(negative_el)
print(negative_list)