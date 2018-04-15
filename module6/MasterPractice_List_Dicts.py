##### LISTS #####

# Accessing an Index of a List based on user input of a number: Enter 1 -5
ageList = [117, 115, 99, 88, 122]

# Ways to to get INDEX value of a LIST:
print(ageList.index(99))  # --> 2

# Use ENUMERATE to get INDEX and VALUE of LIST:
for index, value in enumerate(ageList):
    print(index)
    print('My index is %d and my index value is %d' % (index, value))

# REMEMBER Lists are 0 Index so if user input wants the value of 1 in the list that is EQUAL to 0:
userInput = 2
print('The user wants the number %d value in the list so we need to access the list accordingly: ' % userInput)
print('%d is equal to %d' % (userInput, ageList[userInput - 1]))
