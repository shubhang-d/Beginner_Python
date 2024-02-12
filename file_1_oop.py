# class Shape:
#     def __init__(self, side1, side2):
#         self.side1 = side1
#         self.side2 = side2

#     def area(self):
#         return self.side1*self.side2
#     def peri(self):
#         return 2*(self.side1+self.side2)

# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         super().__init__(length, breadth)


# class Square(Shape):
#     def __init__(self, side):
#         super().__init__(side, side)

    
    
# rec1 = Rectangle(2,3)
# sq1 = Square(2)
# print(rec1.area())
# print(sq1.area())


# class Student:
#     def __init__(self):
#         self.name = "NA"
#         self.age = "NA"
#         self.gender = "NA"
#     def setDetails(self, name,  age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def getdetails(self):
#         return f'''Name: {self.name}
# Age: {self.age}
# Grade: {self.grade}'''
#     def calc_grade(self, marks_perc):
#         if marks_perc>=90:
#             return "O"
#         elif marks_perc>=80 and marks_perc<90:
#             return "A+"
#         elif marks_perc>=70 and marks_perc<80:
#             return "A"
#         elif marks_perc>=60 and marks_perc<70:
#             return "B+"
#         elif marks_perc>=50 and marks_perc<60:
#             return "B"
#         elif marks_perc>=40 and marks_perc<50:
#             return "C"
    

# stu1 = Student()
# stu2 = Student()
# stu1.setDetails("Shubhang", 18, "A+")
# stu2.setDetails("Utkarsh", 19, 'B')
# print(stu1.getdetails())
# print(stu2.getdetails())

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def getDetails(self):
        return f'''Name: {self.name}
Species: {self.species}
Age: {self.species}'''
    
class Lion:
    def __init(self,name , species, age):
        super().__init__(name, species, age)

class Elephant:
    def __init(self,name , species, age):
        super().__init__(name, species, age)

class Giraffe:
    def __init(self,name , species, age):
        super().__init__(name, species, age)