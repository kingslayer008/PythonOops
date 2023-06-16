class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 4

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Dinesh', 22)
s2 = Student('Gokul', 22)
s1.show()
s2.show()

# To create object outside class
lap1 = Student.Laptop()
lap1.show()
