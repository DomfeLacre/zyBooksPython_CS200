movieCollection = {
    1: {"release_date": 2005, "movie_title": "Munich", "director": "Steven Spielberg"},
    2: {"release_date": 2006, "movie_title": "The Prestige", "director": "Christopher Nolan"},
    3: {"release_date": 2006, "movie_title": "The Departed", "director": "Martin Scorsese"},
    4: {"release_date": 2007, "movie_title": "Into the Wild", "director": "Sean Penn"},
    5: {"release_date": 2008, "movie_title": "The Dark Knight", "director": "Christopher Nolan"},
    6: {"release_date": 2009, "movie_title": "Mary and Max", "director": "Adam Elliot"},
    7: {"release_date": 2010, "movie_title": "The King's Speech", "director": "Tom Hooper"},
    8: {"release_date": 2011, "movie_title": "The Artist", "director": "Michel Hazanavicius"},
    9: {"release_date": 2011, "movie_title": "The Help", "director": "Tate Taylor"},
    10: {"release_date": 2012, "movie_title": "Argo", "director": "Ben Affleck"},
    11: {"release_date": 2013, "movie_title": "12 Years a Slave", "director": "Steve McQueen"},
    12: {"release_date": 2014, "movie_title": "Birdman", "director": "Alejandro G. Inarritu"},
    13: {"release_date": 2015, "movie_title": "Spotlight", "director": "Tom McCarthy"},
    14: {"release_date": 2016, "movie_title": "The BFG", "director": "Steven Spielberg"}
}

movieList = list(movieCollection)
print(movieCollection[1]["director"])

for key in movieCollection:
    print(movieCollection[key]["director"])
# for key in movieCollection:
#     movieList.append(movieCollection[key]["movie_title"])
#
# print(movieList)


# yearPrompt = int(input("Enter a year between 2005 and 2016: "))
#
# if 2005 <= yearPrompt <= 2016:
#     for key, value in movieCollection.items():
#         if yearPrompt == value["release_date"]:
#             print("{}, {}".format(value["movie_title"], value["director"]))
# else:
#     print("N/A")
#
# print()
# menuPrompt = (
#     'MENU\n'
#     'Sort by:\n'
#     'y - Year\n'
#     'd - Director\n'
#     't - Movie title\n'
#     'q - Quit'
# )
# print(menuPrompt)
# print()

