# zyBooks Chpt.5 Exercise 5.9.1 Simon says (Python 3)

user_score = 0
simon_pattern = 'RRGBRYYBGY'
user_pattern  = 'RRGBBRYBGY'

print(range(len(simon_pattern)))

for letter in range(len(simon_pattern)):
    if simon_pattern[letter] == user_pattern[letter]:
        user_score += 1
    else:
        break

print('User score:', user_score)
