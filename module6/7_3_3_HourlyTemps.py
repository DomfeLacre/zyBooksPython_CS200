"""
Write a loop to print all elements in hourly_temperature. Separate elements with a -> surrounded by spaces.
Sample output for the given program:

90 -> 92 -> 94 -> 95

Note: 95 is followed by a space, then a newline.
"""

hourly_temperature = [90, 92, 94, 95]

count = 0
for temp in hourly_temperature:
    count += 1
    if count == len(hourly_temperature):
        print('%s ' % temp)
    else:
        print('%s -> ' % temp, end='')
