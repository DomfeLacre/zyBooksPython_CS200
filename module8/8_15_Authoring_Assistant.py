# Type all other functions here


def get_num_of_non_WS_characters(usrStr):
    count = 0
    non_ws_string = ''.join(usrStr.split())
    for char in non_ws_string:
        count += 1
    print("Number of non-whitespace characters: {}\n".format(count))
    return count

def get_num_of_words(usrStr):
    word_count = len(usrStr.split())
    print("Number of words: {}\n".format(word_count))
    return word_count

def fix_capitalization(usrStr):
    holdMahString = ""
    count = 0
    for sentence in usrStr.split('. '):
        holdMahString += (sentence.strip().capitalize() + ". ")
    for char in holdMahString:
        if char.isupper():
            count += 1
    holdMahString = holdMahString.replace("i ", "I ")
    print("Number of letters capitalized: {}".format(count))
    print("Edited text: {}\n".format(holdMahString))
    return count

def replace_punctuation(usrStr, exclamationCount, semicolonCount):
    print("Punctuation replaced")
    print("exclamationCount: {}".format(exclamationCount.count('!')))
    print("semicolonCount: {}".format(semicolonCount.count(';')))
    noExcitment = usrStr.replace('!', '.')
    noDualMeaning = noExcitment.replace(';', ',')
    print("Edited text: {}".format(noDualMeaning))


def shorten_space(usrStr):
    print("Edited text: {}".format(' '.join(usrStr.split())))


def print_menu(usrStr):
    while True:
        print('MENU\n'
              'c - Number of non-whitespace characters\n'
              'w - Number of words\n'
              'f - Fix capitalization\n'
              'r - Replace punctuation\n'
              's - Shorten spaces\n'
              'q - Quit\n')

        menuOp = input('Choose an option: \n')

        if menuOp == 'q':
            break
        elif menuOp == 'c':
            get_num_of_non_WS_characters(usrStr)
        elif menuOp == 'w':
            get_num_of_words(usrStr)
        elif menuOp == 'f':
            fix_capitalization(usrStr)
        elif menuOp == 'r':
            replace_punctuation(usrStr, usrStr, usrStr)
        elif menuOp == 's':
            shorten_space(usrStr)
        else:
            print("Please enter a valid Menu selection - \n")

    return menuOp, usrStr


userInput = input("Enter a sample text: \n")
print("You entered: {}\n".format(userInput))

menuChoice, userString = print_menu(userInput)

