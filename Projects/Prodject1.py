###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
################################################
stage.set_background ("spring")

q1 = codesters.Square(100,100,200,'blue')
q2 = codesters.Square(-100,100,200, 'yellow')
q3 = codesters.Square(-100,-100,200,'red')
q4 = codesters.Square(100,-100,200,'green')

s1 = codesters.Sprite("Football",100,100)
s1.set_size(0.2)
s2 = codesters.Sprite("dog",-100,-100)
s2.set_size(0.5)
s3 = codesters.Sprite("cardinal",100,-100)
s3.set_size(0.5)
s4 = codesters.Sprite("cardinal",-100,100)
s4.set_size(0.25)

message1 = codesters.Text("Wyatt James Kisicki",0,220,"black")
message2 = codesters.Text("Labron is not the GOAT",0,-220,"red")