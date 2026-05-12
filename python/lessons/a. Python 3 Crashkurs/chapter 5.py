# CHAPTER 5:
# IF-STATEMENTS

print("\nCHAPTER 5: IF-STATEMENTS")

# AN EASY EXAMPLE:
print("\nAn easy example:")
plants = ['Orchidacae', 'Digitalis', 'Tulpia', 'Rosa', 'Lilium', 'Dahlia']

for plant in plants:
    if plant == "Rosa":
        print(plant.upper())
    else:
        print(plant.lower())

# CONDITIONS:

# There are if-statements, elif-statements and else-statements.

# COMPARISON OPERATORS:

comparison_operators = ['== : is equal to',
                        '!= : is not equal to',
                        '<  : less than',
                        '>  : greater than',
                        '<= : less than or equal to',
                        '>= : greater than or equal to'
                        ]

print("\nThis is a list of comparison operators:")
for comparison_operator in comparison_operators:
    print(comparison_operator)
