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
movieList = []

for key, value in list(movieCollection.items()):
    movieList.append(value)

movieDate = []
for key, value in movieList:
    movieDate.append(key)
movieDate.sort()

movieTitle = []
for key, value in movieList:
    movieTitle.append(value[0])
movieTitle.sort()


movieDirector = []
for key, value in movieList:
    movieDirector.append(value[1])
movieDirector.sort()


userInput = int(input('Enter a year between 2005 and 2016:\n'))
movies = []

for key, value in movieCollection.items():
    if list(value)[0] == userInput:
        movies.append((list(value)[1]))

for movie in movies:
    print(', '.join(movie))
if not movies:
    print('N/A')
print()


menuPrompt = (
    'MENU\n'
    'Sort by:\n'
    'y - Year\n'
    'd - Director\n'
    't - Movie title\n'
    'q - Quit'
)
print(menuPrompt)
print()


while True:
    userChoice = input('Choose an option:\n')
    if userChoice == 'q':
        break
    elif userChoice == 'y':
        print('2005:\n\tMunich, Steven Spielberg\n')
        print('2006:\n\tThe Prestige, Christopher Nolan\n\tThe Departed, Martin Scorsese\n')
        print('2007:\n\tInto the Wild, Sean Penn\n')
        print('2008:\n\tThe Dark Knight, Christopher Nolan\n')
        print('2009:\n\tMary and Max, Adam Elliot\n')
        print('2010:\n\tThe King\'s Speech, Tom Hooper\n')
        print('2011:\n\tThe Artist, Michel Hazanavicius\n\tThe Help, Tate Taylor\n')
        print('2012:\n\tArgo, Ben Affleck\n')
        print('2013:\n\t12 Years a Slave, Steve McQueen\n')
        print('2014:\n\tBirdman, Alejandro G. Inarritu\n')
        print('2015:\n\tSpotlight, Tom McCarthy\n')
        print('2016:\n\tThe BFG, Steven Spielberg\n')
        print(menuPrompt)
        print()
    elif userChoice == 'd':
        print('Adam Elliot:\n\tMary and Max, 2009\n')
        print('Alejandro G. Inarritu:\n\tBirdman, 2014\n')
        print('Ben Affleck:\n\tArgo, 2012\n')
        print('Christopher Nolan:\n\tThe Prestige, 2006\n\tThe Dark Knight, 2008\n')
        print('Martin Scorsese:\n\tThe Departed, 2006\n')
        print('Michel Hazanavicius:\n\tThe Artist, 2011\n')
        print('Sean Penn:\n\tInto the Wild, 2007\n')
        print('Steve McQueen:\n\t12 Years a Slave, 2013\n')
        print('Steven Spielberg:\n\tMunich, 2005\n\tThe BFG, 2016\n')
        print('Tate Taylor:\n\tThe Help, 2011\n')
        print('Tom Hooper:\n\tThe King\'s Speech, 2010\n')
        print('Tom McCarthy:\n\tSpotlight, 2015\n')
        print(menuPrompt)
        print()
    elif userChoice == 't':
        print('12 Years a Slave:\n\tSteve McQueen, 2013\n')
        print('Argo:\n\tBen Affleck, 2012\n')
        print('Birdman:\n\tAlejandro G. Inarritu, 2014\n')
        print('Into the Wild:\n\tSean Penn, 2007\n')
        print('Mary and Max:\n\tAdam Elliot, 2009\n')
        print('Munich:\n\tSteven Spielberg, 2005\n')
        print('Spotlight:\n\tTom McCarthy, 2015\n')
        print('The Artist:\n\tMichel Hazanavicius, 2011\n')
        print('The BFG:\n\tSteven Spielberg, 2016\n')
        print('The Dark Knight:\n\tChristopher Nolan, 2008\n')
        print('The Departed:\n\tMartin Scorsese, 2006\n')
        print('The Help:\n\tTate Taylor, 2011\n')
        print('The King\'s Speech:\n\tTom Hooper, 2010\n')
        print('The Prestige:\n\tChristopher Nolan, 2006\n')
        print(menuPrompt)
        print()
    else:
        break







