movieCollection = {
    'Munich': ['Steven Spielberg', 2005],
    'The Prestige': ['Christopher Nolan', 2006],
    'Spotlight': ['Tom McCarthy', 2015],
    '12 Years a Slave': ['Steve McQueen', 2013],
    'Mary and Max': ['Adam Elliot', 2009],
    'The Departed': ['Martin Scorsese', 2006],
    'The Artist': ['Michel Hazanavicius', 2011],
    'The Dark Knigh': ['Chistopher Nolan', 2008],
    'Into the Wild': ['Sean Penn', 2007],
    'The Help': ['Tate Taylor', 2011],
    'The King\'s Speech': ['Tom Hooper', 2010],
    'Argo': ['Ben Affleck', 2012],
    'The BFG': ['Steven Spielberg', 2016],
    'Birdman': ['Alejandro G. Inarritu', 2014]
}

movieInfoList = list(movieCollection.items())

### FINALLY !!!!!! ###
userInfo = int(input("Please enter a year between 2005 and 2016: \n"))
if userInfo >= 2005 and userInfo <= 2016:
    for key, value in enumerate(movieInfoList):
        if userInfo in value[1]:
            print('{}, {}'.format(value[0], value[1][0]))
else:
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

        print(menuPrompt)
        print()
    elif userChoice == 'd':

        print(menuPrompt)
        print()
    elif userChoice == 't':

        print(menuPrompt)
        print()
    else:
        break


