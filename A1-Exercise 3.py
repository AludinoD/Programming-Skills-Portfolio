'''
--------------------------------------------------------------------------------------------------------------------------------------------
Exercise 3: Biography

In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.
Steps:
Store the information (name, hometown, and age) as key-value pairs in a dictionary.
Print the values on separate lines using a single print() statement.
Use variables with appropriate data types for each piece of information.
--------------------------------------------------------------------------------------------------------------------------------------------
'''
#Dictionaries are used to store data in key:value pairs and uses curly brackets to store the values.

dict = {
    "name1": "Deniz", #Data for the name
    "hometown1" : "Philippines", #Data for the hometown
    "age1" : 17 #Data for age
}
print (f"Name:{dict['name1']}\nHometown:{dict['hometown1']}\nAge:{dict['age1']}")
'''
---------------------------------------------------------------------------
Print is used to print the dictionary with the given values
f string is used to evaluate the expressions inside the curly braces {}
dict[' '] is used to access the values inside the dictionary
/n is used to create a new line 
---------------------------------------------------------------------------
'''

'''
-----------------------------------------------------------------------------------------------------------------------------------
Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values. 
Try giving both your first and second name when asked for your name. 
What happens? How can you handle multiple words in Python? Test the program by entering a string value for age (e.g., "twenty"). 
What happens? How can you prevent this issue?
-----------------------------------------------------------------------------------------------------------------------------------
'''

print ("|---------------------------------------|")
print ("Advanced Requirement")

#Gets user inputs and puts them into a variable
name2 = input("Enter your Full Name:")
hometown2 = input("Enter your Hometown:")

while True: #loops until the given condition is met
    age2 = input("Enter your age:") #Gets the age input from user
    if age2.isdigit(): #Checks if the input from the user is a digit
        break #If the condition is met, it exits the loop


    print("Please enter a VALID NUMBER") #If the user input is not a digit, it will print this message.

#This is where the variables are saved.
user_bio = {
    "name2" : name2, #Stores the name 
    "hometown2" : hometown2, #Stores the hometown
    "age2" : age2 #Stores the Age
}

print (f"Name: {user_bio['name2']}\nHomeTown: {user_bio['hometown2']}\nAge: {user_bio['age2']}")
#Prints the users inputs saved in the dictionary(users_bio)