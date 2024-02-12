# class Calculator:
#     def __init__(self):
#         pass

#     def add(self, num1, num2):
#         return num1 + num2
    
#     def subtract(self, num1, num2):
#         return num1 - num2
    
#     def multiply(self, num1, num2):
#         return num1 * num2
    
#     def divide(self, num1, num2):
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Error: Division by zero."
        
# calc = Calculator()
# print("Addition:", calc.add(5, 3))
# print("Subtraction:", calc.subtract(8, 2))
# print("Multiplication:", calc.multiply(4, 6))
# print("Division:", calc.divide(10, 2))


#Problem - 2

# class Student:
#     def __init__(self,name, roll_no):
#         self.name = name
#         self.roll_no = roll_no

#     def display_student_details(self):
#         return f"Name: {self.name} \nRoll Number: {self.roll_no}"
    
# stu1 = Student("Shubhang", 51)
# print(stu1.display_student_details())


#problem - 3

# class Employee:
#     def __init__(self, name, empID, hours_per_week):
#         self.name = name
#         self.empID = empID
#         self.hours_per_week = hours_per_week
#         self.totalSalary = 0
    
#     def calculate_salary(self):
#         self.totalSalary = 500*self.hours_per_week
    
#     def display_Total_Salary(self):
#         return f'''Name: {self.name}
# Employee ID: {self.empID}
# Hours Worked per Week: {self.hours_per_week}
# Total Salary: {self.totalSalary}'''
    
# #Driver Code

# emp1 = Employee("Shubhang", "xyz123", 60)
# emp1.calculate_salary()
# print(emp1.display_Total_Salary())


#problem - 4

# class ToDo:
#     def __init__(self):
#         self.tasks = {}
#         self.counter = 0
#         self.str = ""
    
#     def add_Task(self, task, completion):
#         self.task = task
#         self.counter += 1
#         self.completion = completion
#         self.tasks[self.counter] = {"Task": self.task, "Completion": self.completion}

#     def mark_as_completed(self, number):
#         self.number = number
#         self.tasks[number]["Completion"] = True

#     def display_Tasks(self):
#         self.str = "----------------TASKS--------------\n"
#         for i in self.tasks:
#             self.str += str(i) + ". "
#             self.str += (self.tasks[i]["Task"])
#             self.str += ", Completed: " + str(self.tasks[i]["Completion"])
#             self.str += "\n"
            
#         return self.str
    
# #driver Code
# todo = ToDo()
# todo.add_Task("Add this to Task Dictionary", False)
# todo.add_Task("Second Task", False)
# todo.mark_as_completed(1)
# print(todo.display_Tasks())


#Problem - 5

# class car:
#     def __init__(self, model, color, rent_charges):
#         self.model = model
#         self.color = color
#         self.rent_charges = rent_charges

# class rental:
#     def __init__(self, car, hours):
#         self.car = car
#         self.hours = hours

#     def display_rent(self):
#         return f'''Model: {self.car.model}
# Color: {self.car.color}
# Total Rent: {self.car.rent_charges*self.hours}'''
    

# car1 = car("BMW M5", "Black", 500)
# rental = rental(car1, 24)
# print(rental.display_rent())


#problem - 6

# class BankAccount:
#     def __init__(self):
#         self.balance = 0
    
#     def deposit(self):
#         self.deposit = float(input("Enter the amount you want to add: "))
#         self.balance += self.deposit

#     def withdraw(self):
#         self.withdraw = float(input("Enter the amount you want to withdraw:"))
#         if (self.withdraw>self.balance):
#             print("Insufficient Funds")
#         else:
#             self.balance -= self.withdraw
#             print(f"Amount Withdrawn: {self.withdraw}")

#     def display_Balance(self):
#         return f"Balance: {self.balance}"

# ba1 = BankAccount()
# print(ba1.display_Balance())
# ba1.deposit()
# print(ba1.display_Balance())
# ba1.withdraw()
# print(ba1.display_Balance())


# problem - 7

# class Shape:
#     def __init__(self,l=0, b=0):
#         self.l = l
#         self.b = b
    
#     def display_square_area(self):
#         print(f"Sqaure Area: {self.l*self.l}")
    
#     def display_rectange_area(self):
#         print(f"Rectange Area: {self.l*self.b}")
    
#     def display_circle_area(self):
#         print(f"Circle Area: {3.14*self.l*self.l}")

# shape1 = Shape(4)
# shape1.display_square_area()
# shape1.display_circle_area()
# shape2 = Shape(3,4)
# shape2.display_rectange_area()



#problem - 8

# class Time:
#     def __init__(self):
#         self.seconds = 0
#         self.minutes = 0
#         self.hours = 0

#     def Hours_to_minutes(self, hours):
#         self.hours = hours
#         print(f"Time in Minutes: {self.hours*60}")

#     def Minutes_to_seconds(self, minutes):
#         self.minutes = minutes
#         print(f"Time in Minutes: {self.minutes*60}")
    
#     def Seconds_to_minutes(self, seconds):
#         self.seconds = seconds
#         print(f"Time in Seconds: {self.seconds/60}")

#     def Minutes_to_hours(self, minutes):
#         self.minutes = minutes
#         print(f"Time in Hours: {self.minutes/60}")

# time = Time()
# time.Hours_to_minutes(2)
# time.Minutes_to_hours(180)
# time.Seconds_to_minutes(120)
# time.Minutes_to_seconds(10)


# problem - 9

# import random
# class Dice:
#     def RollDie(self):
#         print(random.randint(1, 6))

# Dice = Dice()
# Dice.RollDie()


#problem -10

# class Book:
#     def __init__(self, title, author, availability):
#         self.title = title
#         self.author = author
#         self.availability = availability
    
# class Library:
#     def __init__(self):
#         self.books = []
#         self.counter = 0
#         self.str = ""
    
#     def add_Book(self, book):
#         self.books.append(book)
    
#     def borrow_book(self, number):
#         self.number = number-1
#         if self.books[self.number].availability == True:
#             self.books[self.number].availability = False
#             print("Book Borrowed")
#         else:
#             print("Sorry Book not available")

#     def return_book(self, number):
#         self.number = number - 1
#         self.books[self.number].availability = True
#         print("Book Returned")

#     def display_Books(self):
#         self.counter = 0
#         self.str = ""
#         for i in self.books:
#             self.counter += 1
#             self.str += str(self.counter) + ".\n"
#             self.str += "Title: " + i.title + "\n"
#             self.str += "Author: " + i.author + "\n"
#             self.str += "Availability: " + str(i.availability) + "\n\n"
#         return self.str

# #driver Code:
# Book1 = Book("The Power of Your Subconcious Mind", "Joseph Murphy", True)
# Book2 = Book("Ignited Minds", "Dr. APJ Abdul Kalam", True)
# library = Library()
# library.add_Book(Book1)
# library.add_Book(Book2)
# print(library.display_Books())
# library.borrow_book(2)
# print(library.display_Books())
# library.return_book(2)
# print(library.display_Books())
