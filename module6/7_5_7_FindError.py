tictactoe = [
    ['X', 'O', 'O'],
    ['O', 'O', 'X'],
    ['X', 'X', 'X']
]

# Check for 3 Xs in one row
# (Doesn't check columns or diagonals)
for row in tictactoe:
    num_X_in_row = 0
    for square in row:
        if square == 'X':
            num_X_in_row += 1
    if num_X_in_row == 3:
        print('X wins!')
        break
else:
    print("Cat's game!")
