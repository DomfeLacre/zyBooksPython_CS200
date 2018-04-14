# Output a menu of automotive services and the corresponding cost of each service.
print('Davy\'s auto shop services')

# Creat dict() to store services : prices
servicePrices = {
    'Oil change' : 35,
    'Tire rotation' : 19,
    'Car wash' : 7,
    'Car wax' : 12
}

print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

# Prompt the user for two services from the menu.
serviceOne = str(input('\nSelect first service: \n'))
serviceTwo = str(input('\nSelect second service: \n'))


# Check to see if input is a dash (-). If so append 'No service' : 0 to the servicesPrices[] dict()
if serviceOne == '-':
    servicePrices['No service'] = 0
    # Set the value of serviceOne to str 'No service' to achieve required assignment output
    serviceOne = 'No service'
else:
    serviceOne = serviceOne

# Check to see if input is a dash (-). If so append 'No service' : 0 to the servicesPrices[] dict()
if serviceTwo == '-':
    servicePrices['No service'] = 0
    # Set the value of serviceTwo to str 'No service' to achieve required assignment output
    serviceTwo = 'No service'
else:
    serviceTwo = serviceTwo


# Output an invoice for the services selected. Output the cost for each service and the total cost.
print('\n')
print('Davy\'s auto shop invoice\n')

# Condition to check to see if a dash(-) was entered for serviceOne input
if serviceOne == 'No service':
    print('Service 1: %s' % serviceOne)
elif serviceOne in servicePrices:
    print('Service 1: %s, $%d' % (serviceOne, servicePrices[serviceOne]))
else:
    servicePrices[serviceOne] = 0
    print('Service 1: We do not provide the service that you have requested.')

# Condition to check to see if a dash(-) was entered for serviceTwo input
if serviceTwo == 'No service':
    print('Service 2: %s' % serviceTwo)
elif serviceTwo in servicePrices:
    print('Service 2: %s, $%d' % (serviceTwo, servicePrices[serviceTwo]))
else:
    servicePrices[serviceTwo] = 0
    print('Service 2: We do not provide the service that you have requested.')

# Add total using the values from the servicePrices dict()
serviceTotal = servicePrices[serviceOne] + servicePrices[serviceTwo]


print('\nTotal: $%d' % serviceTotal)
