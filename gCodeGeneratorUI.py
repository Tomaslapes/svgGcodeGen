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
        self.bShowGcode = False
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
        self.checkBox2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox2.setGeometry(QtCore.QRect(10, 120, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox2.setFont(font)
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
        self.checkBox2.setText(_translate("MainWindow", "Show G-CODE preview"))
        self.checkBox2.stateChanged.connect(self.previewGCode)
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
        gcode = gCodeGenerator(self.svgPath,self.bShowPreview,self.bShowGcode,self.savePath,SAMPLE_HEIGHT=self.sampleHeight,STEP_HEIGHT=self.stepHeight)
        self.cleanUp()

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

    def previewGCode(self):
        self.bShowGcode = not self.bShowGcode
        print(self.bShowGcode)

    def cleanUp(self):
        self.svgPath = ""
        self.savePath = ""
        self.updateStatus()

def main():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

main()
