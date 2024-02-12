noi = int(input("How many Items you want to add?"))
dct = {}
for i in range(noi):
    item = input("Enter the name of the item you want to add?")
    Quantity = input("Enter the quantity of the item you want to add?")
    dct[item] = Quantity

print("Item".ljust(30), "Quantity")
print()
for i in dct:
    print(f"{i.ljust(30)} {dct[i]}")