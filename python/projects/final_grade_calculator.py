def main():
    while True:
        print()
        print("Welcome to the 'Average Grade Probability' calculator!")
        print()
        score = int(input("What is your score for block I.? (Calculated with E=P/U * 40)"))
        if score < 200:
            print("You will not be admitted to the A-level exams.")
        else:
            print("You will be admitted to the A-level exams.")
        
        print("Which subjects do you write your final exams in?")
            # instead of: fach1 = input("Fach 1: ")
            #        fach 2 = ...
            # we can use a for loop
        
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
        points = []
        print()
        print("How many points do you expect to get in each exam?")
    
        for subject in subjects:
            while True:
                
                        p = int(input(f"{subject}: "))
                        
                        if 0<= p <= 15:
                            break
                        else:
                            print("Please enter a valid value between 0 and 15.")
            points.append(p) 
        print()
        print("You expect the following points:")
        for i in range(len(subjects)):
            print(f"{subjects[i]}: {points[i]} Punkte")
        
        print()
        print("Your marks may vary slightly. The following is a range within which your actual marks are likely to fall:")
        
        total_min = 0
        total_max = 0

        for i in range(len(subjects)):
            min_points = max(0, points[i] - 3)
            max_points = min(15, points[i] + 3)

            total_min += min_points
            total_max += max_points

            print(f"{subjects[i]:15}: {min_points:02}-{max_points:02} Punkte")
        
        print()
        
        #POINT RANGE FOR BLOCK II.
        print(f"Your total amount of points for block II. could lie between {total_min*5} and {total_max*5} Points.")

        #TOTAL AMOUNT OF POINTS
        print("All points that have been archieved in the final exams are multiplied by 5 and added to the points of block I.")
        print("The points of block I. and block II. make up the total amount of points.")
        print()
        print(f"Your total amount of points could lie between {(score + total_min)*5} and {(score + total_max)*5} points")
        restart = input("Do you want to start another calculation? (yes/no): ").lower()

        if restart == "no":
            print("Thank you for using the calculator.")
            print()
            print()
            break
        

         
            
    pass

main()