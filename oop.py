class Person:
    def setDetails(self, name, salary):
        self.n = name
        self.s = salary
    
    def getDetails(self):
        print(f"{self.n} has {self.s}")

emp1 = Person()
emp1.setDetails("Ravi", 1234)
emp1.getDetails()