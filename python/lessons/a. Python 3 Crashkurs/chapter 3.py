# CHAPTER 3
# AN INTRODUCTION TO LISTS


# ---------------
# DEFINITION AND RETRIEVING:

# A list is a collection of elements (a, b, c, .../ 1, 2, 3, .../ ...)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Python will print the complete list, including the brackets and quotation marks.
# To fix this, we can add [0] after bicycles:

print(bicycles[0])

# Now, the first Element is pinted.

# Accessing an element can be archieved by telling the programm to print the x-element of the list.
# If we want to print an element aton the end of a list (e.g. 20/400/7.0000/...), we can ask the
# programm to print the -x-element.

print(bicycles[-1]) # => specialized is printed


print()


# Elements of a list can be retrieved in a message, e.g.
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
# The resulting output is:
# My first bicycle was a Trek.

print()


# ---------------
# CHANGING ELEMENTS:


# Changing elements:                        --------------------

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

bicycles[0] = 'canyon'
print(bicycles)
# The resulting output is:
# ['trek', 'cannondale', 'redline', 'specialized']
# ['canyon', 'cannondale', 'redline', 'specialized']

print()


# Adding elements                           --------------------
# Elements can be added using the method append(), e.g.  in an empty list:

fruits = []
fruits.append('apple')
print(fruits)
fruits.append('banana')
print(fruits)

print()


# Inserting elements                        --------------------
# Elements can be inserted using the method insert(), e.g.:
fruits.insert(1, 'orange')
print(fruits) # => The fruit "orange" is inserted on position 1 (between "apple" and "banana")
# The "first" element of a list is the position 0

print()


# Removing elements                         --------------------
# Elements can be removed, using the method del(), e.g.:

del fruits[0]
print(fruits)

# AFTER REMOVING AN ELEMENT, IT IS NO LONGER POSSIBLE TO ACCESS THE DELETED VALUE!!!

# Removing elements with the method pop()    --------------------
# By using the method pop() instead of del(), elements can still be used!

# ()
print()
print("Removing elements with the method pop():")
fruits.insert(0, 'apple')
# ()

print(fruits)

popped_fruits = fruits.pop()
print(fruits)
print(popped_fruits) # The elements, which has been removed from the list, is printed.

# This method is useful for making a statement about the (last) element, e.g.:

print(f"The last fruit I ate yesterday was a {popped_fruits}!")

# OR

first_fruit = fruits.pop(0)
print(f"The first fruit I ate today was an {first_fruit}!")

# Removing elements depending on their value:

fruits = ['apple', 'banana', 'orange', 'melon', 'grape', 'blueberry']
print(fruits)

print()

fruits.remove('orange')
print(fruits)

# The method remove() makes Python search for an element and remove it.
# Another example: "1. sandox_2.py"

print()


# ---------------
# SORTING LISTS:

# Using the method srot(), the order of elements of a list can be changed.

latinPlantNames = ['Orchidacae', 'Digitalis', 'Tulpia', 'Rosa', 'Lilium', 'Dahlia']
print(f"Some latin plant names: {latinPlantNames}")

print()
print("Sorted (in alphabetical order):")
print()

latinPlantNames.sort()
print(latinPlantNames)

print()
print("Sorted (in reversed alphabetical order):")
latinPlantNames.sort(reverse=True)
print(latinPlantNames)

# When using the sort()-method, a lists order is changed permanently.

print()


# Sorting lists temporarily                 --------------------

latinPlantNames = ['Orchidacae', 'Digitalis', 'Tulpia', 'Rosa', 'Lilium', 'Dahlia']
print(latinPlantNames)
print(f"Temporarily sorted list of the latin plant names: {sorted(latinPlantNames)}")


# Finding the length of a list              --------------------

print(len(latinPlantNames))

# The function len counts the number of elements of a list


# ---------------
# AVOIDING INDEX ERRORS:

# The last element of a list can be displayed using "print(listName[-1])"!

# The first element is located at index 0!

# Often, index errors can be solved by checking the list's length!
