itemName = input('Enter food item name: \n')
itemPrice = float(input('Enter item price: \n'))
itemQuantity = int(input('Enter item quantity: \n'))
totalCost = (itemPrice * itemQuantity)

print('\nRECEIPT')
print(itemQuantity, itemName, '@ $', itemPrice, '= $', totalCost)
print("Total cost: $", totalCost)

print('\n')
itemName2 = input('Enter second food item name: \n')
itemPrice2 = float(input('Enter item price: \n'))
itemQuantity2 = int(input('Enter item quantity: \n'))
totalCost2 = itemPrice2 * itemQuantity2

combinedCost = totalCost + totalCost2

print('\nRECEIPT')
print(itemQuantity, itemName, '@ $', itemPrice, '= $', totalCost)
print(itemQuantity2, itemName2, '@ $', itemPrice2, '= $', totalCost2)
print('Total cost: $', combinedCost)

# FIXME (3): Add a gratuity and total with tip to the second receipt
gratuity = (combinedCost * 0.15)
taxAndTotal = combinedCost + gratuity
print('\n15% gratuity: $', gratuity)
print('Total with tip: $', taxAndTotal)
