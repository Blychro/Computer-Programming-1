# Thomas Marshall
# weightedAverage.py


# This program will use the grades and the names listed in grades.txt file to
# calculate the weighted average of each student listed in the file and give the
# class average.


# Inputs: Names and grades given in the grades.txt file.
# Outputs: Each student's weighted average and the classes weighted average.
# I certify that this lab is entirely my own work.

def weightedAverage():
    # Program explanation
    print("This program will use the grade.txt file to calculate the weighted\n"
          "average of each student listed in the file, as well as the class average.\n")

    # Opens the grade.txt file for use
    grades = open("grades.txt", "r")
    
    # Definitions for the math later
    total = 0
    count = 0

    # line loop used to individualize each line of text
    for line in grades:
        # Gives a list
        lists = line.split()
        # Seperate the name from the grades
        names = lists[0] + " " + lists[1]
        gradesList = lists[2:]

        # Another definition that needs to be reset at the end of each loop
        number = 0
        # math loop
        for i in range(0, len(gradesList), 2):
            # Shortcut for converting the list to numbers
            gradesList[i] = eval(gradesList[i])
            # Define wn and gn
            wn = gradesList[i]
            gn = eval(gradesList[i + 1%len(gradesList)])
            # Calculate each set of wn and gn
            number += (wn * gn)

        # Denominator of class average
        count += 1
        # Finalize individual averages
        number = (number) / 100
        # Numerator of class average
        total += number

        # Print the name and average of each student
        print(names + "'s average: " + str(number))

    # Class average
    total = total / count

    # Print the class average
    print("\nClass average: " + str(total))
        

    # Close the grades.txt window
    grades.close()


# Auto-run program
weightedAverage()
