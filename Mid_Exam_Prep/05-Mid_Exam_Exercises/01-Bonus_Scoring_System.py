# 01. Bonus Scoring System
import math

students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

max_bonus = 0
max_bonus_attendances = 0

if lectures_count > 0 and students_count > 0:
    for student in range(students_count):
        attendances = int(input())
        total_bonus = attendances / lectures_count * (5 + additional_bonus)
        if total_bonus >= max_bonus:
            max_bonus = total_bonus
            max_bonus_attendances = attendances

print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {max_bonus_attendances} lectures.')