import sys #Needed to exit the program.
'''
-------------------------------------------------------------------------------------------------------------------------------------------
Exercise 5: Days of the Month - 30 Marks
Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) 
to the number of days in each month.

Instructions:
Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
Input Handling: Ask the user to input the month number.
Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. 
For February, ask the user if the year is a leap year and adjust the number of days accordingly.
----------------------------------------------------------------------------------------------------------------------------------------------
'''

#Dictionary Containing the number of months as the key and the days as the values.
days_in_month={
    1:31, #January
    2:28, #February
    3:31, #March
    4:30, #April
    5:31, #May
    6:30, #June
    7:31, #July
    8:31, #August
    9:30, #September
    10:31, #October
    11:30, #November
    12:31 #December
}
while True: #Starts a loop until the user wants to leave. This gives a chance for the users to keep using the program until they want.
    print ("Type Exit if you wish to leave.")
    month = input("Enter the month number(1-12): ") #Stores the user's answer on which month they want.
    if month.casefold() == "exit".casefold(): #If the user wants to leave the program, they type in exit(not case sensitive).
        print("Goodbye!")
        sys.exit() #Exits the program
        
     
    if month.isdigit():
        month = int(month)
        if 1 <= month <= 12:
            #Suffix for the months because the first 3 months use a different suffix.
            if month == 1: #1st Month
                suffix = "st"
            elif month == 3: #3rd Month
                suffix ="rd"
            else: #4th month and above
                suffix = "th"
            if month == 2: #February
                #Checks if the month of February is a leap year or not.
                leap_year = input("Is it a Leap Year?(Yes/No)").casefold()
                if leap_year == "Yes".casefold(): #Case fold so the input is not case sensitive
                    print("The number of days in February is 29.") #If February is a leap year, its 29 days.
                elif leap_year == "No".casefold(): #Case fold so the input is not case sensitive
                    print("The number of days in February is 28.")# If February is not a leap year, its 28 days.
                else:
                    print("Invalid input, please type yes or no.") #Prints if there are any other inputs other than yes/ no.
            else:
                print(f"The number of days in the {month}{suffix} month is {days_in_month[month]} days.") #Prints the month and how many days are in that month.
        else:
            print("Invalid month number. Please enter a number between 1 and 12.") #If the input is higher than 12 or the months.
    else:
        print("Invalid input. Please enter a number.") #If there are any other inputs, it prints and tells the user to enter a number between 1-12.

