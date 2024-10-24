import sys
'''
----------------------------------------------------------------------------------------------------------------------------------
Exercise 8: Simple Search - 30 Marks
Write a program that searches for a specific string within a list of strings. The list is initialized with specific names 
("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

Optional Requirements:
Allow the user to input the search term instead of using a predefined value.
Implement the search functionality based on user input.
----------------------------------------------------------------------------------------------------------------------------------
'''
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #List for names
search = "Sam" #Person were looking for.
print(names)

if search in names: #Checks if the person were looking for is inside the list.
    print (f"{search} is in the names list.") #If the person is inside the list.
else:
    print (f"{search} is not found in the names list.") #If the person isn't in the list.

print("Do you want to keep using the program?")#Asks the user if they want to proceed with the program.
while True:#Starts a loop and waits for the user's input.
    adv_mode= input("Yes or No:")#Stores the answer.
    if adv_mode.casefold() == "Yes".casefold():#If the user says yes, the program continues.
        print (
    '''
|---------------------------|
|    Advanced Requirement   |
|---------------------------|
    '''
)
        break #Breaks out of the loop and continues the program

    elif adv_mode.casefold() == "No".casefold():#If the user says No, the program closes
        print ("Goodbye!")#Prints a goodbye message for them
        sys.exit()#Exits the program

user_search = input("Who are you looking for?").casefold() #Asks the user for who they want to look for, and is not case sensitive.
if user_search in [name.casefold() for name in names]: # Looks for the users input inside the list.
    print (f"{user_search} is in the names list.")
else:
    print (f"{user_search} is not found in the names list.")
