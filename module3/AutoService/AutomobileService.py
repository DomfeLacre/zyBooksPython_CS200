# (1) Prompt the user for an automobile service. Output the user's input. (1 pt)
#
# Ex:
#
# Enter desired auto service: Oil change
# You entered: Oil change
#
#
# (2) Output the price of the requested service. (4 pts)
#
# Ex:
#
# Cost of oil change: $35
#
#
# The program should support the following services:
#
#     Oil change -- $35
#     Tire rotation -- $19
#     Car wash -- $7
#
# If the user enters a service that is not listed above, then output the following error message:
#
# Error: Requested service is not recognized.

serviceType = input('Enter desired auto service: \n')

print('You entered:', serviceType)

serviceType = serviceType.lower()
servicePrices = {
    'oil change' : 35,
    'tire rotation' : 19,
    'car wash' : 7
}

if serviceType in servicePrices:
    print('\nCost of %s: $%d' % (serviceType, servicePrices[serviceType]))
else:
    print('\nError: Requested service is not recognized.')
