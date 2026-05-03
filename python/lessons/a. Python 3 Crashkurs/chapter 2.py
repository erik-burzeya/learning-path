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