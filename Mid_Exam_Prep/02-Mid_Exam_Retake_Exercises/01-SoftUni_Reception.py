# 01. SoftUni Reception
first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())

students_count = int(input())
hours_counter = 0

emplyees_efficiency_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

while students_count > 0:
    students_count -= emplyees_efficiency_per_hour
    hours_counter += 1
    if hours_counter % 4 == 0:
        hours_counter += 1
print(f"Time needed: {hours_counter}h.")