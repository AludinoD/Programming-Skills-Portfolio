#-----------------------------------------------------Modules-----------------------------------------------------------------------------------
import sys #Exits The system
import os #Clearing the console
import random #For RNG
from time import sleep #For Delays 
#----------------------------------------------------Debugging-----------------------------------------------------------------------------------
# Vending Machine Categories and Products.
categories = {
    "Drinks": { # Drinks are abbreviated as D.
        "D1": {"name": "Water", "price": 1.50},
        "D2": {"name": "Pepsi", "price": 3.50},
        "D3": {"name": "Lipton Iced Tea", "price": 2.50}
    },
    "Snacks": { # Snacks are abbreviated as S.
        "S1": {"name": "Lays Chips", "price": 1.50},
        "S2": {"name": "Cheetos Chips", "price": 2.50},
        "S3": {"name": "Oreo Cookies", "price": 3.50}
    },
    "Chocolates": { # Chocolates are abbreviated as C.
        "C1": {"name": "Snickers", "price": 1.50},
        "C2": {"name": "KitKat", "price": 2.50},
        "C3": {"name": "Maltesers", "price": 3.50}
    }
}

# Generate a random number for the stocks per item (0-10).
stock = {category: {item_id: random.randint(0, 10) for item_id in items} for category, items in categories.items()}

# Tracks how many purchases, receipts and balance the user has. Defaulted to 0.
user_purchase = []
user_receipt = 0
user_balance = 0.00

#----------------------------------------------------Common Code Used Explanation----------------------------------------------------------------

# Every function of the vending machine is made by using different functions(def + function name) and are just called when needed.
# .casefold() is used to make string inputs non-case sensitive.
# .isdigit() is used to ensure that the inputs are integers and not strings.
# .2f is used for 2 decimal places of a number, example: 1.00.
# f string or formatted strings are used for expressing expressions enclosed inside of a curly braces {}. It accesses and prints the values inside of the dictionary.
# Global is used for accessing variables that are outside of a function.


