import re

total = 0

with open('Day2Input.txt') as file:
        for line in file:
            #get dimensions per line and store in array
            dimensions = re.findall('\d+', line)
            #conver that contents to integer
            mapToInt = map(int, dimensions)
            #set array to individual variables
            length = mapToInt[0]
            width = mapToInt[1]
            height = mapToInt[2]
            #compute multiplication
            lengthWidth = length * width
            lengthHeight = length * height
            widthHeight = width * height
            #set slack
            slack = min(lengthWidth, lengthHeight, widthHeight)

            total += ((2 * lengthWidth +
                      2 * lengthHeight +
                      2 * widthHeight) +
                      slack)
                      
print total
