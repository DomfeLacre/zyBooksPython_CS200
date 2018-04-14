# Code: Analysis of I/O With Annotations #
# zyBooks 4.10 Auto Service Invoice Lab #


# Print out Service Invoice Header and Service Options

# Header
print('Davy\'s auto shop services')

'''
Best Practice 1: Practicality beats purity - The Service Options could have been stored as a dict(), but using the 
print() method on the individual Service Options was more practical in this situation. 

Problem Solving Approach: I had originally wanted to store the services as a dict() object so that I would later be able
to iterate through the values in order to:
a. print out the service options with a for loop and...
b. user the key:value pairs to total the final price. 
This ended up implementing much more logic than was needed for this program. Though using a dict() to store the Service 
Options would scale much better with a larger or dynamic Service Options list, removing the dict() was a choice in 
practicality over purity
'''
# Service Options
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')


# Gather User Input for Service Selections
serviceOne = input('\nSelect first service: \n')
serviceTwo = input('\nSelect second service: \n')

'''
Best Practice 2: Explicit is better than implicit - To avoid errors and maintain control over user input, we will
force all input into lower cased strings using the lower() method.

Problem Sovling Approach: Though the lab didn't require this, one could easily guess that user input could differ than
the input that we require. Therefore, a method to standardize the format of user input needs to be implemented. Forcing
all strings to lower case is step one in solving this problem. 
'''
# Store user input as lower cased strings
serviceOne = serviceOne.lower()
serviceTwo = serviceTwo.lower()

# Begin Output of Service Invoice

print('\nDavy\'s auto shop invoice\n')

'''
Best Practice 3: Simple is better than complex - A simple if-else conditional was enough to satisfy this labs
requirements which called for a small Services Options list and no error handling. 

Problem Solving Approach: I originally had written this conditional to update a dict() with the 
additional requirement of allowing the (-) dash option as key entry and setting it's value to zero. Additionally, that 
is how I handled any input other than what was allowed from the Service Options list. Though this method was more 
dynamic and I was proud of the logic I had implemented, it was to complex and brittle.vI re-wrote the entire program 
using a simple if-else condition which proved to be a much better approach to this particular problem. Setting the 
else condition to inform the user that their input was not valid was the second and final step in standardizing user 
input.
'''
# Allow for (-) input for a Service Option, store and output Service 1 and Service 2 selections along with thier
# cost. Use else case to handle undesired input.
if serviceOne == '-':
    serviceOneCost = 0;
    print('Service 1: -')
elif serviceOne == 'oil change':
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

if serviceTwo == '-':
    serviceTwoCost = 0;
    print('Service 2: -')
elif serviceTwo == 'oil change':
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

'''
Best Practice 4: Readability counts - Simply stated variables explain exactly what is happening here
'''
# Add Service 1 and Service 2 and get a Total Cost for services requested
serviceTotal = serviceOneCost + serviceTwoCost

# Print Total Cost
print('\nTotal: $%d' % serviceTotal)