#----------------------------------------------------Start up screen Functions-------------------------------------------------------------------
# For the Loading Bar Visual.   
def loading(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total))) #Calculating the percentage.
    filledLength = int(length * iteration // total) #Calculates how many characters should be filled in the progress bar.
    bar = fill * filledLength + '-' * (length - filledLength) #Builds the progress bar.
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r') #Displaying the progress bar.
    if iteration == total: #Prints a new line, showing that the progress is done.
        print()
        
# For the Loading Screen Animation.
def simulate_loading():
    items = list(range(0, 50)) #Creates a list of 50 items.
    total = len(items) #Calculates the total amount of items.
    for i, item in enumerate(items): #Starts a loop that iterates over each item in the list.
        sleep(0.1) #Delay of 0.1 seconds.
        loading(i + 1, total, prefix='Loading Vending Machine...', suffix='Complete', length=50) #Calls the loading function.


#Function for clearing the Console.
def clear_console():
    input("Press 'Enter' to continue...") #User Input
    os.system("cls" if os.name == "nt" else "clear")  #Clear console for different operating systems
    header() #Calls the header function.

# Function for printing the header.
def header():
    header = [
        "████████╗██╗  ██╗███████╗    ██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗",
        "╚══██╔══╝██║  ██║██╔════╝    ██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝",
        "   ██║   ███████║█████╗      ██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  ",
        "   ██║   ██╔══██║██╔══╝      ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  ",
        "   ██║   ██║  ██║███████╗     ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗",
        "   ╚═╝   ╚═╝  ╚═╝╚══════╝      ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝",
        "----------------------------------------------------------------------------------------------------------------------------------------------------"]
    for line in header:
        print(line)
        sleep(0.1)  #Delay for animation effect
    print("\n")

#---------------------------------------------------------Vending Machine Core----------------------------------------------------------------------------------

# Function for inserting cash.
def insert_cash():
    global user_balance  #Access user_balance as a Global Variable.
    while True:  #Runs a loop until the conditions are met.
        userCash = input("Insert cash: ") #Asks the user to insert cash.

        # Check if input is a valid number.
        if userCash.isdigit():
            userCash = float(userCash)  #If the input is a digit, convert it to a float.

            # Check if the input is greater than 0.
            if userCash > 0:
                user_balance += userCash  #Add cash to user balance.
                clear_console()  #Clear the console after cash is added.
                print(f"Successfully added ${userCash:.2f} to your balance.")  #Confirm cash has been added.
                vending_machine()  #Return to vending machine menu.
                break  #Exit the loop after adding cash.
            else: #If the input is less than 0
                print("Please insert a valid amount GREATER than 0.")  #Informs the user to put an amount greater than 0.
        else: #If the input is not a number.
            print("Please enter a VALID number.")  #Informs the user to put a valid number.


#---------------------------------------------------------------------------------------------------------------------------------------------

# Function for showing the vending machine menu.
def show_menu():
    clear_console() #Clears Console to avoid flooding.
    print("\n-----------Vending Machine Menu-----------") # Top Header.
    for category, items in categories.items(): #Creates a list that checks the categories.
        print(f"\n{category}:")  # Prints the category name.
        for item_id, item_info in items.items(): 
            item_name = item_info['name'] # Item Name
            item_price = item_info['price'] # Item Price
            availability = f"Stock: {stock[category][item_id]}" if stock[category][item_id] > 0 else "Out of Stock" #Checks the availability of the item.
            print(f"  ID: {item_id} - {item_name} - ${item_price:.2f} ({availability})")  # Prints the item ID, name, price, and stock.
    print("------------------------------------------")  # Bottom Header




def purchase_item():
    global user_balance # Access the user_balance as a Global Variable
    global user_purchase # Access user_purchase as a Global Variable.
    global user_receipt # Access user_receipt as a Global Variable.

    while True:
        show_menu()  # Calls the menu function to show the available categories and items.
        
        category_choice = input("Enter the CATEGORY name (or type 'exit' to go back): ").casefold() #Asks the user for the category name and is non case sensitive.

        if category_choice == "exit".casefold(): # If the user wants to go back to the vending machine options.
            clear_console()  #Clears console to avoid flooding
            return  #Returns to the main vending machine options.

        # Validate category
        matching_categories = [cat for cat in categories if cat.casefold() == category_choice]  # Checks if the category matches in a case-insensitive way.
        if not matching_categories:  # If no valid category is found.
            print("Invalid CATEGORY NAME. Please try again.")  # Informs the user the category name is invalid.
            continue  #Asks for the category again.

        selected_category = matching_categories[0]  # Select the first matching category.
        print(f"Items in {selected_category}:")  # Displays the items in the selected category.

        # Displays items with their ID, name, price, and stock availability.
        for item_id, item_info in categories[selected_category].items():
            item_name = item_info['name']
            item_price = item_info['price']
            availability = f"Stock: {stock[selected_category][item_id]}" if stock[selected_category][item_id] > 0 else "Out of Stock"
            print(f"  ID: {item_id} - {item_name} - ${item_price:.2f} ({availability})")

        while True:
            item_id = input("Enter the ITEM ID to purchase (or type 'exit' to go back): ").casefold() #Asks the user for the item ID and is non case sensitive.

            if item_id == "exit".casefold(): #If the user wants to go back to the vending machine options.
                return  #Returns to the vending machine options.

            # Validate item ID
            item_id_upper = item_id.upper()  #Converts user input to uppercase to match with item IDs stored in the dictionary.
            if item_id_upper not in categories[selected_category]:  #If the item ID doesn't match.
                print("Invalid ITEM ID. Please try again.")  #Informs the user that the input is invalid.
                continue  #Asks for the item ID again.

            # Check stock availability
            if stock[selected_category][item_id_upper] <= 0:  # If the stock is 0 or less.
                print(f"Sorry, {categories[selected_category][item_id_upper]['name']} is out of stock.")  #Informs the user that the item is out of stock.
                continue  #Goes back to asking for a valid item.

            # Asking for quantity to purchase
            while True:
                quantity_input = input(f"How many {categories[selected_category][item_id_upper]['name']} would you like to purchase? (Available stock: {stock[selected_category][item_id_upper]}): ") #Asks the user how much quantity they want to buy.
                
                # Check if the quantity is a valid number and is greater than 0.
                if quantity_input.isdigit() and int(quantity_input) > 0:
                    quantity = int(quantity_input)  #Converts input to an integer.
                    
                    if quantity > stock[selected_category][item_id_upper]:  #If the user requests more items than available.
                        print(f"Sorry, we only have {stock[selected_category][item_id_upper]} in stock.")  #Informs the user about the stock.
                        continue  #Asks for quantity again.

                    total_cost = categories[selected_category][item_id_upper]['price'] * quantity  #Calculate total cost.

                    # Check if the user has enough balance to make the purchase.
                    if total_cost > user_balance:
                        print(f"Insufficient balance. You need ${total_cost - user_balance:.2f} more.")  #Informs the user if balance is insufficient.
                        return  #Returns to ask how much quantity they want, as they don't have enough balance.

                    # Process the purchase:
                    user_balance -= total_cost  #Deduct the total cost from the user's balance.
                    stock[selected_category][item_id_upper] -= quantity  #Subtract the purchased quantity from the stock.
                    user_purchase.extend([categories[selected_category][item_id_upper]['name']] * quantity)  #Track the purchased items.
                    user_receipt += quantity  #Add the purchased quantity to the user receipt.

                    clear_console()  #Clear the console after successful purchase.
                    print(f"Successfully purchased {quantity} {categories[selected_category][item_id_upper]['name']}(s) for ${total_cost:.2f}.")  #Informs the user that purchase is successful.
                    print(f"Dispensing {quantity} {categories[selected_category][item_id_upper]['name']}(s). Enjoy!")  #Dispenses Item.
                    print(f"Your change is ${user_balance:.2f}.")  #Inform the user of their remaining balance.
                    
                    # After purchasing, offer a random product suggestion.
                    suggest_product()  #Call the function to suggest a random product.
                    return  # Return to the main vending machine menu after purchase.

                else:  #If the input is not a valid number or is less than or equal to 0.
                    print("Please enter a VALID number for quantity.")  #Inform the user to input a valid quantity.


# Function for Suggesting a Product.
def suggest_product():
    global user_balance  # Access the user_balance as a Global Variable.
    global user_receipt  # Access the user_receipt as a Global Variable.
    
    # Choose a random category and item from the categories dictionary.
    category, item = random.choice([(cat, itm) for cat, items in categories.items() for itm in items]) 
    
    # Get the price from the item dictionary.
    price = categories[category][item]['price'] 
    
    # Check if the stock of the item is greater than 0.
    if stock[category][item] > 0:  
        while True:
            #Ask the user if they want to try the random product.
            print(f"Would you like to try {categories[category][item]['name']} from {category} for ${price:.2f}? (yes/no): ", end="")
            response = input().casefold()  #User input and non case sensitive.
            
            if response == "yes".casefold():
                #Check if the user has enough balance to buy the product.
                if user_balance >= price:
                    user_balance -= price  #Deduct the price from the user's balance.
                    stock[category][item] -= 1  #Decrease the stock of the item.
                    user_purchase.append(categories[category][item]['name'])  #Add the item to the user's purchase list.
                    user_receipt += 1  # Add to the user's receipt.
                    print(f"Your change is ${user_balance:.2f}.")  #Inform the user of their remaining balance.
                    clear_console()  #Clear console after adding suggestion.
                    print(f"You have added {categories[category][item]['name']} to your purchase for ${price:.2f}.")  #Inform the user of the purchase.
                else:
                    print("Insufficient balance for the suggested item.")  # Inform the user if they don't have enough balance.
                    clear_console()  #Clears Console to avoid flooding.
                break  #Exit the loop after responding to the suggestion.

            elif response == "no".casefold():
                print("No problem!")
                clear_console()  #Clears Console to avoid flooding.
                break  #Exit the loop.

            else:
                print("Invalid Input. Please enter 'yes' or 'no' only.")  #Informs the user that they placed an invalid input.


# Function for showing the receipt.
def show_receipt():
    global user_purchase  #Access the user_purchase as a Global Variable.
    global user_balance   #Access user_balance as a Global Variable.
    clear_console()  #Clears the console so that the receipt will be the main focus.
    print("\n----------- Receipt -----------")  # Top Header

    if user_purchase:
        total_spent = 0  #How much the user spent in total. Defaulted to 0
        for item in user_purchase:
            print(f"{item}")  #Print each purchased item

            # Find the item in the categories and sum up the price
            for cat in categories:
                for item_id, item_info in categories[cat].items():
                    if item_info['name'] == item:  #Match the item name
                        total_spent += item_info['price']  #Add the item's price to the total spent

        # Print total spent and remaining balance
        print(f"Total Spent: ${total_spent:.2f}")
        print(f"Remaining Balance: ${user_balance:.2f}")
    else:
        print("No items purchased.")  #If the user has not purchased anything yet.

    print("-------------------------------")  #Bottom Header
    clear_console()  #Clears Console to avoid flooding.

#-------------------------------------------------------Admin Commands---------------------------------------------------------------------
# Function for Admin Menu.
def admin():

    print("Are you an Admin because you control everything, or do u control everything because you're an admin?") 
    password = input ("Password:") #Ask for the password. 
    if password == "IControlEverything.": #Password 
        print ("Access Granted. Welcome , Admin.") #Indicates that the user accessed the admin commands.

    else:
        print("You are not Him.") #Indicates that the user placed the wrong password.
        clear_console() #Clears Console to avoid flooding.
        vending_machine() #Goes back to the vending machine
    while True:
        show_menu()
        print ("----ADMIN MENU----") # Top Header 
        print ("[1] Add Stock\n[2] Remove Stock\n[3] Exit Admin Menu") #Options
        print ("-----------------") # Bottom Header
        admin_input = input ("Option:") #Asks for user input.

        if admin_input == "1": #Add Stock
            add_stock() #Calls the add_stock function.
        elif admin_input == "2": #Remove Stock
            remove_stock() #Calls the remove_stock function
        elif admin_input == "3": #Exit Admin Menu or go back to the vending machine.
            clear_console() #Clears the Console to avoid flooding.
            vending_machine() #Calls and goes back to the vending machine option.
        else:
            print("Invalid Input. Please enter a VALID number.") #  Indicator that the user placed an invalid number.

# Function for adding stocks.
def add_stock():
    while True: #Runs a loop until the conditions are met.
        show_menu() #Shows the menu so that the user can see what the stocks are.
        category = input("Enter the CATEGORY name to add stock (or type 'exit' to go back): ").casefold() #Asks the user for the category name and is non case sensitive.
        if category == "exit".casefold(): #If the user wants to return to the Admin menu commands.
            return #Goes back to the Admin Menu Commands.

        matching_categories = [cat for cat in stock if cat.casefold() == category] #Validates if the category matches the categories in the dictionary.
        if not matching_categories: #If the user's category doesn't match the categories, it informs the user.
            print("Invalid CATEGORY name. Please try again.") #Indicates that the category name doesn't match
            continue #Asks the user for the category name again.

        selected_category = matching_categories[0] #Selects the first matching category.

        while True: #Runs a loop until the conditions are met. 
            item_id = input(f"Enter the ITEM ID to add stock in {selected_category} (or type 'exit' to go back): ").casefold() #Asks the user for the item ID and is non case sensitive.
            if item_id == "exit".casefold(): #If the user wants to return to the Category menu
                return  #Returns to the admin menu.

            matching_items = [item for item in stock[selected_category] if item.casefold() == item_id] #Validates if the item ID matches the items in the category.
            if not matching_items: #If the user's item doesn't match the item's ID's, it informs the user.
                print("Invalid ITEM ID. Please try again.") #Indicates that the item ID doesn't match.
                continue #Asks the user for the item ID again.

            selected_item_id = matching_items[0] #Selects the first matching item.

            while True: #Runs a loop until the conditions are met.
                quantity = input(f"Enter the quantity to ADD to {selected_item_id} (or type 'exit' to go back): ").casefold() #Asks the user for the quantity to add to the item.
                if quantity == "exit".casefold(): # If the user wants to return to the admin menu.
                    return  # Returns to the admin menu.

                if quantity.isdigit() and int(quantity) > 0: #Checks if the user input(quantity) is a digit and is greater than 0.
                    stock[selected_category][selected_item_id] += int(quantity) #Adds the user quantity to the stock of the selected item.
                    print(f"Successfully added {quantity} to {selected_item_id} in {selected_category}.") #Indicates that the quantity has been added to the item.
                    return  #Exit after successfully adding stock.
                else:
                    print("Invalid input. Please enter a POSITIVE number.") #Indicates that the user input is not a number or is less than 0.


# Function for removing stock.
def remove_stock():
    while True: #Runs a loop until the conditions are met.
        show_menu() #Shows the menu so that the user can see what the stocks are.
        category = input("Enter the CATEGORY name to remove stock (or type 'exit' to go back): ").casefold() #Asks the user for the category name and is non case sensitive.
        if category == "exit": #If the user wants to return to the Admin menu commands.
            return  #Returns to the admin menu.

        # Find the matching category (case-insensitive)
        matching_categories = [cat for cat in stock if cat.casefold() == category] #Validates if the category matches the categories in the dictionary.
        if not matching_categories: #If the user's category doesn't match the categories, it informs the user.
            print("Invalid CATEGORY name. Please try again.") #Indicates that the category name doesn't match
            continue #Asks the user for the category name again.

        selected_category = matching_categories[0] #Selects the first matching item.

        while True: #Runs a loop until the conditions are met.
            item_id = input(f"Enter the ITEM ID to remove stock in {selected_category} (or type 'exit' to go back): ").casefold() #Asks the user for the item ID and is non case sensitive.
            if item_id == "exit": #If the user wants to return to the Admin menu commands.
                return  #Returns to the admin menu.

            matching_items = [item for item in stock[selected_category] if item.casefold() == item_id] #Validates if the item ID matches the items in the category.
            if not matching_items: #If the user's item doesn't match the item's ID's, it informs the user.
                print("Invalid ITEM ID. Please try again.") #Indicates that the item ID doesn't match.
                continue #Asks the user for the item ID again.

            selected_item_id = matching_items[0] #Selects the first matching item.

            while True: #Runs a loop until the conditions are met.
                quantity = input(f"Enter the quantity to REMOVE from {selected_item_id} (or type 'exit' to go back): ").casefold() #Asks the user for the quantity to remove from the item.
                if quantity == "exit": #If the user wants to return to the Admin menu commands.
                    return  #Returns to the admin menu.

                if quantity.isdigit() and int(quantity) > 0: # Checks if the user input(quantity) is a digit and greater than 0.
                    quantity = int(quantity) #Converts the quantity into an integer.
                    if stock[selected_category][selected_item_id] >= quantity: #Checks if the stock is greater than or equal to the quantity the user wants to remove.
                        stock[selected_category][selected_item_id] -= quantity #If it stock is greater than or equal to the quantity, the stock gets subtracted with the user's wanted quantity.
                        print(f"Successfully removed {quantity} from {selected_item_id} in {selected_category}.") #Indicates that the quantity has been removed from the item.
                        return  #Exit after successfully removing stock.
                    else:
                        print(f"Insufficient stock to remove. Current stock: {stock[selected_category][selected_item_id]}.") #If the quantity the user wants to remove is greater than the stocks.
                else:
                    print("Invalid input. Please enter a POSITIVE number.") #Indicates that the user input is not a number and is greater than 0.
#-------------------------------------------------------------------------------------------------------------------------------------------
# Function for the vending machine
def vending_machine():
    global user_balance #Access the user_balance as a Global Variable.
    global user_receipt #Access the user_receipt as a Global Variable.
    global user_purchase #Access the user_purchase as a Global Variable.
    print ("Hello! Welcome to THE VENDING MACHINE!\nTake your time and feel free to try everything!\nEnjoy!")
    
    while True: #Runs a loop until the conditions are met.
        print ("-----------------User Interface---------------------") #Top Header
        print (f"User Balance = {user_balance:.2f}" + "$") #Tracks the balance the user has.
        print (f"User Receipt = {user_receipt}") #Tracks the receipt.
        print ("-----------------------------------------------------") #Bottom Header
        user_input = input ("What do you want to do?\nOptions:\n[1] Insert Cash\n[2] Look at the Menu\n[3] Purchase Item \n[4] See the Receipt \n[5] Exit THE VENDING MACHINE\nOption: ") #Shows the options user can choose.
        if user_input ==  "1": #Insert Cash
            insert_cash() #Calls the insert_cash function
            
        elif user_input == "2": #Show Menu
            show_menu() #Calls the show_menu function
            
        elif user_input == "3": #Purchase Item
            purchase_item() #Calls the purchase_item function.
            
        elif user_input == "4": #Show Receipt
            show_receipt() #Calls the show_receipt function.
            
        elif user_input == "5": #Exit THE VENDING MACHINE and Show Receipt
            print ("Thank you for using THE VENDING MACHINE!")
            print ("Here is your receipt!")
            show_receipt() #Calls the show_receipt function.
            sys.exit() #Exits the console.
        
        elif user_input == "Admin": #Admin Commands
            admin() #Calls the admin function.
            clear_console() #Clears Console to avoid flooding.
        else:
            print("Invalid Input. Please enter a VALID Number.") #Indicator that the user placed an invalid number.
    

# Function for starting the program
def start():
    while True: #Runs a loop until the conditions are met.
        user_ans = input("Do you want to use THE VENDING MACHINE? (Yes/No): ").casefold() #Asks the user if they want to use THE VENDING MACHINE and is non case sensitive.
        if user_ans == "yes":
            header() #Calls the header function.
            simulate_loading() #Calls the loading bar.
            clear_console() #Clears Console to avoid flooding.
            vending_machine() #Calls the main vending machine
            break
        elif user_ans == "no":
            print("Very well. Goodbye! Have a nice day!")
            header()
            sys.exit() #Exits the console.
        else:
            print("Invalid input. Please enter 'Yes' or 'No' only.") #Informs the user that they placed an invalid input.

# Starts THE VENDING MACHINE
start()