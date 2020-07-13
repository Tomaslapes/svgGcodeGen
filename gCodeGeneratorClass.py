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


