class Person:
    def person_info(self, name, age):
        self.name = name
        self.age = age

class Student:
    def student_info(self, roll, mark):
        self.roll = roll
        self.mark = mark

class EngineeringStudent(Person, Student):
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll)
        print("Mark:", self.mark)

# object creation
e1 = EngineeringStudent()

# calling parent class methods
e1.person_info("prangya", 20)
e1.student_info(101, 85)

# display
e1.show() 