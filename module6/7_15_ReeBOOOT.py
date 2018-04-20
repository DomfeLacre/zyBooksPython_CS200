movieCollection = {
    2005: ['Munich', 'Steven Spielberg'],
    2006: ['The Prestige', 'Christopher Nolan', 'The Departed', 'Martin Scorsese'],
    2007: ['Into the Wild', 'Sean Penn'],
    2008: ['The Dark Knight', 'Christopher Nolan'],
    2009: ['Mary and Max', 'Adam Elliot'],
    2010: ['The King\'s Speech', 'Tom Hooper'],
    2011: ['The Artist', 'Michel Hazanavicius', 'The Help', 'Tate Taylor'],
    2012: ['Argo', 'Ben Affleck'],
    2013: ['12 Years a Slave', 'Steve McQueen'],
    2014: ['Birdman', 'Alejandro G. Inarritu'],
    2015: ['Spotlight', 'Tom McCarthy'],
    2016: ['The BFG', 'Steven Spielberg']
}

userInput = 2007
movieKeyList = list(movieCollection.keys())
movieValueList = list(movieCollection.values())
movieItemsList = list(movieCollection.items()) # --> becomes tuples containing lists
# movieItemsList = list(movieItemsList) # --> becomes a list containing tuples and lists
# print(movieItemsList)
# print(movieItemsList)
# print(movieItemsList[0][1])

for collection in movieItemsList:
    # print(collection) # tuples containing a mutable list: (2016, ['The BFG', 'Steven Spielberg'])
    year, movie = collection
    if year == userInput:
        print(len(collection[1]))
        print(type(movie))
        print(len(movie))
    #     print(', '.join(movie))


# for key, value in movieItemsList:
#     if key == userInput:
#         newList = []



# for key, value in enumerate(movieItemsList):
#     if value[0] == userInput:

# strItem = str(testItem)
# strItem = strItem.strip('[]')
# print(strItem)
# for i in movieItemsList:
#     for j in i:
#         if type(j) == list:
#             print(j)
