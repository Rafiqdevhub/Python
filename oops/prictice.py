class Student:
     # Constructor (initializes attributes)
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
    
# Method (behavior)
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

# Create objects (instances) from the class
s1= Student("Tim", 19, 95)
s2= Student("Bill", 19, 75)
s3= Student("Jill", 19, 65)

# Use the objects
# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.get_average_grade())

# print(s1.name)

# Inheritance
class Pet:  # Base class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I don't know what I say")

class Cat(Pet): # Derived class
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color= color
    def speak(self):
        print("Meow")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
        
class Dog(Pet): # Derived class
    def speak(self):
        print("Bark")

# p = Pet("Tim", 19)
# p.show()
# p.speak()

d= Dog("Bill", 34)
d.show()
d.speak()

# c= Cat("Bill", 34, "Brown")
# c.show()
# c.speak()