"""
Напишете програма, реализираща класове базов клас SchoolMember,  и производни класове Teacher и Student, като всеки от тях има атрибути име и възраст.
Обекти от класа Teacher освен това съхраняват информация за заплатата си и списък от курсовете, които преподават.
Обекти от класа Student съхраняват информация за курсовете, които са записали, годината, в която е записан всеки всеки курс и списък с оценки за всеки курс.
Конструктурът на Teacher трябва да приема низ за име, години и заплата.
Пример:
    A=Teacher('Andonov',30,3000)
    Да са реализирани методите:
        getSalary(), който връща заплатата.
        addCourse(), който приема два параметъра - сигнатура и име на курс и ги добавя в речник с ключ сигнатурата и стойност името на курса
        getCourses(), който разпечатва всички курсове, по един на ред, първо сигнатурата, после интервал, после името.
        Контсруктурът на Student приема име и възраст.
        пример: B=Student('Petrov',21)
        Класът студент трябва да реализира следните методи:
            attendCourse, който приема сигнатура на курс и година и го добавя в речник с ключ сигнатурата и стойност друг речник, който съдържа ключове grades и year, и стойностите им са съответно списък с оценки и година на записване на курса.
            пример:
                attendCourse('CSCB101',2013)
                addGrade метод, който получава като параметри сигнатура и оценка и добавя оценката в съответния списък в речниковата стойност grades на курса с тази сигнатура. Методът извършва това само ако вече съществува курс с това име в речникът с курсове. В противен случай не прави нищо.
                Пример:
                    addGrade('CSCB101',3)
                    getCourses(), който разпечатва всички курсове, по един на ред, първо сигнатурата, после стойността като речник.
                    Пример:
                        CSCB101 {'grades': [], 'year': 2013} - преди добавяне на оценките с addGrade
                        CSCB101 {'grades': [3, 4], 'year': 2013} - след добавяне на две оценки
                        getAvgGrade() метод, който приема за входен параметър сигнатура на курс и връща средното аритметично за всичко оценки, съхранени в списъка с оценки.
                        Пример:
                            print(B.getAvgGrade('CSCB101')) разпечатва
                            3.5
                            След тестване на написаните от вас класове оставете основната програма празна. Нека няма никакви декларации на обекти от тези класове, нито приемане на параметри от командния ред, нито друг код в "главната програма".
"""


class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = {}

    def getSalary(self):
        return self.salary

    def addCourse(self, course_code, course_name):
        self.courses[course_code] = course_name

    def getCourses(self):
        for course_code, course_name in self.courses.items():
            print(f"{course_code} {course_name}")


class Student(SchoolMember):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = {}

    def attendCourse(self, course_code, year):
        self.courses[course_code] = {'grades': [], 'year': year}

    def addGrade(self, course_code, grade):
        if course_code in self.courses:
            self.courses[course_code]['grades'].append(grade)

    def getCourses(self):
        for course_code, details in self.courses.items():
            print(f"{course_code} {details}")

    def getAvgGrade(self, course_code):
        if course_code in self.courses and self.courses[course_code]['grades']:
            grades = self.courses[course_code]['grades']
            return sum(grades) / len(grades)
        return 0.0


# Тестови случаи
if __name__ == "__main__":
    # Създаване на обект Teacher
    teacher = Teacher('Andonov', 30, 3000)
    print("Print from getSalary: ", teacher.getSalary())
    teacher.addCourse('CSCB101', 'Introduction to Computer Science')
    teacher.addCourse('MATH123', 'Calculus I')
    print("Printing from getCourses:")
    teacher.getCourses()

    # Създаване на обект Student
    student = Student('Petrov', 21)
    student.attendCourse('CSCB101', 2013)
    print("before adding grades")
    student.getCourses()
    student.addGrade('CSCB101', 3)
    student.addGrade('NonExistant course', 2)
    student.addGrade('CSCB101', 4)
    student.attendCourse('MATH123', 2014)
    student.addGrade('MATH123', 5)
    print("Курсове на студента:")
    print("After adding grade")
    student.getCourses()
    print("Средна оценка по CSCB101:", student.getAvgGrade('CSCB101'))
    print("Средна оценка по MATH123:", student.getAvgGrade('MATH123'))
