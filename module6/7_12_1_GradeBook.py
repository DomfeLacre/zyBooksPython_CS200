 # Write a program that uses the keys(), values(), and/or items() dict methods to find statistics about
 # the student_grades dictionary. Find the following:
 #    Print the name and grade percentage of the student with the highest total of points
 #    Find the average score of each assignment.
 #    Find and apply a curve to each student's total score, such that the best student has 100% of the total points.


# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Colin': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Mary': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}


gradeTotal = 0
topStudent = ''
avgGrade = 0
for key, value in student_grades.items():
    if sum(value) > gradeTotal:
        gradeTotal = sum(value)
        topStudent = key
        avgGrade = gradeTotal / len(value)
print('%s, with a grade percentage of %.2f, is our Top Student!' % (topStudent, avgGrade))

# for key in student_grades:
#     print(student_grades.get(key))

# gradeTotal = 0
#
# for value in list(student_grades.values()):
#     print(sum(value))
#     if sum(value) > gradeTotal:
#         gradeTotal = sum(value)
#         print(sum(value))
#
# print(gradeTotal)



