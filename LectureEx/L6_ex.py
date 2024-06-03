class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Branch_Manager(SchoolMember):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.branch_leader_of = []

    def add_branch(self, branch):
        self.branch_leader_of.append(branch)

    def __str__(self):
        return f"Branch Manager: {super().__str__()}, Salary: {self.salary}, Brach: {', '.join(self.branch_leader_of)}"


class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"Teacher: {super().__str__()}, Salary: {self.salary}, Courses: {', '.join(self.courses)}"


class Student(SchoolMember):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = {}

    def enroll_course(self, course, year):
        if course not in self.courses:
            self.courses[course] = {'year': year, 'grades': []}

    def add_grade(self, course, grade):
        if course in self.courses and 2 <= grade <= 6:
            self.courses[course]['grades'].append(grade)

    def __str__(self):
        course_info = []
        for course, details in self.courses.items():
            grades = ', '.join(map(str, details['grades']))
            course_info.append(f"{course} (Year: {details['year']}, Grades: {grades})")
        return f"Student: {super().__str__()}, Courses: {'; '.join(course_info)}"


# Tests
teacher = Teacher("Petar Ivanov", 13, 2000)
teacher.add_course("Smoking METH")
teacher.add_course("Chemistry")
teacher.add_course("Selling Crack")
print(teacher)

student = Student("Penka Georgieva", 23)
student.enroll_course("Smoking METH", 2021)
student.add_grade("Smoking METH", 3)
student.add_grade("Smoking METH", 2)
student.enroll_course("Chemistry", 2020)
student.add_grade("Chemistry", 4)
student.add_grade("Chemistry", 3)
print(student)

student2 = Student("Ivan Ivanov", 27)
student2.enroll_course("Selling Crack", 1983)
student2.add_grade("Selling Crack", 6)
print(student2)
print("That boy be slanging rock!!")

branch_manager = Branch_Manager("Walter White", 53, 20000000)
branch_manager.add_branch("Cooking METH")
branch_manager.add_branch("Teaching Jessy")
branch_manager.add_branch("Killing rivals")
branch_manager.add_branch("Being the one who knocks")
print(branch_manager)
