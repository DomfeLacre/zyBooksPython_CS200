userInput = ''

while userInput != 'q':
    userInput = input('Enter string:\n')
    commaIndex = userInput.find(',')
    while commaIndex == -1 and userInput != 'q':
        print('Error: no comma in string')
        break
    if commaIndex != -1:
        splitInput = userInput.split(',')
        firstWord = splitInput[0].strip()
        secondWord = splitInput[1].strip()
        print('First word: %s' % firstWord)
        print('Second word: %s\n' % secondWord)


#
# userInput = ''
# commaIndex = userInput.find(',')
#
# while userInput != 'q':
#     userInput = input('Enter input string:\n')
#     while commaIndex == -1 and userInput != 'q':
#         print('Error: No comma in string.')
#         break
#     if commaIndex != -1:
#         userInput = userInput.split(',')
#         firstWord = userInput[0].strip()
#         secondWord = userInput[1].strip()
#         print('First word: %s' % firstWord)
#         print('Second word: %s' % secondWord)
