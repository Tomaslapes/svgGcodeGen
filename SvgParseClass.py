import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt
import numpy as np

class svgParser:
    def __init__(self, svgPath, showPreview, USE_MILLIMETERS = True):
        self.svgPath = svgPath
        if type(self.svgPath) != str:
            raise Exception('INVALID PATH -svgPath should be a string!')
        self.tree = ET.parse(self.svgPath)
        self.root = self.tree.getroot()
        self.Colors = [] #list of string colors
        self.strokeWidths = [] # list of stroke widths as floats
        self.lineCollection = []# Stores all lines as [[[xPoint1,yPoint1],[xPoint2,yPoint2]],[[xPoint1,yPoint1],[xPoint2,yPoint2]]]
        self.lineXCollection = []# Stores all X values as a list X values per each line ie. list of x coord. list
        self.lineYCollection = []# Stores all Y values as a list Y values per each line ie. list of y coord. list
        self.USE_MILLIMETERS = USE_MILLIMETERS
        self.parseData()
        if showPreview:
            self.preview()

    def rgb_to_hex(self,rgb):
        self.rgb = rgb

        if type(self.rgb) == str:
            self.temp1 = self.rgb.strip("(")
            self.temp1 = self.rgb.strip(")")
            self.templst = self.temp1.split(",")
            self.tempfin_ = []
            print(self.templst)
            for num in self.templst:
                self.tempfin_.append(int(num))
            self.rgb_tuple = tuple(self.tempfin_)
            print(self.rgb_tuple)
            return '%02x%02x%02x' % self.rgb_tuple

        return '%02x%02x%02x' % self.rgb

    def parseData(self):
        self.childLst = []
        for child in self.root:
            self.childLst.append(child.attrib)
        for child in self.childLst:
            self.Coords = child["d"]

            self.LinesSTR = self.Coords.strip("M")
            self.LinesSTR = self.LinesSTR.strip("Z")
            self.LinesSTR = self.LinesSTR.split("L")
            print(self.LinesSTR)

            self.Lines = []
            self.LinesX = []
            self.LinesY = []
            for line in self.LinesSTR:
                self.coordList = line.split(",")
                print(self.coordList)
                if self.USE_MILLIMETERS:
                    self.x=float(self.coordList[0])/11.811024
                    self.LinesX.append(self.x)
                    self.y=float(self.coordList[1])/11.811024*-1
                    self.LinesY.append(self.y)
                else:
                    self.x=float(self.coordList[0])
                    self.LinesX.append(self.x)
                    self.y=float(self.coordList[1])
                    self.LinesY.append(self.y)
                self.point = [self.x,self.y]
                self.Lines.append(self.point)
            print(self.Lines)
            self.lineCollection.append(self.Lines)
            self.lineXCollection.append(self.LinesX)
            self.lineYCollection.append(self.LinesY)

            #******* Extract additional info ******
            self.style = child["style"]
            self.styles = self.style.split(";")
            for atr in self.styles:
                if "stroke:" in atr:
                    self.color = atr.split(":")[1]
                    if "rgb" in atr:
                        self.color = self.color.strip("rgb(")
                        self.color = self.rgb_to_hex(self.color)
                        self.color = "#" + self.color
                    self.Colors.append(self.color)
                if "stroke-width" in atr:
                    self.pixelsSTR = atr.split(":")[1]
                    self.strokeWidths.append(float(self.pixelsSTR.strip("px"))/2)
                print("Color and stroke-width were successfully EXTRACTED!")
            #print(Colors)
            #print(strokeWidths)
            #**********Correction transformation*****
            print("**********Corrections")
            self.min_ = min(self.lineYCollection)
            self.min_ = min(self.min_)
            print(self.min_*-1)
            
        for a,line in enumerate(self.lineYCollection):
            print(line)
            for b,point in enumerate(line):
                self.lineYCollection[a][b] = self.lineYCollection[a][b] + self.min_*-1
                print(self.lineYCollection[a][b])
                            

    def preview(self):
        print("***********Debug Display***********")
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        for i in range(0,len(self.lineXCollection)):
            #ax.plot3D(self.lineXCollection[i],self.lineYCollection[i],self.lineYCollection[i],"gray")

            plt.plot(self.lineXCollection[i],self.lineYCollection[i],color=self.Colors[i],linewidth = self.strokeWidths[i])
        plt.axis('off')
        plt.title("SVG preview-close to continue")
        plt.show()

    def getXlist(self):
        return self.lineXCollection

    def getYlist(self):
        return self.lineYCollection

    def getLines(self):
        return self.lineCollection


#testParse = svgParser("TestFiles/HouseTest.svg",False,True)
