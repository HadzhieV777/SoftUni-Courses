# 11. SoftUni Exam Results
students_info = input()

students_dict = {}
langs = {}

while not students_info == "exam finished":
    username = students_info.split("-")[0]

    if students_info.split("-")[1] == "banned":
        students_dict.pop(username)
    else:
        language = students_info.split("-")[1]
        points = int(students_info.split("-")[2])
        if language not in langs.keys():  # count the languages
            langs[language] = 1
        else:
            langs[language] += 1
        if username not in students_dict:
            students_dict[username] = {'language': language, 'points': points}
        else:
            if students_dict[username]['points'] < points:
                students_dict[username]['points'] = points
    students_info = input()
print("Results:")
for key, value in sorted(students_dict.items(), key=lambda x: (-x[1]['points'], x[0])):
    if key:
        print(f"{key} | {value['points']}")
print('Submissions:')
for lan, num in sorted(langs.items(), key=lambda x: (-x[1], x[0])):
    print(f"{lan} - {num}")
