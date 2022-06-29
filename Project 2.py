# -------------------------------------------------------------------------------
# Name: Nathan Workman
# Date:   3/12/19
# Assignment:  Project 2 - Autoshop Selection
# Description:   Calculate an invoice for automotive services.
# -------------------------------------------------------------------------------
service1=''         #Initializing The varaible service1
service2=''         #Initializing The varaible service2
Menu = ''           #Initializing The varaible Menu
Cost = ''           #Initializing The varaible Cost
tax =''             #Initializing The varaible tax
grandtotal =''      #Initializing The varaible grandtotal

print("Hello! Welcome to AutoParts! Please look at the menu and choose the services needed by typing the number beside the given service")      #Prints welcome message and instructions for selection
print("There is also a 6% tax on all services.")                        #Reminds User that there is a 6% tax on all services
print('1.Oil Change - $35\n2.Tire Rotation - $19\n3.Car Wash - $7\n4.Car Wax - $12')        #prints services menu for selection
Menu = {'1':35,'2':19,'3':7,'4':12,'-':0}       #Creates a dictionary of the menu, pairs the price to the serivce
servicenames = {'1':'Oil Change','2':'Tire Rotation','3':'Car Wash','4':'Car Wax','-':'None'}      #Assigns an easier list for the user to follow to what the service is
service1 = input('Service 1: ')             #Gets input from user user for first service selection
service2= input('Service 2: (If no second service is needed just enter ‘-‘)')    #Gets input from  user for second service selection
if service1 in Menu and service2 in Menu:          #If statement to ensure right values are entered
    Cost = Menu[service1] + Menu[service2]  # Adds the paired prices together from the services located in the Dictionary
    tax = Cost * .06  # Calculates the tax based on the price from the two services combined
    grandtotal = Cost + tax  # Gets a grand total by adding the cost of the two services and the tax together
    print("Here is your automated invoice for todays vist")  # Prints here is your invoice for today
    print("Service 1:", servicenames[service1], '$', Menu[service1])  # Prints the service selected and the price of that service
    print('Service 2:', servicenames[service2], '$',Menu[service2])  # Prints the  second service selected and the price of that service
    print("Tax:", '$', tax)  # Prints the curent tac on those services combined
    print("Grand Total:", '$', grandtotal)  # Prints grandtotal of the whole vist
    print('Thank you for your vist! Come Again!')
elif service1 not in Menu:                    #If-statement, if what is inputed isnt on the menu(Dictionary) then prints, this is not a selection
    print("This is not a selection")
elif service2 == '-':       #If no second service is wanted and '-' is entered then it assignes the value of none a price of zero, allows for just one service to be selected
    service2 = 'None'
elif service2 not in Menu:  # If-statement, if what is inputed isnt on the menu(Dictionary) then prints, this is not a selection
        print('This is not a selection')
else:
    print('This is not a selection')     #Else just prints not a selection
