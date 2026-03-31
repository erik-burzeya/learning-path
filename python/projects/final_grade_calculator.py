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
        
        for i in range(len(subjects)):
            min_points = max(0, points[i] - 3)
            max_points = min(15, points[i] + 3)
            print(f"{subjects[i]:15}: {min_points:02}-{max_points:02} Punkte")
        print()

        
        restart = input("Do you want to start another calculation? (yes/no): ").lower()

        if restart == "no":
            print("Thank you for using the calculator.")
            print()
            print()
            break
        

         
            
        pass

main()