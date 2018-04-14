currency = [
    [1.00, 5.00, 10.0],
    [0.75, 3.33, 4.75],
    [0.65, 3.25, 6.50]
]

# for row in currency:
#     for cell in row:
#         print('%.2f ' % cell, end='')
#     print()

# using enumerate()
for row_index, row in enumerate(currency):
    for column_index, item in enumerate(row):
        print('currency[%d][%d] is %.2f' % (row_index, column_index, item))
