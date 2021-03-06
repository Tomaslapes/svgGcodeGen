import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt

USE_MILLIMETERS = True

tree = ET.parse("TestFiles/HouseTest.svg")
root = tree.getroot()

#print(type(root))

#print(root.attrib)

#print(root[0].attrib)

#print(type(root[0]))

for child in root:
    print(child.attrib["style"])
    print(child.tag)

print(root[0].attrib['d'])
#*****Extract additional data **
Colors = [] #list of string colors
strokeWidths = [] # list of stroke widths as floats

def rgb_to_hex(rgb):
    if type(rgb) == str:
        temp1 = rgb.strip("(")
        temp1 = rgb.strip(")")
        templst = temp1.split(",")
        tempfin_ = []
        print(templst)
        for num in templst:
            tempfin_.append(int(num))
        rgb_tuple = tuple(tempfin_)
        print(rgb_tuple)
        return '%02x%02x%02x' % rgb_tuple
    return '%02x%02x%02x' % rgb

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
            y=float(coordList[1])/11.811024*-1
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

    #******* Extract additional info ******
    style = child["style"]
    styles = style.split(";")
    for atr in styles:
        if "stroke:" in atr:
            color = atr.split(":")[1]
            if "rgb" in atr:
                color = color.strip("rgb(")
                color = rgb_to_hex(color)
                color = "#" + color
            Colors.append(color)
        if "stroke-width" in atr:
            pixelsSTR = atr.split(":")[1]
            strokeWidths.append(float(pixelsSTR.strip("px")))
        print("Color and stroke-width were successfully EXTRACTED!")
    #print(Colors)
    #print(strokeWidths)
        
#***********Debug Display***********

print("***********Debug Display***********")
for i in range(0,len(lineXCollection)):
    plt.plot(lineXCollection[i],lineYCollection[i],color=Colors[i],linewidth = strokeWidths[i])
plt.show()

