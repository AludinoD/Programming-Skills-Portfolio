import sys #Needed to exit the program.
'''
---------------------------------------------------------------------------------------------------------------------------------------
Exercise 7: Some Counting - 20 Marks
Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console in each case.

Write a loop that counts up from 0 to 50 in increments of 1.
Write a loop that counts down from 50 to 0 in decrements of 1.
Write a loop that counts up from 30 to 50 in increments of 1.
Write a loop that counts down from 50 to 10 in decrements of 2.
Write a loop that counts up from 100 to 200 in increments of 5. You may include all loops in a single project
---------------------------------------------------------------------------------------------------------------------------------------
'''


print ("Loops")
print ("Choose what loop you want to run")
while True: #Runs a loop so that the user can keep using the program until they want.
    while True: # A loop for checking the user's input. It will keep running until the condition is met. This checks if the user input is numbers between 1-5 and not strings.
        user_loop = (input("1. 0 to 50 in increments of 1\n2. 50 to 0 in decrements of 1.\n3. 30 to 50 in increments of 1\n4. 50 to 10 in decrements of 2.\n5. 100 to 200 in increments of 5.\nType Exit if you wish to leave.\nLoop Number: "))
        if user_loop.casefold() == "exit".casefold(): #Makes the "exit" word not case sensitive
            sys.exit() #Exits the program
    #Checks if the user loop is a digit and not a string.
        if user_loop.isdigit():
            break #Breaks out of the loop.
        
        print("Invalid input, please put numbers between 1-5.") #If any other inputs were used, the loop will keep running until the condition is met.
    #Loops can work as (Starting number, Ending Number, increments/decrements)
    #First Loop(1.)
    if user_loop == "1":
        print("0-50 in increments of 1.")
        for a in range(0, 51, 1):
            print (a)
    #Second Loop(2.)
    elif user_loop == "2":
        print("50-0 in decrements of 1.")
        for b in range(50, -1, -1):
            print (b)
    #Third Loop(3.)
    elif user_loop == "3":
        print ("30-50 in increments of 1.")
        for c in range(30, 51, 1):
            print (c)
    #Fourth Loop(4.)
    elif user_loop == "4":
        print ("50-10 in decrements of 2.")
        for d in range(50, 9, -2 ):
            print (d)
    #Fifth Loop(5.)
    elif user_loop == "5":
        print ("100-200 in increments of 5.")
        for e in range(100, 201, 5):
            print (e)
    #Any other inputs will make this code run.            
    else:
        print ("Invalid number, please enter a number between 1-5.")
