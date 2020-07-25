from SvgParseClass import svgParser
import math

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
            gcodelst_ = self.customGcode.split("#")
            for part in gcodelst_:
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
            firstPoint_ = line[0]
            lastPoint_ = line[-1]
            linesTouch = False
            print("FirstPoint = "+str(firstPoint_) +"\nLastPoint = "+str(lastPoint_))
            if math.isclose(firstPoint_[0],lastPoint_[0],abs_tol=0.001) and math.isclose(firstPoint_[1],lastPoint_[1],abs_tol=0.001):
                print("Points are close enough")
                linesTouch = True
            for a in range(self.layerCount):
                for i,point in enumerate(line):
                    x = str(point[0])
                    y = str(point[1])
                    self.movingInstructions += f"G01 X{x} Y{y}"
                    if i == 0:
                        self.movingInstructions +=" F3000\n"
                        #move down
                        self.currentDepth = self.currentDepth-self.STEP_HEIGHT
                        if self.currentDepth<0:
                            self.currentDepth = 0
                        self.movingInstructions += f"G01 Z{self.currentDepth-self.SAMPLE_HEIGHT}\n"
                        continue
                    self.movingInstructions += "\n"
                if not linesTouch:
                    self.movingInstructions += "G01 Z5\n"
            self.movingInstructions += "G01 Z5\n"
            self.currentDepth = self.SAMPLE_HEIGHT

        self.finalGcode.write(self.movingInstructions)
        self.finalGcode.write(self.endGcode)

        self.finalGcode.close()
        print("**** G-CODE GENERATION SUCCESSFUL! ****")


