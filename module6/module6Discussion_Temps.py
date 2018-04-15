temperatures = [ [32, 86, 212] , [0, 30, 100], [273, 303, 373]]


# print(temperatures[1][1])

userInput = temperatures[0][1]

for temp_row, row in enumerate(temperatures):
    for temp_index, temp in enumerate(row):
        print('Row: %d, Cell: %d, Temperature: %d' % (temp_row, temp_index, temp))

if userInput == temperatures[0][1]:

  print('Equivalent temp in Kelvin is: %d' % temperatures[2][1])
