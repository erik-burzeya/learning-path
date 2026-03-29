#MY FIRST PYTHON_PROGRAM
print("Hello, World!")
    #print() displays text in the console
    #everythin inside "" is a string, which is a type of data that represents text
    #you can also use '' for strings, but "" is more common in Python
name = "Erik"
age = 18




#UNDERSTANDING VARIABLES
    #A variable is a name that refers to a value. You can think of it as a container that holds data.
    #In Python, you can create a variable by assigning a value to it using the = operator.
print(name)
print(age)




#INPUT FROM THE USER
name = input("What is your name? ")
print("Hello, " + name + "!")
    #input() waits for the user to type something and press Enter, then it returns that input as a string.
    # You can store it in a variable and use it later in your program. 



#DATA TYPES (important for understanding how to work with variables)
age = int(input("How old are you? "))
print("In 50 years, you will be " + str(age + 50) + " years old.")
