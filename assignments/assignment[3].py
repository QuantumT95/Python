"""
Charlie Tran
Assignment #3
COSC 1306
"""


################################################################################
# Write a function to determine a letter grade given a final average(float) value.
# It should take as an input parameter a number with which to find the grade.
# It should execute a number of if statements to determine the letter grade.
# It should then return that letter grade without printing.
################################################################################
def letter_grade(finalAvg):
    if finalAvg >= 90:
        letterGrade = "A"
    elif finalAvg < 90 and finalAvg >= 86:
        letterGrade = "A-"
    elif finalAvg < 86 and finalAvg >= 82:
        letterGrade = "B+"
    elif finalAvg < 82 and finalAvg >= 78:
        letterGrade = "B"
    elif finalAvg < 78 and finalAvg >= 74:
        letterGrade = "B-"
    elif finalAvg < 74 and finalAvg >= 70:
        letterGrade = "C+"
    elif finalAvg < 70 and finalAvg >= 66:
        letterGrade = "C"
    elif finalAvg < 66 and finalAvg >= 62:
        letterGrade = "C-"
    elif finalAvg < 62 and finalAvg >= 58:
        letterGrade = "D+"
    elif finalAvg < 58 and finalAvg >= 54:
        letterGrade = "D"
    elif finalAvg < 54 and finalAvg >= 50:
        letterGrade = "D-"
    else:
        letterGrade = "F"

    print()
    print("Congratulations, you earned a/an", letterGrade)
    print("========================================")


################################################################################
# *** Optional Bonus ***
################################################################################
# Write a function to determine the points needed for the next higher letter grade
# given a final average(float) value.
# It should take as an input parameter a number with which to find the next higher
# grade and the points needed to earn it.
# It should execute a number of if statements to determine and print out the higher
# the letter grade and points needed to reach it.
################################################################################

def pointsNeeded(grade):
    if grade >= 90:
        print("You've earned the maximum grade allowed")
    elif grade < 90 and grade >= 86:
        grade -= 90
        print("You're", abs(grade), "points away from an A")
    elif grade < 86 and grade >= 82:
        grade -= 86
        print("You're", abs(grade), "points away from an A-")
    elif grade < 82 and grade >= 78:
        grade -= 82
        print("You're", abs(grade), "points away from an B+")
    elif grade < 78 and grade >= 74:
        grade -= 78
        print("You're", abs(grade), "points away from an B")
    elif grade < 74 and grade >= 70:
        grade -= 74
        print("You're", abs(grade), "points away from an B-")
    elif grade < 70 and grade >= 66:
        grade -= 70
        print("You're", abs(grade), "points away from an C+")
    elif grade < 66 and grade >= 62:
        grade -= 66
        print("You're", abs(grade), "points away from an C")
    elif grade < 62 and grade >= 58:
        grade -= 62
        print("You're", abs(grade), "points away from an C-")
    elif grade < 58 and grade >= 54:
        grade -= 58
        print("You're", abs(grade), "points away from an D+")
    elif grade < 54 and grade >= 50:
        grade -= 54
        print("You're", abs(grade), "points away from an D")
    else:
        grade -= 50
        print("You're", abs(grade), "points away from an D-")

################################################################################
# Main Body of the program
################################################################################
# Write an input statement to get a course final average(float) from the user.
# Call the function to determin the letter grade an print a message with that grade.
# Optionally, call the function to determine the next higher grade.
################################################################################


finalAvg = float(input("Please enter a final average: "))
letter_grade(finalAvg)
pointsNeeded(finalAvg)
