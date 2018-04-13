print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

serviceOne = input('\nSelect first service: \n')
serviceTwo = input('\nSelect second service: \n')
serviceOne = serviceOne.lower()
serviceTwo = serviceTwo.lower()

print('\nDavy\'s auto shop invoice\n')
if serviceOne == 'oil change':
    serviceOneCost = 35
    print('Service 1: Oil change, $35')
elif serviceOne == 'tire rotation':
    serviceOneCost = 19
    print('Service 1: Tire rotation, $19')
elif serviceOne == 'car wash':
    serviceOneCost = 7
    print('Service 1: Car wash, $7')
elif serviceOne == 'car wax':
    serviceOneCost = 12
    print('Service 1: Car wax, $12')
else:
    serviceOneCost = 0
    print('I am sorry, we do not offer that service')

if serviceTwo == 'oil change':
    serviceTwoCost = 35
    print('Service 2: Oil change, $35')
elif serviceTwo == 'tire rotation':
    serviceTwoCost = 19
    print('Service 2: Tire rotation, $19')
elif serviceTwo == 'car wash':
    serviceTwoCost = 7
    print('Service 1: Car wash, $7')
elif serviceTwo == 'car wax':
    serviceTwoCost = 12
    print('Service 1: Car wax, $12')
else:
    serviceTwoCost = 0
    print('I am sorry, we do not offer that service')

serviceTotal = serviceOneCost + serviceTwoCost

print('\nTotal: $%d' % serviceTotal)
