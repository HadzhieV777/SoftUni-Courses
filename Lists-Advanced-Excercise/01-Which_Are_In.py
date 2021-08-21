# 01. Which Are In?
firs_line_string_input = [str(el) for el in input().split(", ")]
second_line_string_input = [str(el) for el in input().split(", ")]
if_true = []

for j in range(len(firs_line_string_input)):
    for i in range(len(second_line_string_input)):
        if firs_line_string_input[j] in second_line_string_input[i]:
            if not firs_line_string_input[j] in if_true:
                if_true.append(firs_line_string_input[j])
print(if_true)