# 04. Odd and Even Sum
def odd_and_even_numbs():
    user_input = input()
    is_even = 0
    is_odd = 0
    single_elements = list(map(int, user_input))

    for element in single_elements:
        if element % 2 == 0:
            is_even += element
        else:
            is_odd += element
    print(f"Odd sum = {is_odd}, Even sum = {is_even}")


odd_and_even_numbs()