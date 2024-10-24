'''
---------------------------------------------------------------------------------------------------------
Exercise 6: Brute Force Attack - 30 Marks
Write a program that simulates a password entry system. The correct password is defined as 12345.
The program should keep asking the user to enter the password until they provide the correct one.

Basic Requirements:
Define the correct password.
Use a while loop to repeatedly ask the user for the password until the correct one is entered.
Output an appropriate message when the correct password is entered.
Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password,
inform them of the remaining attempts. If the maximum number of attempts is reached, 
inform the user that the authorities have been alerted.
---------------------------------------------------------------------------------------------------------
'''
name = input ("Username:") 
print("You have 5 attempts.")
correct_pass = "12345" #Correct Password
attempts = 5 #5 Attempts


while attempts > 0: #Lets the user continue the loop/program until they have more than 0 attempts.
    user_pass = input("Please enter the password: ")
    
    if user_pass == correct_pass: #If the user's input matches the correct password, it runs this code.
        print("Access Granted! Welcome", name) #Grants the user an access.
        break #Breaks out of the loop.
    else: #If the user input doesn't match the correct password, it runs this code.
        attempts -= 1 #Reduces the amount of attempts.
        if attempts > 0: # If the attempts is less than 0, it runs this code.
            print(f"Incorrect password. You have {attempts} attempts left before the authorities are alerted.") #Informs the user that the password they gave is wrong and provides them with the remaining attempts.
        else:
            print("Incorrect password. The authorities have been alerted.") #If the user reaches the amount of attempts possible, it prints this message.

