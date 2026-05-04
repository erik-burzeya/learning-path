##VARIABLES AND BASIC DATA TYPES

    ## .py shows the filetype (python file)
    ## The python interpreter reads the code.
    ## The editor colors the code (dt. Syntaxkennzeichnung, engl. syntax highlighting)


# ---------------
# VARIABLES:

message = "Hello Python world!"
print(message)

# The resulting output is "Hello Python world!"
# "message" is our variable
# Using two lines means more work for the interpreter!

# Add the text "Hello Python Crash Course world!"

message = "Hello Python Crash Course world!"
print(message)

# The resulting output is 
# "Hello Python world!"
# "Hello Python Crash Course world!"

# The value of a variable can change at any time.
# Pyton always remembers the current value.


# ---------------
# RULES FOR NAMING AND USING VARIABLES

# Variable names must only contain letters, digits, numbers
# Variable names must always start with a letter or digit
# Spaces are not allowed
# Python keywords or -funktion names are not allowed
# Variable names must be short and meaningful
# (e.g.: "name" is better than "n" and "name_length" is better than "length")
# Be careful when using I and o/O, as these could be confused with 1 (one) and 0 (zero)


# ---------------
# AVOIDING MISTAKES WITH VARIABLE NAMES

# Wrong: 
# message = "Hello Python world!"
# print(mesage)

# The terminal shows the location of a possible mistake (traceback):
    # Traceback (most recent call last):
    #  File "/Users/erikburzeya/Documents/07. Lernen/Programmieren (Lernpfad I.)/learning-path/python/lessons
    #  /a. Python 3 Crashkurs/chapter 2.py", line 48, in <module>
    #    print(mesage)
    # NameError: name 'mesage' is not defined

# Programming languages ​​don't distinguish between good and bad spelling. 
# If we had typed "mesage" both times, we would have gotten a correct result.


# ---------------
# STRINGS

# A string is a data type. Everything within single or double questionmarks is a string.
# E.g.:
# "I told my friend: 'Python is my favorite language!'"


# ---------------
# METHODS (AND CAPITALIZATION):

name = "ada lovelace"
print(name.title())

# The METHOD "title()"" displays all words in capital letters.
# The dot after "name" implies that the following method must be applied to the variable "name".
# Methods need declarations (that will be added in brackets). 
# The medhod "title" doesn't need these, therefore the brackets are empty.

name = "ada lovelace"
print(name.upper())
print(name.lower())

# Result => "ADA LOVELACE" AND "ada lovelace"
# print(name.lower()) is especially useful when storing data. Users might make a spelling mistake.
# The correct spelling can be applied later.


# ---------------
# VARIABLES IN STRINGS

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # "f" is used to insert a variable in a string (inside the curly brackets)
print(full_name)

# Other examples for "F-STRINGS":

print(f"Hello, {full_name.title()}!")

# OR

message = f"Hello, {full_name.title()}!"
print(message)


# ---------------
# ADDING WHITE SPACE
# (non-printable symbols like space-/tab characters or line breaks)

# Tab characters:

# \t
print("Python")
#Python

print("\t Python")
#   Python

# Line breaks:
# \n
print("\nLanguages: \nPython\nJavaScript\nCSS")

# Tab charakters and line breaks can be combindes:

print("\nLanguages: \n\tPython\n\tJavaScript\n\tCSS")


# ---------------
# REMOVING WHITE SPACE

# "rstrip" OR "lstrip" (removing spaces from the left or right side of a string)

first_name = "ada"
last_name = "lovelace " # The space after "lovelace" would be visible without the method ".rstrip()"!
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title().rstrip()}!"
print(message)

# ---------------
# CALCULATING

a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
exponents = a**b


print(a + b, a**b)

universe_age = 14_000_000_000
print(universe_age)
# Result => 14000000000


# ---------------
# CONSTANT

# A constant does not change during the lifespan of the program.
# By convention, Python programmers use uppercase letters to indicate 
# that a variable should be treated as a constant.

MAX_CONNECTIONS = 5000

# ---------------
# COMMENT

# 


# ---------------
# THE ZEN OF PYTHON

# "Beautiful is better than ugly."

# "Simple is better than complex"

# Readability counts