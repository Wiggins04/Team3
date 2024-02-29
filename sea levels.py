print ("Welcome")

def option_a():
    print("Enter dates for average calculation")
    dates = input("")
    #code for algorithm a goes here
    

def option_b():
    print("Enter dates for average calculation")
    dates = input("")
    #code for algoithm b goes here
    

def option_c():
    print("Enter dates for average calculation")
    dates = input("")
    #code for algorithm c goes here

def mainMenu():
    print ("Select an option")
    print ("-1 OPTION A") # Replace this name later on with the function provided
    print ("-2 OPTION B") # Replace this name later on with the function provided
    print ("-3 OPTION C") # Replace this name later on with the function provided
    #Any extra options should be entered here
    print ("-4 Quit")
    while True:
        selection = input("")
        if selection == "1":
            option_a()
            break
        elif selection == "2":
            option_b()
            break
        elif selection == "3":
            option_c()
            break
        elif selection == "4":
            return
        else:
            print("Please select a valid option")
mainMenu()#calling the main menu



