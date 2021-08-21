# 09. Factorial Division
def str_to_list(first_num, second_num):
    first_num_list = []
    second_num_list = []

    for number in range(1, first_num + 1):
        first_num_list.append(number)
    for number in range(1, second_num + 1):
        second_num_list.append(number)

    firs_list_to_set = set(first_num_list)
    second_list_to_set = set(second_num_list)
    difference_between_lists = firs_list_to_set.difference(second_list_to_set)


    def multiplyList():
        result = 1
        for x in difference_between_lists:
            result = result * x
        print(f"{result:.2f}")

    multiplyList()


first_number = int(input())
second_number = int(input())

str_to_list(first_number, second_number)