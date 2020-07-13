from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from gCodeGeneratorClass import gCodeGenerator


class Ui_MainWindow(object):
    def __init__(self):
        self.svgPath = ""
        self.savePath = ""
        self.sampleHeight = 30.0
        self.stepHeight = 3.0
        self.bShowPreview = False
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.openFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(0, 510, 131, 41))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.openFileButton.setFont(font)
        self.openFileButton.setObjectName("openFileButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.openFileButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton_2.setGeometry(QtCore.QRect(310, 510, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.openFileButton_2.setFont(font)
        self.openFileButton_2.setObjectName("openFileButton_2")
        self.openFileButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton_3.setGeometry(QtCore.QRect(610, 470, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.openFileButton_3.setFont(font)
        self.openFileButton_3.setObjectName("openFileButton_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 391, 441))
        self.groupBox.setObjectName("groupBox")
        self.LabelSample = QtWidgets.QLabel(self.groupBox)
        self.LabelSample.setGeometry(QtCore.QRect(10, 50, 131, 31))

        self.Statuslabel = QtWidgets.QLabel(self.centralwidget)
        self.Statuslabel.setGeometry(QtCore.QRect(450, 60, 200, 31))
        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(500, 60, 200, 31))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelSample.setFont(font)
        self.LabelSample.setObjectName("LabelSample")

        self.Statuslabel.setFont(font)
        self.Statuslabel.setObjectName("Status")
        self.Status.setFont(font)
        self.Status.setObjectName("Status")

        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.LineEditSample = QtWidgets.QLineEdit(self.groupBox)
        self.LineEditSample.setGeometry(QtCore.QRect(140, 50, 91, 31))
        self.LineEditSample.setClearButtonEnabled(False)
        self.LineEditSample.setObjectName("LineEditSample")
        self.LabelStep = QtWidgets.QLabel(self.groupBox)
        self.LabelStep.setGeometry(QtCore.QRect(10, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelStep.setFont(font)
        self.LabelStep.setObjectName("LabelStep")
        self.LineEditStep = QtWidgets.QLineEdit(self.groupBox)
        self.LineEditStep.setGeometry(QtCore.QRect(120, 90, 91, 31))
        self.LineEditStep.setClearButtonEnabled(False)
        self.LineEditStep.setObjectName("LineEditStep")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(274, 402, 111, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 0, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Rage Italic")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "G-Code GENERATOR"))
        self.openFileButton.setText(_translate("MainWindow", "Open file"))
        self.openFileButton.clicked.connect(self.pushOpenFile)
        self.label.setText(_translate("MainWindow", "OPTIONS"))
        self.openFileButton_2.setText(_translate("MainWindow", "Chose save location"))
        self.openFileButton_2.clicked.connect(self.pushSaveLoc)
        self.openFileButton_3.setText(_translate("MainWindow", "Generate"))
        self.openFileButton_3.clicked.connect(self.pushGenerate)
        self.groupBox.setTitle(_translate("MainWindow", "Options"))
        self.LabelSample.setText(_translate("MainWindow", "Sample HEIGHT:"))
        self.Statuslabel.setText(_translate("MainWindow","Status: "))
        self.Status.setText(_translate("MainWindow", "Please select file paths!"))
        self.checkBox.setText(_translate("MainWindow", "Show SVG preview"))
        self.checkBox.stateChanged.connect(self.showPreview)
        self.LineEditSample.setPlaceholderText(_translate("MainWindow", "30.0 mm"))
        self.LabelStep.setText(_translate("MainWindow", "Step HEIGHT:"))
        self.LineEditStep.setPlaceholderText(_translate("MainWindow", "3.0 mm"))
        self.pushButton.setText(_translate("MainWindow", "Apply settings"))
        self.pushButton.clicked.connect(self.applySettings)
        self.label_2.setText(_translate("MainWindow", "G-CODE Generator"))

    def updateStatus(self):
        if self.savePath != "" and self.svgPath != "":
            self.Status.setText("Everything is ready!")
        else:
            self.Status.setText("Please select file paths!")

    def pushOpenFile(self):
        self.svgPath = QFileDialog.getOpenFileName()[0]
        print(type(self.svgPath))
        self.updateStatus()

    def pushSaveLoc(self):
        self.savePath = QFileDialog.getSaveFileName()[0]
        if ".gcode" not in self.savePath:
            self.savePath += ".gcode"
        print(self.savePath)
        self.updateStatus()

    def pushGenerate(self):
        if self.svgPath == "" or self.savePath =="":
            warn = QMessageBox()
            warn.setWindowTitle("SVG file needs to be specified!")
            warn.setText("SVG file needs to be specified!")
            warn.setIcon(QMessageBox.Critical)
            warn.exec_()
            return
        gcode = gCodeGenerator(self.svgPath,self.bShowPreview,self.savePath,SAMPLE_HEIGHT=self.sampleHeight,STEP_HEIGHT=self.stepHeight)


    def applySettings(self):
        if self.LineEditSample.text() != "" or self.LineEditStep.text() != "":
            self.sampleHeight = float(self.LineEditSample.text())
            self.stepHeight = float(self.LineEditStep.text())
        else:
            warn = QMessageBox()
            warn.setWindowTitle("Settings empty!")
            warn.setText("Please fill the parameters in settings.")
            warn.setIcon(QMessageBox.Critical)
            warn.exec_()
            return
        print("Settings applied")
        info = QMessageBox()
        info.setWindowTitle("Settings applied!")
        info.setText("Settings applied!")
        info.setIcon(QMessageBox.Information)
        info.exec_()

    def showPreview(self):
        self.bShowPreview = not self.bShowPreview
        print(self.bShowPreview)

    def cleanUp(self):
        self.svgPath = ""
        self.savePath = ""
        self.updateStatus()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt

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
        for i in range(0,len(self.lineXCollection)):
            plt.plot(self.lineXCollection[i],self.lineYCollection[i],color=self.Colors[i],linewidth = self.strokeWidths[i])
        plt.show()

    def getXlist(self):
        return self.lineXCollection

    def getYlist(self):
        return self.lineYCollection

    def getLines(self):
        return self.lineCollection


#testParse = svgParser("TestFiles/HouseTest.svg",False,True)

from SvgParseClass import svgParser

class gCodeGenerator:
    def __init__(self,svgPath,showPreview,savePath = "/",SAMPLE_HEIGHT = 30.0,STEP_HEIGHT=3.0):
        self.svgPath = svgPath
        self.savePath = savePath
        self.showPreview = showPreview
        self.SAMPLE_HEIGHT = SAMPLE_HEIGHT
        if STEP_HEIGHT <= 0.0:
            raise Exception("Step height should not be 0 or bellow 0!")
        self.STEP_HEIGHT = STEP_HEIGHT
        self.generateGcode()

    def generateGcode(self):
        print("**** STARTING G-CODE GENERATION ****")
        self.startGcode = ""
        self.endGcode = ""

        with open("customGcode.gcode") as self.gcode:
            self.customGcode = self.gcode.read()
            self.gcodelst_ = self.customGcode.split("#")
            for part in self.gcodelst_:
                if ";Start gCode" in part:
                    self.startGcode = part
                if ";End gCode" in part:
                    self.endGcode = part

        self.finalGcode = open(self.savePath,"w+")

        self.finalGcode.write(self.startGcode)

        self.svg = svgParser(self.svgPath,self.showPreview,True)

        self.movingInstructions = ""
        self.currentDepth = self.SAMPLE_HEIGHT

        self.layerCount = int(round((self.SAMPLE_HEIGHT/self.STEP_HEIGHT)+0.5))

        for line in self.svg.lineCollection:
            for a in range(self.layerCount):
                for i,point in enumerate(line):
                    self.x = str(point[0])
                    self.y = str(point[1])
                    self.movingInstructions += f"G01 X{self.x} Y{self.y}"
                    if i == 0:
                        self.movingInstructions +=" F3000\n"
                        #move down
                        self.currentDepth = self.currentDepth-self.STEP_HEIGHT
                        if self.currentDepth<0:
                            self.currentDepth = 0
                        self.movingInstructions += f"G01 Z{self.currentDepth-self.SAMPLE_HEIGHT}\n"
                        continue
                    self.movingInstructions += "\n"
                
            self.movingInstructions += "G01 Z5\n"
            self.currentDepth = self.SAMPLE_HEIGHT

        self.finalGcode.write(self.movingInstructions)
        self.finalGcode.write(self.endGcode)

        self.finalGcode.close()
        print("**** G-CODE GENERATION SUCCESSFULL! ****")


