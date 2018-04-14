# zyBooks Chpt.5 Exercise 5.13 Drawing a half arrow (Python 3)

print ('Enter arrow base height: ')
arrow_base_height = int(input())

print ('Enter arrow base width: ')
arrow_base_width = int(input())

print ('Enter arrow head width: ')
arrow_head_width = int(input())
while arrow_head_width <= arrow_base_width:
    print ('Please enter an arrow head width that is larger than the arrow base: ')
    arrow_head_width = int(input())
arrow_head_width = arrow_head_width

for symbol in range(arrow_base_height):
    print(('*') * arrow_base_width)

i = arrow_head_width
for symbol in range(arrow_head_width):
    print(('*') * i)
    i -= 1
