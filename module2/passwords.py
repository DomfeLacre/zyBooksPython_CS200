# FIXME (1): Finish reading another word and an integer into variables.
# Output all the values on a single line
favoriteColor = input('Enter favorite color: \n')
favoritePet = input('Enter pet\'s name: \n')
favoriteNumber = int(input('Enter a number: \n'))

print('\n')
print('%s %s %d' % (favoriteColor, favoritePet, favoriteNumber))

# FIXME (2): Output two password options
password1 = favoriteColor + '_' + favoritePet
password2 = str(favoriteNumber) + favoriteColor + str(favoriteNumber)
print('\n')
print('First password:', password1)
print('Second password:', password2)



# FIXME (3): Output the length of the two password options
lenPasswd1 = len(password1)
lenPasswd2 = len(password2)
# Number of characters in yellow_Daisy: 12
print('\n')
print('Number of characters in %s: %d' % (password1, lenPasswd1) )
print('Number of characters in %s: %d' % (password2, lenPasswd2) )
