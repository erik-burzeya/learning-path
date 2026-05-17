# CHAPTER 4
# WORKING WITH LISTS

# ---------------
# INTERATING THROUGH A COMPLETE LIST:
print("ITERATING THROUGH A COMPLETE LIST:")
print()


iPhones = ['iPhone, 2007', 'iPhone 3G, 2008',
           'iPhone 3GS, 2009', 'iPhone 4, 2010']
print("These are the first four iPhones:")
for iPhones in iPhones:
    print(iPhones)

# Using a for-loop, elements on a list can be printed:

    # These are the first four iPhones:
    # iPhone, 2007
    # iPhone 3G, 2008
    # iPhone 3GS, 2009
    # iPhone 4, 2010

# Python always returns to the first part of the command, as there are
# still elements left.

# Typical mistakes:

    # Indentation Errors are typical errors for coding-beginners!
    # pizza = ['1', '2', '3']
    # for pizza in pizza:
    # print(pizza)                      <- This should be indented

    # pizza = ['1', '2', '3']
    # for pizza in pizza:
    #   print(pizza)
    # print("That was a good pizza!")   <- As it is indented, the command is
    # part of the loop.

    # Forgotten colon at the end
    # pizza = ['1', '2', '3']
    # for pizza in pizza                <- A colon is needed at this position to
    #   print(pizza)                       make the loop work

print()


# ---------------
# NUMERIC LISTS:
print("WORKING WITH NUMERIC LISTS:")
print()

# range()-function:

for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)


print()


# Converting range() to a list:


numbers = list(range(1, 6))
print(numbers)

# Displaying only even numbers:

print()
print("Even numbers:")
even_numbers = list(range(2, 11, 2))
print(even_numbers)

print()
print("Uneven numbers:")
uneven_numbers = list(range(1, 10, 2))
print(uneven_numbers)


# Displaying squares:

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

# OR:       => First try to write code correctly. Trying to make code
# shorter can be done later.

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

print()


# Simple statistics for numeric lists:

print(min(squares))
print(max(squares))
print(sum(squares))

print()


# Notation of lists:

squares = [value**2 for value in range(1, 11)]
print(squares)

print()


# ---------------
# WORKING WITH SLICES:
print("WORKING WITH SLICES:")
print()

animals = ['dog', 'cat', 'bird', 'horse', 'worm']
print(animals[0:3])                 # => Only the required subset is displayed.

# More examples:

print(animals[:5])      # => Python automatically starts at the first position.
# => Python automatically displays all elements, starting with the THIRD element.
print(animals[2:])
print(animals[-3:])     # => ['bird', 'horse', 'worm']
# => ['cat', 'horse'] (every second element is displayed)
print(animals[1::2])

print()


# Copying lists:
# Lists can be copied using "[:]":

my_foods = ['carrot cake', 'noodles', 'sushi']
friends_foods = my_foods[:]

print(f"My foods are: {my_foods}!")
print(f"My friends foods are: {friends_foods}!")

# Now, an element can be added to each list:

print()


my_foods.append('falafel')
friends_foods.append('yoghurt')

print(f"My foods are: {my_foods}!")
print(f"My friends foods are: {friends_foods}!")

print()

# ---------------
# TUPLES:

print("TUPLES:")
print()

print(
    "Tuples are lists with parentheses instead of square brackets, "
    "which cannot be modified after creation.")

print()

dimensions = (300, 30)
print(dimensions[0])
print(dimensions[1])

print()

# We cannot change an element inside of a tuple!
# dimensions = (300,30)
# dimensions[0] = 250

#  dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment

# TUPLES ARE (TECHNICALLY) DEFINED BY THE EXISTANCE OF A COMMA!

# RUNNING THROUGH THE ELEMENTS OF A TUPLE:

# Tuples can be run through like a list

# Changing a tuple is NOT possible, altough changing a variable that holds
# a tuple IS possible, e.g.:

dimensions = (300, 30)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 40)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

# Compared to lists, tuples are simple data structures.

print()


# ---------------
# FORMATTING RULES (PEP 8 style guidelines):

# A combination of spaces and indents can lead to confusion.
# Lines should be no longer than 80 characters.
# Spaces can be useful, e.g. to structure files, but should not be used
# excessively.

# PEP 8 = Python Enhancement Proposal 8


def test(x, y):
    print(x + y)
