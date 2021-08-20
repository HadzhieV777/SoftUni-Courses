# 07. Perfetct Number
def is_perfect_number(number: int):
    divisors = []
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors.append(divisor)
    return True if sum(divisors) == number else False


n = int(input())
print("We have a perfect number!" if is_perfect_number(n) else "It's not so perfect.")