import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt

USE_MILLIMETERS = True

tree = ET.parse("TestFiles/Tomtest3.svg")
root = tree.getroot()

print(type(root))

print(root.attrib)

print(root[0].attrib)

print(type(root[0]))

for child in root:
    print(child.attrib)
    print(child.tag)

print(root[0].attrib['d'])
#*****Extract additional data **
Colors = [] #list of string colors
strokeWidths = [] # list of stroke widths as floats

#*********** Parsing ***********
print("**************Parsing")

childLst = []
for child in root:
    childLst.append(child.attrib)

lineCollection = []# Stores all lines as [[[xPoint1,yPoint1],[xPoint2,yPoint2]],[[xPoint1,yPoint1],[xPoint2,yPoint2]]]
lineXCollection = []# Stores all X values as a list X values per each line ie. list of x coord. list
lineYCollection = []# Stores all Y values as a list Y values per each line ie. list of y coord. list

for child in childLst:
    Coords = child["d"]

    LinesSTR = Coords.strip("M")
    LinesSTR = LinesSTR.strip("Z")
    LinesSTR = LinesSTR.split("L")
    print(LinesSTR)

    Lines = []
    LinesX = []
    LinesY = []
    for line in LinesSTR:
        coordList = line.split(",")
        print(coordList)
        if USE_MILLIMETERS:
            x=float(coordList[0])/11.811024
            LinesX.append(x)
            y=float(coordList[1])/11.811024
            LinesY.append(y)
        else:
            x=float(coordList[0])
            LinesX.append(x)
            y=float(coordList[1])
            LinesY.append(y)
        point = [x,y]
        Lines.append(point)
    print(Lines)
    lineCollection.append(Lines)
    lineXCollection.append(LinesX)
    lineYCollection.append(LinesY)
        
            

'''
xCoordsSTR = Coords.split("L")[0]
xCoordsSTR = xCoordsSTR.strip("M")
xCoords_ = xCoordsSTR.split(',')
xCoords = []

for x in xCoords_:
    xCoords.append(float(x)/11.811024)

yCoordsSTR = Coords.split("L")[1]
yCoords_ = yCoordsSTR.split(',')
yCoords = []

for y in yCoords_:
    yCoords.append(float(y)/11.811024)

yCoords.reverse()


print(xCoords)
print(yCoords)

'''

#***********Debug Display***********
print("***********Debug Display***********")
for i in range(0,len(lineXCollection)):
    plt.plot(lineXCollection[i],lineYCollection[i])
plt.show()

