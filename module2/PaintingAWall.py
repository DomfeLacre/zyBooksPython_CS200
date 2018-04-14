#IMPORT Math module
import math

#OBTAIN wall height
wallHeight = float(input('Enter wall height (feet): \n'))

#OBTAIN wall length
wallLength = float(input('Enter wall width (feet): \n'))

#CALCULATE wall area (square footage) by multiplying wall height by wall length
wallArea = wallHeight * wallLength

#PRINT out the wall area
print('Wall area: %f' % wallArea)

#Assume that one gallon can of paint covers 350 square feet
#CALCULATE gallons of paint needed by divding square footage by 350
gallonsPaint = wallArea / 350

#PRINT out the number of gallons required to paint the wall
print('Paint needed: %f' % gallonsPaint)

#CALCULATE how many one gallon cans of paint would be needed by rounding up the result of the calculated gallons of paint result
cansPaint = math.ceil(gallonsPaint)

#PRINT out the number of one gallon cans required to paint the wall
print('Cans needed: %d' % cansPaint)

#OBTAIN preferred color of paint to paint the wall
colorChoice = input('Choose a color to paint the wall: \n')

#STORE price per gallon of paint for the following colors:
#Red: $35/gallon
#Blue: $25/gallon
#Green: $23/gallon
paintColors = {
    'red'   : 35,
    'blue'  : 25,
    'green' : 23
}

#CALCULATE the total cost of the of the preferred colored paint by multiplying total one gallon cans of paint needed by the
#cost per one gallon can of the preferred colored paint
totalCost = paintColors[colorChoice] * cansPaint

#PRINT out the total cost for the total amount of cans of paint of the desired color needed to paint the wall
print('Cost of purchasing %s paint: $%d' % (colorChoice, totalCost))

