user_age_years = int(input('How many years old are your? :\n'))
user_age_days = user_age_years * 365
user_age_hours = user_age_days * 24
user_age_minutes = user_age_days * 60
user_age_seconds = user_age_minutes * 60
user_heartBeats = user_age_minutes * 72
#Estimated number of sneezes per day = 1.2 times https://leinbachservices.com/times-average-person-sneeze-day-2/
#Average number of calories burnt per day = 2000 https://www.livestrong.com/article/278257-how-many-calories-does-the-body-naturally-burn-per-day/
#Average number of calories in a hamburger: 438 https://www.livestrong.com/article/306441-how-many-calories-does-a-hamburger-have/
userSneezes = 1.2 * user_age_days
hamburgerPerDay = 2000 / 438

print('You are %d days old' % user_age_days)
print('You are %d minutes old' % user_age_minutes)
print('You are %d seconds old' % user_age_seconds)
print('Your heart has beat about %d times in your life so far' % user_heartBeats)
print('You have sneezed aproximately %d time in your lifetime' % userSneezes)
print('You burn an average of 2000 calories per day. That is the equivalent of %d hamburgers' % hamburgerPerDay)

