
# Prompt user for a set of grades each seperated by a space. Ex 1 2 3 4
gradeList = [int(i) for i in input("Enter grades: \n").split()]
highGrade = 0;
lowGrade = 0;
avgGrade = 0;
gradeTotal = 0;

for grade in range(len(gradeList)):
    gradeTotal += gradeList[grade]
    if gradeList[grade] > highGrade:
        highGrade = gradeList[grade]
        lowGrade = gradeList[grade]
for grade in range(len(gradeList)):
    if gradeList[grade] < lowGrade:
        lowGrade = gradeList[grade]

avgGrade = gradeTotal / len(gradeList)
print(highGrade, lowGrade, avgGrade)


