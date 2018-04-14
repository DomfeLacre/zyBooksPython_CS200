# zyBooks Chpt.5 Exercise 5.12 Drawing a right triangle (Python 3)

print ('Enter a character: ')
triangle_char = input()

print ('Enter triangle height: ')
triangle_height = int(input())

theRange = range(triangle_height)
print(theRange)
print(len(theRange))

# i = 1
#
# while i <= triangle_height:
#     print(('%s ' % triangle_char) * i)
#     i += 1

for i in range(triangle_height):
    print(('%s ' % triangle_char) * (i + 1))

