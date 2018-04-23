"""
Write a loop to populate user_guesses with num_guesses integers. Read integers using int(input()).
Ex: If num_guesses is 3 and user enters 9 5 2, then user_guesses is [9, 5, 2].
"""

num_guesses = 3
user_guesses = []


while num_guesses > 0:
    userInput = int(input('Enter numbers: \n'))
    user_guesses.append(userInput)
    num_guesses -= 1


print(user_guesses)
