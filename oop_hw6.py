class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        self.average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка: {self.average_grade()}\nКурсы в процессе: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nАвтор курсов: {self.courses_attached} '
        return res

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rate(self):
        self.average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_rate() < other.average_rate()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self.average_rate()} '
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def grade_av_student(student_list, course):
    sum = 0
    count = 0
    for person in student_list:
        for i in person.grades[course]:
            sum += i
            count += 1
    return round(sum / count, 1)

def grade_av_lecturer(lecturer_list, course):
    sum = 0
    count = 0
    for person in lecturer_list:
        for i in person.grades1[course]:
            sum += i
            count += 1
    return round(sum / count, 1)


Kate_student = Student('Каte', 'Petrova', 'female')
Roma_student = Student('Roma', 'Ivanov', 'Male')
Kate_student.finished_courses += ['Java']
Kate_student.courses_in_progress += ['Python', 'Git']
Roma_student.finished_courses += ['Java', 'Git']
Roma_student.courses_in_progress += ['Python']

Anna_mentor = Mentor('Anna', 'Sirotina')
Nata_mentor = Mentor('Nata', 'Dobry')

Sasha_lecturer = Lecturer('Sasha', 'Belyi')
Ulia_lecturer = Lecturer('Ulia', 'Vlasova')
Sasha_lecturer.courses_attached += ['Python', 'Git']
Ulia_lecturer.courses_attached += ['Python', 'Git']

Irina_reviewer = Reviewer('Irina', 'Volkova')
Olga_reviewer = Reviewer('Olga', 'Katina')
Irina_reviewer.courses_attached += ['Python', 'Git']
Olga_reviewer.courses_attached += ['Python', 'Git']

Kate_student.rate_lecturer(Sasha_lecturer, 'Python', 10)
Kate_student.rate_lecturer(Ulia_lecturer, 'Phython', 9)
Roma_student.rate_lecturer(Ulia_lecturer, 'Python', 8)
Kate_student.rate_lecturer(Ulia_lecturer, 'Python', 7)
Roma_student.rate_lecturer(Ulia_lecturer, 'Python', 6)

Irina_reviewer.rate_hw(Kate_student, 'Python', 6)
Irina_reviewer.rate_hw(Roma_student, 'Python', 7)
Irina_reviewer.rate_hw(Kate_student, 'Python', 8)
Olga_reviewer.rate_hw(Kate_student, 'Python', 9)
Olga_reviewer.rate_hw(Roma_student, 'Python', 9)
Olga_reviewer.rate_hw(Kate_student, 'Git', 10)
print('_' * 10)
Kate_student.average_grade()
Roma_student.average_grade()
print('Студенты:')
print(Kate_student)
print(Roma_student)
print('Лучшая успеваемость:')
print(f'{Roma_student.surname if Kate_student < Roma_student else Kate_student.surname}')


print('_' * 10)
Sasha_lecturer.average_rate()
Ulia_lecturer.average_rate()
print(Sasha_lecturer < Ulia_lecturer)
print(Sasha_lecturer)
print(Ulia_lecturer)
print(Irina_reviewer)
print(Olga_reviewer)

lecturer_list = [Sasha_lecturer, Ulia_lecturer]
student_list = [Kate_student, Roma_student]
course = 'Python'
print('_' * 10)
print('Средняя оценка студентов по курсу', course)
print(grade_av_student(student_list, course))

print('Средняя оценка лекторов по курсу', course)
print(grade_av_student(student_list, course))