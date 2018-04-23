import math
# 7.13 Warm up: People's weights (Lists) (Python 3)
#
# (1) Prompt the user to enter four numbers, each corresponding to a person's weight in pounds. Store all weights in a list. Output the list. (2 pts)
#
# Ex:
#
# Enter weight 1: 236
# Enter weight 2: 89.5
# Enter weight 3: 176.0
# Enter weight 4: 166.3
#
#Weights: [236.0, 89.5, 176.0, 166.3]

userWeights = []
maxPrompts = 1
while maxPrompts <= 4:
    userInput = float(input('Enter weight {}: \n'.format(maxPrompts)))
    maxPrompts += 1
    userWeights.append(userInput)
print()
print('Weights: {}'.format(userWeights))

#
# (2) Output the average of the list's elements. (1 pt)
avgWeight = sum(userWeights) / len(userWeights)
print('Average weight: %.2f' % avgWeight)
#
# (3) Output the max list element. (1 pt)
#
# Ex:
#
# Enter weight 1: 236
# Enter weight 2: 89.5
# Enter weight 3: 176.0
# Enter weight 4: 166.3
maxWeight = max(userWeights)
print('Max weight: %.1f' % maxWeight)
#
# Weights: [236.0, 89.5, 176.0, 166.3]
# Average weight: 166.95
# Max weight: 236.0
#
# (4) Prompt the user for a number between 1 and 4. Output the weight at the user specified location and the corresponding value in kilograms. 1 kilogram is equal to 2.2 pounds. (3 pts)
#
# userTest = 1
# print(userWeights[userTest -1])
# print(type(userWeights[userTest - 1]))
userIndex = int(input('Enter a list index (1 - 4): \n'))
print('Weight in pounds: %.1f' % userWeights[userIndex -1])
print('Weight in kilograms: %.1f\n' % (math.ceil(userWeights[userIndex -1] * 0.45)))

#Ex:
#
# Enter a list index (1 - 4): 3
# Weight in pounds: 176.0
# Weight in kilograms: 80.0
#
# (5) Sort the list's elements from least heavy to heaviest weight. (2 pts)
#
reverseWeights = userWeights[:]
reverseWeights.sort()
print('Sorted list: {}'.format(reverseWeights))

# Ex:
#
# Sorted list: [89.5, 166.3, 176.0, 236.0]
# '''
