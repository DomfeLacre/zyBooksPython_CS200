# (1) Prompt the user to input an integer between 0 and 155, a float, a character, and a string, storing each into separate vari# ables. Then, output those four values on a single line separated by a space. (Submit for 2 points). 

userInt = int(input('Enter integer (0 - 155): \n'))
userFloat = float(input("Enter a float number such as 2.0: \n"))
userChar = input("Enter a single character such as 'g'. We will later convert that to Unicode: \n")
userString = input("Enter a string such as \"the dog runs fast\": \n")
userUni = ord(userChar)

myCombo = (userInt, userFloat, userChar, userString)
reverseCombo = (userString, userChar, userFloat, userInt)

print(myCombo)
print(reverseCombo)
print(userUni)
