# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import random

#Written By Nathan Workman(Code Team), Edit made by Rachel with the if statement
#4-25-19

###Varaible Initialization###
Len=input("Enter the Length of the Room(In Feet), If you want to select a random length enter '-':")  #User-Input
Wid=input("Enter the Width of the Room(In Feet), If you want to select a random Width enter '-':")    #User-Input
i=0                             #Counter for x-axis from the numbers 0-Random number
j=0                             #Counter for y-axis from the numbers 0-Random number
indx=0                          #Counter for the index for the list in the x-axis 
indy=0                          #Counter for the index for the list in the y-axis
x = []                           #List for x-axis
y = []                           #List for y-axis

###If no number is entered, picks a random length and width (in Feet) for the room###
if Len == '-':
    Len=random.randint(1, 100)     #Selects a Random number from 1-100, Can be changed
elif  Wid == '-':
    Wid=random.randint(1, 100)      #Selects a Random number from 1-100, Can be changed
else:
    Len=int(Len)            #Converts length string to integer, Edit Made by Rachel 
    Wid=int(Wid)            #Converts width string to integer, Edit Made by Raachel 

###While Loop:Inserts the domain of x/y in their respected lists, this allows for them to be plotted###
while i != Len and j != Wid:            #While Loop while the counter for i and j doesnt equal the random width or length it will run
    x.insert(indx,i)                    #Puts the smallest value into the list of the x-axis
    y.insert(indy,j)                     #Puts the smallest value into the list of the y-axis
    i= i+1                                  #Increments the counter for i (x-axis)
    j= j+1                                  #Increments the counter for j (y-axis)
    indx=+ 1                                #Increments the counter for the  index of the list for x-axis
    indy=+ 1                                #Increments the counter for the  index of the list for y-axis

###Cleaning up the List(x/y)###
x.remove(0)                                 #The value of zero is added to the end of the list once looped is finished, so I just remove it to not mess up xaxis
y.remove(0)                                 ##The value of zero is added to the end of the list once looped is finished, so I just remove it to not mess up yaxis
xmax=len(x)                         #Gets the length of x , important for indexing later
ymax=len(y)                         #Gets the length of y, important for indexing later


###Graph/Room ###
plt.xlim(x[0],x[xmax-1])                                #Plots the x-axis(Domain)
plt.ylim(y[0],y[ymax-1])                                #Plots the y-axis(Range)
plt.gca().invert_xaxis()                        #When plotted the axis is flipped, so I need to reverse it to make it more logical(x-axis) 
plt.gca().invert_yaxis()                        #When plotted the axis is flipped, so I need to reverse it to make it more logical (y-axis)

###Two Randomly Placed People####

#Person1
Person1x= (np.random.uniform(x[0],x[xmax-1], size=1))           #Random x point for person 1
Person1y= (np.random.uniform(y[0],y[ymax-1], size=1))           #Random y point for person 1
plt.plot(Person1x,Person1y,marker='o', color="red")             #Plots Person 1 as red

#Person2
Person2x= (np.random.uniform(x[0],x[xmax-1], size=1))           #Random x point for person 2
Person2y= (np.random.uniform(y[0],y[ymax-1], size=1))           #Random y point for person 2
plt.plot(Person2x,Person2y,marker='o', color="blue")             #Plots Person 2 as blue
