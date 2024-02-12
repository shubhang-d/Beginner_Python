usr_dmnd ={}
availableItems = {1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}}

def display_available_items(dct):
	print("\t\t\t Available Items:")
	print()
	print("S.No.\t\t Item \t\t Quantity \t\t Cost/Item")
	for i in dct:
		    print(f"{str(i).ljust(16)} {dct[i]['Item'].ljust(15)} {str(dct[i]['Quantity']).ljust(23)} {str(dct[i]['Cost/Item'])}")
	

def add_items():
    noi = int(input("How many Items you want to add?"))
    for i in range(noi):
        item = input("Enter the name of the item you want to add?")
        Quantity = int(input("Enter the quantity of the item you want to add?"))
        usr_dmnd[item] = Quantity


def display_cart():
    tcost = 0
    for i in usr_dmnd:
         for j in availableItems:
                if i == availableItems[j]["Item"]:
                     if usr_dmnd[i] <= availableItems[j]["Quantity"]:
                            print("Item Available")
                            tcost += usr_dmnd[i] * availableItems[j]["Cost/Item"]
                     else:
                         print("Quantity Not Availale")
                else:
                    print("Item not Available")
    print(tcost)

add_items()
display_cart()
# display_available_items(usr_dmnd)