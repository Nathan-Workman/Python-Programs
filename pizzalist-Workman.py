# -------------------------------------------------------------------------------
# Name: Nathan Workman
# Date:   4/18/18
# Assignment:  Project 9 - Pizza Ordering using three synchronized lists.
# Description:   Calculate Pizza order total using Python Lists - no if/elif/else required unless error handling.
# -------------------------------------------------------------------------------
from setup_messagebox import *
size_of_pizza = 0
amount_of_pizzas = 0
price_of_pizza = 0


menu = ['a','b','c','d']
size =  ['small','medium','large', 'extra large']
prices = [7.99,14.99,18.99,06.02]

print("Let me help you order a pizza", "by Nathan Workman")
print("What size would you like?")
print("a. small ($7.99) b. medium ($14.99) c. large ($18.99) d. extra-large ($06.02)")

pick = (input("Please enter a,b, c or d:"))
list_location = menu.index(pick)
size_of_pizza = size[list_location]
price_of_pizza = prices[list_location]
print("Ok,", size_of_pizza,",that is $",price_of_pizza,"each")
amount_of_pizzas =  int(input("How many would you like?"))

print("The cost is:", amount_of_pizzas * price_of_pizza)
messagebox.showinfo("Order Total",amount_of_pizzas * price_of_pizza)


print( "End of Project 9 by Nathan Workman")