import sys #Needed to exit the program.
'''
----------------------------------------------------------------------------------------------------------------------------------------
Exercise 4: Primitive Quiz - 30 Marks

In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

Steps:
Write a program that asks the user "What is the capital of France?" and waits for their response.
If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
If the answer is incorrect, the program should print a message saying the answer is wrong.
------------------------------------------------------------------------------------------------------------------------------------------
'''


print ("Primitive Quiz!! ")
while True: # Uses a While loop to give the users a chance to keep retrying until they get the right answer.
    ans = input("What is the capital of France?(Case sensitive)") #Stores the answer.
    if ans == 'Paris':#Checks the answer and is case sensitive. If the answer isn't with a capitalized P, it's considered wrong.
        print ("Correct!")#Prints Correct
        break# If the answer is right, it breaks out of the loop.

    print ("Wrong. Please Try Again.") #Prints if the answer is wrong.


'''
-------------------------------------------------------------------------------------------------------------
Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization 
(e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. 
Provide feedback for each question.
-------------------------------------------------------------------------------------------------------------
'''

print ("Do you want to proceed to the advanced mode?")#Asks the user if they want to proceed to the advanced questions.
while True: #Starts a loop and waits until the given condition is met.
    adv_mode= input("Yes or No:") #Stores the answer.
    if adv_mode.casefold() == "Yes".casefold(): #If the user says yes, the program continues.
        print ( #Header
    '''
|---------------------------|
|    Advanced Requirement   |
|---------------------------|
    '''
)
        break #Breaks out of the loop and continues the program

    elif adv_mode.casefold() == "No".casefold(): #If the user says No, the program closes
        print ("Goodbye!") #Prints a goodbye message for them
        sys.exit() #Exits the program

    print ("Please answer using Yes or No.") #If any other inputs were used.

capitals = ["Berlin", "Brussels", "Warsaw", "Copenhagen", "Budapest", "Lisbon", "Prague", "Athens", "Sofia", "Nicosia"]#All capitals are written in a list.

score = 0 #Stores the score of the user if they get the answer right.

print ("There are 10 European countries, and you have to guess their capitals.")
print ("You will only be given once chance to answer.\nYou get 1 point for each correct answer.\nGoodluck!")

#The countries are the variables.
germa = input("What is the capital of Germany?") #Germany
if germa.casefold() == capitals[0].casefold():
    print ("Good job! It's correct!")
    score+=1
else:
    print ("Sorry, the correct answer is Berlin. ")

belg = input("What is the capital of Belgium?") #Belgium
if belg.casefold() == capitals[1].casefold():
    print ("Good job! It's correct!")
    score+=1
else:
    print ("Sorry, the correct answer is Brussels. ")
    
pola = input("What is the capital of Poland?") #Poland
if pola.casefold() == capitals[2].casefold():
    print ("Good job! It's correct!")
    score+=1
else:
    print ("Sorry, the correct answer is Warsaw. ")

den = input("What is the capital of Denmark?") #Denmark
if den.casefold() == capitals[3].casefold():
    print ("Good job! It's correct!")
    score+=1
else:
    print ("Sorry, the correct answer is Copenhagen. ")

hung = input("What is the capital of Hungary?") #Hungary
if hung.casefold() == capitals[4].casefold():
    print ("Good job! It's correct!")
    score+=1
else:
    print ("Sorry, the correct answer is Budapest. ")

port = input("What is the capital of Portugal?") #Portugal
if port.casefold() == capitals[5].casefold():
    print ("Good job! It's correct!")
    score+=1
else:
    print ("Sorry, the correct answer is Lisbon. ")

cz = input("What is the capital of Czech Republic?") #Czech Republic
if cz.casefold() == capitals[6].casefold():
    print ("Good job! It's correct!")
    score+=1
else:
    print ("Sorry, the correct answer is Prague. ")

grc = input("What is the capital of Greece?") #Greece
if grc.casefold() == capitals[7].casefold():
    print ("Good job! It's correct!")
    score+=1
else:
    print ("Sorry, the correct answer is Athens. ")

bulg = input("What is the capital of Bulgaria?") #Bulgaria
if bulg.casefold() == capitals[8].casefold():
    print ("Good job! It's correct!")
    score+=1
else:
    print ("Sorry, the correct answer is Sofia. ")

cyp = input("What is the capital of Cyprus?") #Cyprus
if cyp.casefold() == capitals[9].casefold():
    print ("Good job! It's correct!")
    score+=1
else:
    print ("Sorry, the correct answer is Nicosia. ")

print ("Your score is:" ,score) #Prints score
print ("Thank you for answering the quiz!")


'''
-------------------------------------------------------------------------------------------------------------------------------------------
CODE EXPLANATION
.casefold() were used to make the strings non case sensitive. 
Meaning, any user inputs regardless of the capitalization will be considered correct.
It will be considered correct as long as the spelling is right.

If statements were used to check if the users answers matches the capitals inside the list.
If the answer is right, the score+=1 is used to increment the user's score.

If the answer is wrong, this goes through the else statement which prints that the user's answer is wrong and shows the right answer.
-------------------------------------------------------------------------------------------------------------------------------------------
'''