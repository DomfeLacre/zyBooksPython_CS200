# titleData = input("Enter a title for the data: \n")
# print("You entered: %s\n" % titleData)
#
# columnOne = input("Enger the column 1 header: \n")
# print("You entered: %s\n" % columnOne)
#
# columnTwo = input("Enter the column 2 header: \n")
# print("You entered: %s\n" % columnTwo)


inputData = ''
while inputData != -1 :
    inputData = input("Enter a data point (-1 to stop input): \n")
    dataCheck = 0
    splitData = inputData.split(',')
    while inputData != -1 and inputData.find(',') == -1:
        print("Error: No comma in string.")
        dataCheck = -1
        break
    while inputData.count(',') > 1 :
        print("Error: Too many commas in input.")
        dataCheck = -1
    while


elif not intData.isdigit() :
    print("Error: Comma not followed by an integer.")
else :
    intData = int(intData)
    print("Data string: %s" % stringData)
    print("Data integer: %d" % intData)


