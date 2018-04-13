#Gather customer order include item, quantity and price and add to receipt before proceeding with next order:
print('Please enter the name, quantity, and price of the food order when prompted')

itemOneName = input("Enter food item 1 name: ")
itemOneQuantity = int(input("Enter food item 1 quantity: "))
itemOnePrice = float(input("Enter food item 1 price: "))

print('\n')
print('Item 1: ', itemOneName)
print('Quantity: ', itemOneQuantity)
print('Price: $', itemOnePrice)

subTotal = (itemOnePrice * itemOneQuantity)
salesTax = (subTotal * 0.06)
grandTotal = (subTotal + salesTax)
salesTax = float("{0:.2f}".format(salesTax))

print('Subtotal: $', subTotal)
print('Sales Tax (6%): $', salesTax)
print('Total: $', grandTotal)

