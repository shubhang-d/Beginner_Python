# car: maker, name , model , year, price
# dealership: inventory maintain karni hai, sell, flag generate karna hai, dealership ka naam , list of objects
# customer: Name, aadhar car, dl no., purchased car


class car:
    def __init__(self, maker, name, model, year, price, available):
        self.maker = maker
        self.name = name
        self.model = model
        self.year = year
        self.price = price
        self.available = available

    def display(self):
        return f'''maker = {self.maker}
name = {self.name}
model = {self.model}
year = {self.year}
price = {self.price}'''

class dealership():
    def __init__(self,name):
        self.name = name
        self.rcar = car
        self.inventory = []

    def add_car_to_inventory(self, car):
        self.inventory.append(car)
    
    def display_cars(self):
        count = 0
        for i in self.inventory:
            if i.available == True:
                count+=1
                print(f"Car {count}")
                print(f'''
{i.display()}''')
                
    def sell_car(self, c1, cnum):
        if 0<=cnum<=len(self.inventory) and len(self.inventory) -1 >= cnum:
            return self.inventory.pop(cnum-1)
                
    def noOfCarsSold(self):
        pass

class customer:
    def __init__(self, name, aadhaar, dl):
        self.name = name
        self.aadhaar = aadhaar
        self.dl = dl
        self.purchasedCar = []

    def display_customer_details(self):
        return '''
name: {self.name}
aadhaar: {self.aadhaar}
dl: {self.dl}
No. of Purchased Cars: {self.purchasedCar}'''

    def Purcahse_A_Car(self, car):
        self.purchasedCar.append(car)

car1 = car("BMW", "Competiton", "m3", 2017, 30000000, True)
car2 = car("Hyundai", "Creta", "KnightEdition", 2023, 1400000, True)
car3 = car("Tata", "Nano", "Zero", 2012, 114000, True)
deal = dealership('Varshney Motors')
deal.add_car_to_inventory(car1)
deal.add_car_to_inventory(car2)
deal.add_car_to_inventory(car3)
print(deal.display_cars())

cName = input("Enter the Customer Name: ")
cNum = int(input("Enter the car number you want to purchase"))
c1 = customer(cName, 546454475, 68678657657)
ret = deal.sell_car(c1, cNum)
if ret:
    print(f'{c1.name} purchased car \n {ret.display()}')
    print("----------cars available after purchasing is done-----------------")
    print(deal.display_cars())
    c1.Purcahse_A_Car(ret)
else:
    print('Car is not available')