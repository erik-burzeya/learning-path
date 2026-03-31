#BEST GRADE AVERAGE CALCULATION
def points_to_grade(points: int) -> float:
    if points < 300 or points > 900:
        raise ValueError("Points must be between 300 and 900.")

    difference = 900 - points
    grade = 1.0 + (difference // 18) * 0.1
    return min(grade, 4.0)

def main():
    while True:                 #While loop: making it possible to stop or repeat the calculation
        print()
        print("Welcome to the 'Average Grade Probability' calculator!")
        print()
        
        #ASKING FOR THE SCORE OF BLOCK I.:
        score = int(input("What is your score for block I.? Type your score (Calculated with E=P/U * 40): "))
        if score < 200:
            print("You will not be admitted to the A-level exams.")
        else:
            print("You will be admitted to the A-level exams.")
        
        print("Which subjects do you write your final exams in?")
            # instead of: fach1 = input("Fach 1: ")
            # and       : fach2 = input("Fach ": "),
            # we can use a for loop.
        
        #ASKING FOR SUBJECTS
        subjects = []   
        for i in range(4):
            subject = input(f"subject {i+1}: ")
            subjects.append(subject)
        
        #Printing the given subjects
        print()
        print("These are your subjects:")
        for i, subject in enumerate(subjects):
            print(f"Subject {i+1}: {subject}")
        
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

        #TOTAL AMOUNT OF POINTS
        print("All points that have been archieved in the final exams are multiplied by 5 and added to the points of block I.")
        print("The points of block I. and block II. make up the total amount of points.")
        print()
        print(f"Your total amount of points could lie between {(score + total_min*5)} and {(score + total_max*5)} points")
        restart = input("Do you want to start another calculation? (yes/no): ").lower()

        if restart == "no":
            print("Thank you for using the calculator.")
            print()
            print()
            break       

    while True:
        user_choice = input("Do you want to calculate your grade? (yes/no): ").lower()

        if user_choice == "no":
            print("Program terminated.")
            break

        try:
            points = int(input("Enter your total points (300–900): "))
            grade_value = points_to_grade(points)
            print(f"Your average grade is: {grade_value:.1f}")
        except ValueError as error:
            print(f"Error: {error}")
        again = input("Stop calculator (yes/no): ")
        if again == "yes":
            break
                    
main()