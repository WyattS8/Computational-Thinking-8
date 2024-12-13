###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
################################################


stage.set_background("winter")
mySprite = codesters.Sprite("cardinal")
mySprite.say("Good job finding me!")

print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
print("This is the new last line instruction")
mySprite2 = codesters.Sprite("kitten" ,0,0)
mySprite3 = codesters.Sprite("kitten" ,150,20)
mySprite4 = codesters.Sprite("kitten" ,-150,-20)
