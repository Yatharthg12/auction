import os,sys
import mysql, mysql.connector

def startScreen():
    #To clear the page
    os.system('clear')

    #Heading
    print("\n\n ----- Welcome, please select the screen you wish to visit ----- \n\n\n")

    #variable for screen options
    choice = input("  Login         Quit       \n")

    if choice.lower() in ["l", "login"]:
        loginScreen()

    else:
        print("Thank you for visiting")
        startScreen()



def loginScreen():
    #To clear the page
    os.system('clear')

    #Heading
    print("\n\n ----- Please login to enter the auction ----- \n\n\n")


    #Login Credentials
    reg_id = int(input("Please enter your registration id: "))
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    bid_no = int(input("Please enter your bidding number: "))

    #Login Criteria
    if reg_id in [1,2,3] and username in ["a","b","c"] and password in ["x","y","z"] and bid_no in [5,6,7]:
        auctionScreen()
    else:
        print("Wrong login credentials")     



def auctionScreen():
    #To clear the page
    os.system('clear')

    #Heading
    print("\n\n ----- Welcome to the auction ----- \n\n\n")
    
    #Bidding items
    item = input("Which item would you like to bid for(VPN, Browser Rights, Domain Name, AI chatbot, Humanoid Robot): ")

    #VPN BIDDING
    if item in ["VPN", "vpn", "Vpn"]:
        print("The starting bid for buying the vpn is 500 million")
        #Bid(start)
        bid =  int(input("Please give your bid(in whole numbers): "))
        if bid < 500000000:
            print("The starting bid is 500 million, you have been disqualified")
        else:
            comp_bid = print("The competing bid is:", bid+10000000)
            compete = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
            if compete.lower() == "back out":
                print("Thank you for your time, have a nice day!")
                startScreen()
            elif compete.lower() == "continue":
                #BID 1
                bid1 = int(input("Please enter your new bid(in whole numbers): "))
                if bid1 < 510000000:
                    print("The new bid limit is 510 million, you have been disqualified")
                else:
                    comp_bid1 = print("The competing bid is:",bid1+10000000)
                    compete1 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                    if compete1.lower() == "back out":
                        print("Thank you for your time, have a nice day!")
                        startScreen()
                    elif compete1.lower() == "continue":
                        #BID 2
                        bid2 = int(input("Please enter your new bid(in whole numbers): "))
                        if bid2 < 520000000:
                            print("The new bid limit is 520 million, you have been disqualified")
                        else:
                            comp_bid2 = print("The competing bid is:",bid2+10000000)
                            compete2 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                            if compete2.lower() == "back out":
                                print("Thank you for your time, have a nice day!")
                                startScreen()
                            elif compete2.lower() == "continue":
                                #BID 3
                                bid3 = int(input("Please enter your new bid(in whole numbers):"))
                                if bid3 < 530000000:
                                    print("The new bid limit is 530 million, you have been disqualified")
                                else:
                                    comp_bid3 = print("The competitor does not wish to continue")
                                    print("You have won the auction item, congratulations!!")

    #Brower Rights Bidding
    if item in ["Browser rights", "browser Rights", "browser rights", "Browser Rights"]:
        print("The starting bid for buying the browser rights is 300 million")
        #Bid(start)
        bid =  int(input("Please give your bid(in whole numbers): "))
        if bid < 300000000:
            print("The starting bid is 300 million, you have been disqualified")
        else:
            comp_bid = print("The competing bid is:", bid+10000000)
            compete = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
            if compete.lower() == "back out":
                print("Thank you for your time, have a nice day!")
                startScreen()
            elif compete.lower() == "continue":
                #BID 1
                bid1 = int(input("Please enter your new bid(in whole numbers): "))
                if bid1 < 310000000:
                    print("The new bid limit is 310 million, you have been disqualified")
                else:
                    comp_bid1 = print("The competing bid is:",bid1+10000000)
                    compete1 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                    if compete1.lower() == "back out":
                        print("Thank you for your time, have a nice day!")
                        startScreen()
                    elif compete1.lower() == "continue":
                        #BID 2
                        bid2 = int(input("Please enter your new bid(in whole numbers): "))
                        if bid2 < 320000000:
                            print("The new bid limit is 320 million, you have been disqualified")
                        else:
                            comp_bid2 = print("The competing bid is:",bid2+10000000)
                            compete2 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                            if compete2.lower() == "back out":
                                print("Thank you for your time, have a nice day!")
                                startScreen()
                            elif compete2.lower() == "continue":
                                #BID 3
                                bid3 = int(input("Please enter your new bid(in whole numbers):"))
                                if bid3 < 330000000:
                                    print("The new bid limit is 330 million, you have been disqualified")
                                else:
                                    comp_bid3 = print("The competing bid is:",bid3+10000000)
                                    compete3 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                                    if compete3.lower() == "back out":
                                        print("Thank you for your time, have a nice day!")
                                        startScreen()
                                    elif compete3.lower() == "continue":
                                        #BID 4
                                        bid4 = int(input("Please enter your new bid(in whole numbers):"))
                                        if bid4 < 340000000:
                                            print("The new bid limit is 340 million, you have been disqualified")
                                        else:
                                            comp_bid3 = print("The competitor does not wish to continue")
                                            print("You have won the auction item, congratulations!!")   

    #Domain Name Bidding
    if item in ["Domain name", "domain Name", "domain name", "Domain Name"]:
        print("The starting bid for buying the domain name is 50 million")
        #Bid(first)
        bid =  int(input("Please give your bid(in whole numbers): "))
        if bid < 50000000:
            print("The starting bid is 50 million, you have been disqualified")
        else:
            comp_bid = print("The competing bid is:", bid+10000000)
            compete = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
            if compete.lower() == "back out":
                print("Thank you for your time, have a nice day!")
                startScreen()
            elif compete.lower() == "continue":
                #BID 1
                bid1 = int(input("Please enter your new bid(in whole numbers): "))
                if bid1 < 60000000:
                    print("The new bid limit is 60 million, you have been disqualified")
                else:
                    comp_bid1 = print("The competing bid is:",bid1+10000000)
                    compete1 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                    if compete1.lower() == "back out":
                        print("Thank you for your time, have a nice day!")
                        startScreen()
                    elif compete1.lower() == "continue":
                        #BID 2
                        bid2 = int(input("Please enter your new bid(in whole numbers): "))
                        if bid2 < 70000000:
                            print("The new bid limit is 70 million, you have been disqualified")
                        else:
                            comp_bid2 = print("The competitor does not wish to continue")
                            print("You have won the auction item, congratulations!!")

    #AI Chatbot Bidding
    if item in ["AI chatbot", "ai chatbot", "Ai chatbot", "aI chatbot", "AI Chatbot", "AI ChatBot", "AI Chat Bot", "ai chat bot", "AI chat bot"]:
        print("The starting bid for buying the AI chatbot is 2 billion")
        #Bid(first)
        bid =  int(input("Please give your bid(in whole numbers): "))
        if bid < 2000000000:
            print("The starting bid is 2 billion, you have been disqualified")
        else:
            comp_bid = print("The competing bid is:", bid+100000000)
            compete = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
            if compete.lower() == "back out":
                print("Thank you for your time, have a nice day!")
                startScreen()
            elif compete.lower() == "continue":
                #BID 1
                bid1 = int(input("Please enter your new bid(in whole numbers): "))
                if bid1 < 2100000000:
                    print("The new bid limit is 2.1 billion, you have been disqualified")
                else:
                    comp_bid1 = print("The competing bid is:",bid1+100000000)
                    compete1 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                    if compete1.lower() == "back out":
                        print("Thank you for your time, have a nice day!")
                        startScreen()
                    elif compete1.lower() == "continue":
                        #BID 2
                        bid2 = int(input("Please enter your new bid(in whole numbers): "))
                        if bid2 < 2200000000:
                            print("The new bid limit is 2.2 billion, you have been disqualified")
                        else:
                            comp_bid2 = print("The competing bid is:",bid2+100000000)
                            compete2 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                            if compete2.lower() == "back out":
                                print("Thank you for your time, have a nice day!")
                                startScreen()
                            elif compete2.lower() == "continue":
                                #BID 3
                                bid3 = int(input("Please enter your new bid(in whole numbers):"))
                                if bid3 < 2300000000:
                                    print("The new bid limit is 2.3 billion, you have been disqualified")
                                else:
                                    comp_bid3 = print("The competing bid is:",bid3+100000000)
                                    compete3 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                                    if compete3.lower() == "back out":
                                        print("Thank you for your time, have a nice day!")
                                        startScreen()
                                    elif compete3.lower() == "continue":
                                        #BID 4
                                        bid4 = int(input("Please enter your new bid(in whole numbers):"))
                                        if bid4 < 2400000000:
                                            print("The new bid limit is 2.4 billion, you have been disqualified")
                                        else:
                                            comp_bid4 = print("The competing bid is:",bid4+100000000)
                                            compete4 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                                            if compete4.lower() == "back out":
                                                print("Thank you for your time, have a nice day!")
                                                startScreen()
                                            elif compete4.lower() == "continue":
                                                #BID 5
                                                bid5 = int(input("Please enter your new bid(in whole numbers):"))
                                                if bid5 < 2500000000:
                                                    print("The new bid limit is 2.5 billion, you have been disqualified")
                                                else:
                                                    comp_bid5 = print("The competing bid is:",bid5+100000000)
                                                    compete5 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                                                    if compete5.lower() == "back out":
                                                        print("Thank you for your time, have a nice day!")
                                                        startScreen()
                                                    elif compete5.lower() == "continue":
                                                        #BID 6
                                                        bid6 = int(input("Please enter your new bid(in whole numbers):"))
                                                        if bid6 < 2600000000:
                                                            print("The new bid limit is 2.6 billion, you have been disqualified")
                                                        else:
                                                            comp_bid6 = print("The competing bid is:",bid6+100000000)
                                                            compete6 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                                                            if compete6.lower() == "back out":
                                                                print("Thank you for your time, have a nice day!")
                                                                startScreen()
                                                            elif compete6.lower() == "continue":
                                                                #BID 7
                                                                bid7 = int(input("Please enter your new bid(in whole numbers):"))
                                                                if bid7 < 2700000000:
                                                                    print("The new bid limit is 2.7 billion, you have been disqualified")
                                                                else:
                                                                    comp_bid7 = print("The competitor does not wish to continue")
                                                                    print("You have won the auction item, congratulations!!")

    #Humanoid Robot Bidding
    if item in ["Humanoid Robot", "humanoid robot", "humanoid Robot", "Humanoid robot"]:
        print("The starting bid for buying the humanoid robot is 500 thousand")
        #Bid(start)
        bid =  int(input("Please give your bid(in whole numbers): "))
        if bid < 500000:
            print("The starting bid is 500 thousand, you have been disqualified")
        else:
            comp_bid = print("The competing bid is:", bid+100000)
            compete = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
            if compete.lower() == "back out":
                print("Thank you for your time, have a nice day!")
                startScreen()
            elif compete.lower() == "continue":
                #BID 1
                bid1 = int(input("Please enter your new bid(in whole numbers): "))
                if bid1 < 600000:
                    print("The new bid limit is 600 thousand, you have been disqualified")
                else:
                    comp_bid1 = print("The competing bid is:",bid1+100000)
                    compete1 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                    if compete1.lower() == "back out":
                        print("Thank you for your time, have a nice day!")
                        startScreen()
                    elif compete1.lower() == "continue":
                        #BID 2
                        bid2 = int(input("Please enter your new bid(in whole numbers): "))
                        if bid2 < 700000:
                            print("The new bid limit is 700 thousand, you have been disqualified")
                        else:
                            comp_bid2 = print("The competing bid is:",bid2+100000)
                            compete2 = input(print("Would you like to continue bidding or back out(type 'continue' or 'back out'): "))
                            if compete2.lower() == "back out":
                                print("Thank you for your time, have a nice day!")
                                startScreen()
                            elif compete2.lower() == "continue":
                                #BID 3
                                bid3 = int(input("Please enter your new bid(in whole numbers):"))
                                if bid3 < 800000:
                                    print("The new bid limit is 800 thousand, you have been disqualified")
                                else:
                                    comp_bid3 = print("The competitor does not wish to continue")
                                    print("You have won the auction item, congratulations!!")


startScreen()