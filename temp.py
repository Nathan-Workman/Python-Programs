# -------------------------------------------------------------------------------
# Name: Nathan Workman
# Date:   3/26/19
# Assignment:  Project 3 - Autoshop Selection
# Description:   Calculate an invoice for automotive services using a while loop.
# -------------------------------------------------------------------------------
from setup_messagebox import *
service1=''         #Initializing The varaible service1
service2=''         #Initializing The varaible service2
service3=''         #Initializing The varaible service3
service4=''          #Initializing The varaible service4
Menu = ''           #Initializing The varaible Menu
Cost = ''           #Initializing The varaible Cost
tax =''             #Initializing The varaible tax
grandtotal =''      #Initializing The varaible grandtotal

print("Hello! Welcome to AutoParts! Please look at the menu and choose the services needed by typing the number beside the given service")      #Prints welcome message and instructions for selection
print("There is also a 6% tax on all services.")                        #Reminds User that there is a 6% tax on all services
print('1.Oil Change - $35\n2.Tire Rotation - $19\n3.Car Wash - $7\n4.Car Wax - $12')        #prints services menu for selection
Menu = {'1':35,'2':19,'3':7,'4':12,'-':0}       #Creates a dictionary of the menu, pairs the price to the serivce
servicenames = {'1':'Oil Change','2':'Tire Rotation','3':'Car Wash','4':'Car Wax','-':'Nothing'}      #Assigns an easier list for the user to follow to what the service is
service1 = input('Service 1: ')             #Gets input from user user for first service selection
service2= input('Service 2: (If no second service is needed just enter ‘-‘)')    #Gets input from  user for second service selection
service3= input('Service 3: (If no Third service is needed just enter ‘-‘)')    #Gets input from  user for Third service selection
service4= input('Service 4: (If no Fourth service is needed just enter ‘-‘)')    #Gets input from  user for Fourth service selection

while service1 not in Menu or service2 not in Menu or service3 not in Menu or service4 not in Menu:      #While loop to check user input, if something bad is entered it loops until correct
    print("This is not a selection, please pick again.")
    if service1 not in Menu:                   #If-statement to check each inputed service and if wrong it gets a new input
        service1 = input('Service 1: ')  # Gets input from user user for first service selection
    elif service2 not in Menu:       #If-statement to check each inputed service and if wrong it gets a new input
        service2 = input('Service 2: (If no second service is needed just enter ‘-‘)')  # Gets input from  user for second service selection
    elif service3 not in Menu:            #If-statement to check each inputed service and if wrong it gets a new input
        service3= input('Service 3: (If no second service is needed just enter ‘-‘)')    #Gets input from  user for Third service selection
    elif service4 not in Menu:             #If-statement to check each inputed service and if wrong it gets a new input
        service4= input('Service 4: (If no second service is needed just enter ‘-‘)')    #Gets input from  user for Fourth service selection
    else:
         print("This is not a selection.")

Cost = Menu[service1] + Menu[service2] + Menu[service3] + Menu[service4] # Adds the paired prices together from the services located in the Dictionary
tax = Cost * .06  # Calculates the tax based on the price from the two services combined
grandtotal = Cost + tax  # Gets a grand total by adding the cost of the two services and the tax together
def recp():
    print("\n****Here is your automated invoice for todays vist****")  # Prints here is your invoice for today
    print("Selected Service 1: %s  at $%d" % (servicenames[service1],Menu[service1]))  # Prints the service selected and the price of that service
    print('Selected Service 2: %s at $%d' % (servicenames[service2],Menu[service2]))  # Prints the  second service selected and the price of that service
    print('Selected Service 3: %s at $%d' % (servicenames[service3],Menu[service3]))  # Prints the  Third service selected and the price of that service
    print('Selected Service 4: %s at $%d' % (servicenames[service4],Menu[service4]))  # Prints the  Fourth service selected and the price of that service
    print("Tax: $%s" % (tax))  # Prints the curent tax on those services combined
    print("Grand Total: $%s" % (grandtotal))  # Prints grandtotal of the whole vist
    print('****Thank you for your vist! Come Again!****')

messagebox.showinfo(recp())




