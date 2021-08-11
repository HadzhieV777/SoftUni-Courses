# 03. Leonardo DiCaprio Oscars
integer = int(input())
string = ""

if integer == 88:
    string = "Leo finally won the Oscar! Leo is happy"
elif integer == 86:
    string = "Not even for Wolf of Wall Street?!"
elif integer < 88 and integer != 86:
     string = "When will you give Leo an Oscar?"
elif integer > 88:
     string = "Leo got one already!"

print(string)
