# 05. Palindrome Integers
def is_palindrome():
    list_of_number = input().split(", ")

    for element in list_of_number:
        if element == element[::-1]:
            is_true = True
            print(is_true)
        else:
            is_true = False
            print(is_true)


is_palindrome()