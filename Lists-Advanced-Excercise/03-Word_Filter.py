# 03. Word Filter with list comperhention
string_input = [el for el in input().split() if len(el) % 2 == 0]
print("\n".join(string_input))