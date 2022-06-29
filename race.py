itemName = ""
itemPrice = ""
itemQuantity = ""
totalPrice =""
totalPrice1=""
totalPrice2 = ""
itemName2 = ""
itemPrice2 = ""
itemQuantity2 =""
gratuity =""

itemName = input('Enter food item name:\n')
itemPrice = float(input('Enter item price:\n'))
itemQuantity = int(input('Enter item quantity:\n'))
totalPrice1 = (itemPrice * itemQuantity)

print("RECEIPT")
print(itemQuantity, itemName, "@ $", itemPrice, "=", "$",totalPrice1)
print("Total cost: $",totalPrice1)
print("\n")
itemName2 = input('Enter second food item name:\n')
itemPrice2 = float(input('Enter item price:\n'))
itemQuantity2 = int(input('Enter item quantity:\n'))
totalPrice2 = (itemPrice2 * itemQuantity2)
totalPrice = totalPrice1 + totalPrice2
gratuity = (totalPrice * .15)
print("\n")
print("RECEIPT")
print(itemQuantity, itemName, "@ $", itemPrice, "=", "$", totalPrice1)
print(itemQuantity2, itemName2, "@ $", itemPrice2, "=", "$", totalPrice2)
print("Total cost: $", totalPrice)
print("\n")
print("15% gratuity:",gratuity )
print("Total with tip: $", gratuity + totalPrice)
