# 05. Class
class Class:
    __student_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < Class.__student_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        grade = self.get_average_grade()
        result = f"The students in {self.name}: " \
                 f"{', '.join(self.students)}. " \
                 f"Average grade: {grade:.2f}"
        return result
