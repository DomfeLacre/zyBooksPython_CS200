mult_table = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]

for row in mult_table:

    for cell in row:
        if row.index(cell) == len(mult_table[row.index(cell)]) - 1:
             print('%d' % cell)
        else:
             print('%d | ' % cell, end='')

# movieOne = {
#     'Title' : 'Predetor',
#     'Release Date' : 1985,
#     'Genre': 'Comedy'
# }
#
# movieTwo = {
#     'Title': 'Cowboys',
#     'Release Date': 1975,
#     'Genre': 'Comedy'
# }
#
# database = {
#     '1' : movieOne,
#     '2' : movieTwo
# }
#
#
# for key, value in database:
#     print(key[value])

