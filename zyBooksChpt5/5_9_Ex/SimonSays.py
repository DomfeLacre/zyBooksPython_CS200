user_score = 0
check_score = 0
simon_pattern = 'RRGBRYYBGY'
user_pattern  = 'RRGBBRYBGY'

while user_score == check_score:
    for i in simon_pattern:
        for j in user_pattern:
            if j == i:
                user_score += 1
                check_score += 1
                break
            else:
                check_score = 0
                break
        if check_score == user_score:
            continue




print('User score:', user_score)
