;This is a custom gCode command file
;you can add here what gcode should be executed on start, toolchange, end etc.
;each block shoud be separated with a hashtag character
#
;Start gCode
G00 Z5.0000
G4 S3;Sets a timer of 3 seconds to give me time to turn on the tool
#
;End gCode
G00 Z5.0000
G00 X0.0000 Y0.0000 
