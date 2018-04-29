testSTring = "we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  " \
             "yes; more volunteers, more civilians,  more teachers in space.  nothing ends here;  " \
             "our hopes and our journeys continue!"

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
    return holdMahString, count

testString = "i want some water. he has some. maybe he can give me some. i think I will ask."

fix_capitalization(testString)
