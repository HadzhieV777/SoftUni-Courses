# 01. National Court
def court_system(first, second, third, count, time):
    answer_per_hour = first + second + third

    while count > 0:
        count -= answer_per_hour
        time += 1
        if time % 4 == 0:
            time += 1
    return f"Time needed: {time}h."


first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())

people_count = int(input())
needed_time = 0

print(court_system(first_employee_efficiency,
                   second_employee_efficiency,
                   third_employee_efficiency,
                   people_count,
                   needed_time
))