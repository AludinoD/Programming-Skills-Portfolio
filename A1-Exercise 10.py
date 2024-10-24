'''
--------------------------------------------------------------------------------------------------
Exercise 10: Is it even? - 35 Marks
Write a program that tests if a value is even or odd. Follow the instructions outlined below:

Instructions:
The program should ask the user for a number from within the main function.
The entered number should be passed to a function that determines if the value is even or odd.
The function should return a message indicating whether the number is even or odd.
The message returned by the function should be printed from within the main function.
--------------------------------------------------------------------------------------------------
'''
import sys# Needed to exit the program

print("Even or Odd?.") 

#Defines the function for checking even or odd
def even_or_odd(num):
    if num % 2 == 0: #If the user's number is divided by 2 and is equal to 0, its an even.
        return "The number is even."
    else:
        return "The number is odd." #Otherwise, its odd

# Defines the main function
def main():
    while True: #Runs a loop so that the user can keep using the program until they put exit.
        print("Type exit if you wish to leave.")
        user_input = input("Please enter a NUMBER: ")  #Asks the user for a number or if they want to exit.

        #Makes "exit" not case-sensitive
        if user_input.casefold() == "exit".casefold():
            print("Goodbye!")
            sys.exit() #Exits the program.

        #Checks if the input is a valid number
        if user_input.isdigit():
            num = int(user_input)  # Converts the input to an integer

            #Call the even_or_odd function and print the result
            result = even_or_odd(num)
            print(result)

        else:
            print("Please enter a valid NUMBER or type exit to leave.") #If any other input is given, the loop will continue until they put a valid number.

#Calls the main function
if __name__ == "__main__":
    main()



