students_list = []
lecturer_list = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def stud_av_grade(self):
        stud_average_grade = 0
        for course, grade in self.grades.items():
            for mark in grade:
                stud_average_grade += mark
        result = stud_average_grade / len(grade)
        return result 
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не могу сравнивать с не студентами!')
            return
        return self.stud_av_grade() < other.stud_av_grade()    

    def __str__(self):
        res = (f'Имя: {self.name} \nФамилия: {self.surname}\n'
        f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\n'
        f'Средняя оценка за домашние задания: {self.stud_av_grade()} \nЗавершенные курсы: {" ".join(self.finished_courses)}')
        return res

    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname) 
        self.lecturer_grades = {}   
        lecturer_list.append(self)

    def av_grade(self):
        average_grade = 0
        for course, grades in self.lecturer_grades.items():
            for mark in grades:
                average_grade += mark
        result = average_grade / len(grades)
        return result
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не могу сравнивать с не лекторами!')
            return
        return self.av_grade() < other.av_grade()

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grade()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


def av_grade_per_course(course_name):
    student_av_grade = 0
    counter = 0
    for student in students_list:
        if course_name in student.courses_in_progress:
            student_av_grade += student.stud_av_grade()
            counter += 1 
        else:
            print("Нет оценок по данному курсу")
            return
    result = round(student_av_grade / counter, 2)
    print(f'Срудний бал за д/з по курсу {course_name} - {result}')
    return  

def av_lecturer_grade_per_course(course_name):
    lecturer_av_grade = 0
    counter = 0
    for lecturer in lecturer_list:
        if course_name in lecturer.courses_attached:
            lecturer_av_grade += lecturer.av_grade()
            counter += 1 
        else:
            print("Нет оценок по данному курсу")
            return
    result = round(lecturer_av_grade / counter, 2)
    print(f'Срудний бал за лекции по курсу {course_name} - {result}')
    return
    
# Тестирование работы классов и функций:

Oleg = Lecturer("Олег", "Булыгин")
Oleg.courses_attached += ['Python', 'Java']

Elena = Lecturer("Елена", "Никитина")
Elena.courses_attached += ['Python']

Alex = Reviewer("Александр","Бардин")
Alex.courses_attached += ['Python']

Phill = Reviewer("Филипп","Воронов")
Phill.courses_attached += ['Python']

Pavel = Student('Павел', 'Иванов', 'муж')
Pavel.courses_in_progress += ['Python']
Pavel.rate_lecturer(Oleg,'Python', 9)

Olga = Student('Ольга', 'Курочкина', 'жен')
Olga.courses_in_progress += ['Python']
Olga.rate_lecturer(Oleg,'Python', 10)

Maxim = Student('Максим', 'Прошутинский', 'муж')
Maxim.courses_in_progress += ['Python']
Maxim.rate_lecturer(Oleg,'Python', 5)
Maxim.rate_lecturer(Elena,'Python', 6)
Maxim.finished_courses += ['Основы языка программирования Python']

Alex.rate_hw(Pavel, 'Python', 8)
Alex.rate_hw(Olga, 'Python', 3)
Alex.rate_hw(Maxim, 'Python', 9)
Phill.rate_hw(Pavel, 'Python', 10)
Phill.rate_hw(Olga, 'Python', 5)
Phill.rate_hw(Maxim, 'Python', 5)

print(Oleg)
print()
print(Elena)
print()
print(Alex)
print()
print(Phill)
print()
print(Pavel)
print()
print(Olga)
print()
print(Maxim)
print()
print(Elena<Oleg)
print()
print(Maxim>Pavel)
print()
av_grade_per_course("Python")  
print()
av_lecturer_grade_per_course("Python")
print()
av_lecturer_grade_per_course("Java")