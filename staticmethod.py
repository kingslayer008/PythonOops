class Student:
    school_name = "Cit"

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def show_marks(self):
        print(self.m1, self.m2)

    @classmethod
    def show_school(cls):
        print(cls.school_name)

    @staticmethod
    def show_static():
        print("This is a static method")


s1 = Student(20, 30)
s1.show_marks()
Student.show_school()
Student.show_static()
