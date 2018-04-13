# print('Two-letter domain names:')
#
# letter1 = 'a'
# letter2 = '?'
# while letter1 <= 'z':  # Outer loop
#     letter2 = 'a'
#     while letter2 <= 'z':  # Inner loop
#         print('%s%s.com' % (letter1, letter2))
#         letter2 = chr(ord(letter2) + 1)
#     letter2 = 0
#     while letter2 <= 9:
#         print('%s%s.com' % (letter1, letter2))
#         letter2 += 1
#     letter1 = chr(ord(letter1) + 1)


num_rows = 2
num_cols = 3

while num_rows > 0:
    for i in range(num_cols):
        print('*', end=' ')
    print('')
    num_rows -= 1
