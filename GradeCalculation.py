# Calculates the overall grade for four equally-weighted programming assignments,
# where each assignment is graded out of 50 points.
# Hint: First calculate the percentage for each assignment (e.g., score / 50),
# then calculate the overall grade percentage (be sure to multiply the result by 100).

assignOne = float(input('Enter score on Assignment 1 (out of 50):\n'))
assignTwo = float(input('Enter score on Assignment 2 (out of 50):\n'))
assignThree = float(input('Enter score on Assignment 3 (out of 50):\n'))
assignFour = float(input('Enter score on Assignment 4 (out of 50):\n'))

percentOne = (assignOne / 50) * 100
percentTwo = (assignTwo / 50) * 100
percentThree = (assignThree / 50) * 100
percentFour = (assignFour / 50) * 100

overallGrade = (assignOne + assignTwo + assignThree + assignFour) / 4

print('Your overall grade is:', overallGrade)


#


