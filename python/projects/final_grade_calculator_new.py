#MENU
    #1: Calculating a possible final score
    #2: Turning a score into a grade average (e.g. 1.7)
    #3: Determining necessary final test results for a given final grade average


#1: Calculating a possible final score
def final_score_range():
    print()

    score = int(input("What is your score for block I.? Type your score (Calculated with E=P/U * 40): "))
    if score < 200:
        print("You will not be admitted to the A-level exams.")
    else:
        print("You will be admitted to the A-level exams.")
    print()
    
    print("Which subjects do you write your final exams in?")
    subjects = []   
    for i in range(4):
        subject = input(f"subject {i+1}: ")
        subjects.append(subject)
    #ASKING FOR POINTS
    points1 = []
    print()
    print("How many points do you expect to get in each exam?")
    for subject in subjects:
            while True:
                p = int(input(f"{subject}: ")) 
                if 0<= p <= 15:
                    break
                else:
                    print("Please enter a valid value between 0 and 15.")
            points1.append(p) 
   
    print()
   
    print("You expect the following points:")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {points1[i]} Punkte")
    
    print()
    print("Your marks may vary slightly. The following is a range within which your actual marks are likely to fall:")
    
    #CALCULATING THE POINT-RANGE
    total_min = 0
    total_max = 0

    for i in range(len(subjects)):
        min_points1 = max(0, points1[i] - 3)
        max_points1 = min(15, points1[i] + 3)

        total_min += min_points1
        total_max += max_points1

        print(f"{subjects[i]:15}: {min_points1:02}-{max_points1:02} Punkte")
    
    print()
    
    #POINT RANGE FOR BLOCK II.
    print(f"Your total amount of points for block II. could lie between {total_min*5} and {total_max*5} Points.")


#2: Turning a score into a grade average (e.g. 1.7)
def score_to_grade_average():
    print()


    return "Not implemented yet"


#3: Determining necessary final test results for a given final grade average
def wish_grade_average():
    print()


    return "Not implemented yet!"
    

#MAIN
def main():
    print()
    print("\nWelcome to the 'Final Grade calculator'!")
    print()
    print("\nMenu:")
    print()
    print("1 - Possible final score range")
    print("2 - Score to grade avergage")
    print("3 - Required score for the desired average")
    print()

    selection = int(input("Please select a calculator to begin: "))

    if selection == 1:
        print("Possible final score range: ", final_score_range())
    elif selection == 2:
        print("Score to grade avergage:", score_to_grade_average())
    elif selection == 3:
        print(f"Required score for the desired average: ", wish_grade_average())
    else:
        print("Please select a calculator ('1','2' or '3')!")
main()