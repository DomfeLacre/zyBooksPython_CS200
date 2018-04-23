movieCollection = {
    'movie1': (2005, ['Munich', 'Steven Spielberg']),
    'movie2': (2006, ['The Prestige', 'Christopher Nolan']),
    'movie3': (2006, ['The Departed', 'Martin Scorsese']),
    'movie4': (2007, ['Into the Wild', 'Sean Penn']),
    'movie5': (2008, ['The Dark Knight', 'Christopher Nolan']),
    'movie6': (2009, ['Mary and Max', 'Adam Elliot']),
    'movie7': (2010, ['The King\'s Speech', 'Tom Hooper']),
    'movie8': (2011, ['The Artist', 'Michel Hazanavicius']),
    'movie9': (2011, ['The Help', 'Tate Taylor']),
    'movie10': (2012,['Argo', 'Ben Affleck']),
    'movie11': (2013,['12 Years a Slave', 'Steve McQueen']),
    'movie12': (2014,['Birdman', 'Alejandro G. Inarritu']),
    'movie13': (2015,['Spotlight', 'Tom McCarthy']),
    'movie14': (2016,['The BFG', 'Steven Spielberg'])
}
print('dict.items() ==\n{}'.format(movieCollection.items()))
print()
print('dict.keys() ==\n{}'.format(movieCollection.keys()))
print()
print('dict.values() ==\n{}'.format(movieCollection.values()))
print()
print('dict.values() converted to a list ==\n{}'.format(list(movieCollection.values())))
print(type(list(movieCollection.values())))
dictValueList = list(movieCollection.values())
print()
movieList = list(movieCollection.values())
print('dictionary cast to a list ==\n{}'.format(movieList))
print()
print('new list information at index[0] ==\n{}'.format(movieList[0]))
print()
print(type(movieList[0]))
newList = ['key', 1, 'horses']
print('dictValueList[0] ==\n{}'.format(dictValueList[0]))
print('dictValueList[1] ==\n{}'.format(dictValueList[1]))

print('for loop to go through dictValueList:\n')
for key, value in enumerate(dictValueList):
    print('key = {}, value = {}'.format(key, value))
    print('value at [0] = {}'.format(value[0]))
    print('value(s) at [1] = {}'.format(value[1]))
    for i in value:
        print('values = {}'.format(i))
    for j in value[1]:
        print('value(s) in dictValueList(value[1] sub-list = {}'.format(j))
    if value[0] == 2011:
        for j in value[1]:
            print(j)
