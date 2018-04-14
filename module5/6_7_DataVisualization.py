# titleData = input("Enter a title for the data: ")
# print("You entered: %s\n" % titleData)
#
# columnOne = input("Enter the column 1 header: ")
# print("You entered: %s\n" % columnOne)
#
# columnTwo = input("Enter the colunm 2 header: ")
# print("You entered: %s\n" % columnTwo)

dataPoints = ""
while dataPoints != -1:
    dataPoints = input("Enter a data point (-1 to stop input): ")
    print(dataPoints.isalnum())
    splitData = dataPoints.split(',')
    if dataPoints.find(',') == -1:
        print("Error: No comma in string.")
    elif dataPoints.count(',') > 1:
        print("Error: Too many commas in input.")
    elif
        print("Error: Comma not followed by an integer.")
    else:
        stringList = []
        intList = []
        stringList.append(splitData[0])
        intList.append(int(splitData[1]))
        print("Data string: %s" % stringList[0])
        print("Data integer: {0}".format(intList[0]))

