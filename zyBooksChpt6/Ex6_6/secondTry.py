userInput = ""

while userInput != 'q':
    userInput = input("Enter string:\n")
    commaIndex = userInput.find(',')
    while commaIndex < 0 and userInput != 'q':
        print('Error: No comma in string')
        break
    if commaIndex > 0:
        userInput = userInput.split(',')
        firstWord = userInput[0].strip()
        secondWord = userInput[1].strip()
        print('First word: %s' % firstWord)
        print('Second word: %s\n' % secondWord)

