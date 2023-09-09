#Importing all libraries
import os
#import pandas as pd 
#import numpy as np 
#import time, datetime
import math, random




#Defining Global Variables





#Connecting the project with mysql







#Login Screen
def login():

    os.system('clear')


    print("\n\n\nWelcome to the auction management system!\n\n\n")
    login_id = input("Enter your login id: ")
    password = input("Enter your password: ")
    
    if login_id == "a" or "b" and password == "c" or "d":
        print("Hello\n\n")
        print("What item would you like to bid on?")
    else:
        print("Wrong login id or password")





login()


#Main Screen where auction will happen
def auctionSystem():

    #Items for auctioning
    item_1, item_2, item_3, item_4, item_5 = "choice 1", "choice 2", "choice 3", "choice 4", "choice 5"

    print("\n",item_1 ,"\n", item_2,"\n", item_3,"\n",item_4,"\n",item_5)

    chosen_item = int(input("Please enter the item you would like to bid on (1,2,3,4,5): "))    #Item chosen by user


    #Starting the auction

    #Item 1
    if chosen_item == "1":
        print("The starting bid for", chosen_item, "is:")

    










    #Item 2
    if chosen_item == "2":
        print("The starting bid for", chosen_item, "is:")









    #Item 3
    if chosen_item == "1":
        print("The starting bid for", chosen_item, "is:")













    #Item 4
    if chosen_item == "1":
        print("The starting bid for", chosen_item, "is:")
















    #Item 5
    if chosen_item == "1":
        print("The starting bid for", chosen_item, "is:")


















auctionSystem()

