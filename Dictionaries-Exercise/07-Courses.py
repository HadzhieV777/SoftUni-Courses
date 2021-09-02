# 07. Courses
data = input()

courses = {}

while not data == "end":
    course_name, registered_students = data.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(registered_students)

    data = input()

sorted_courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))

for course, student in sorted_courses.items():
    print(f"{course}: {len(courses[course])}")

    for student_name in sorted(student):
        print(f"-- {student_name}")