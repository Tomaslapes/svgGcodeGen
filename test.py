from SvgParseClass import svgParser
from gCodeGeneratorClass import gCodeGenerator

#testParse = svgParser("TestFiles/FinalTest.svg",True,True)

gcode = gCodeGenerator("TestFiles/FinalTest.svg",True,SAMPLE_HEIGHT = 31.5,STEP_HEIGHT = 3.0,savePath = "classTest3.gcode")
