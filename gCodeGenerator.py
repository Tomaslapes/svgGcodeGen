from SvgParseClass import svgParser

svgPath = "TestFiles/FinalTest.svg"
SAMPLE_HEIGHT = 31.5
STEP_HEIGHT = 3.0

startGcode = ""
endGcode = ""

with open("customGcode.gcode") as gcode:
    customGcode = gcode.read()
    gcodelst_ = customGcode.split("#")
    for part in gcodelst_:
        if ";Start gCode" in part:
            startGcode = part
        if ";End gCode" in part:
            endGcode = part

finalGcode = open("TestGcodeFile4.gcode","w+")

finalGcode.write(startGcode)

svg = svgParser(svgPath,False,True)

movingInstructions = ""
currentDepth = SAMPLE_HEIGHT

layerCount = int(round((SAMPLE_HEIGHT/STEP_HEIGHT)+0.5))

for line in svg.lineCollection:
    for a in range(layerCount):
        for i,point in enumerate(line):
            x = str(point[0])
            y = str(point[1])
            movingInstructions += f"G01 X{x} Y{y}"
            if i == 0:
                movingInstructions +=" F3000\n"
                #move down
                currentDepth = currentDepth-STEP_HEIGHT
                if currentDepth<0:
                    currentDepth = 0
                movingInstructions += f"G01 Z{currentDepth-SAMPLE_HEIGHT}\n"
                continue
            movingInstructions += "\n"
        
    movingInstructions += "G01 Z5\n"
    currentDepth = SAMPLE_HEIGHT

finalGcode.write(movingInstructions)
finalGcode.write(endGcode)

finalGcode.close()