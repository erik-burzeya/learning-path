#TASK 1:
def task1():
    print("Task 1:")
    name = input("What is your name? ")
    print("Hello, " + name.capitalize() + "!")

    age = int(input("How old are you? "))

    height = float(input("How tall are you in meters? "))

    print("Would you like to know your height in foot? Please type yes or no")
    answer = input()
    if answer.lower() == "yes":
        foot = height * 3.28084   #This calculation should not be done beforehand, because if the user says no, it will be a waste of resources.
        print("Your height in foot is: " + str(foot) + " ft.")
    elif answer.lower() == "no":
        print(".")






#--------------------------------------
#TASK 2:

def task2():
    print("Task 2:")
    print("Welcome to the shopping cart program!")
    total = 0   # This variable will keep track of the total price of the items in the cart.

# First Product:
    price = float(input("Pric of the item: "))
    quantity = int(input("Quantity: "))
    total += price * quantity

# Now the loop:
    while True:
        command = input("Type 'add' to add an item to your cart or 'checkout' to finish: ").strip().lower()
            
        if command == "checkout":
            print("Total:", total, "€")
            break
    
        elif command == "add":
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                total += price * quantity

        else: print("Invalid command.\n")


task2()
