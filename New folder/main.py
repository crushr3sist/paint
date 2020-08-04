from pygame_functions import *
from Pbuffers import *
from toolBarDev import *
screenSize(1280,720)
setBackgroundImage('display.png')

#paintChoice.paintColor == None

colorChoice = input("choose color:")

brush = paintbrush(mouseX(),mouseY(),colorChoice)


while True:
    
    brushY = int(mouseY())
    brushX = int(mouseX())

    if mousePressed():
        pass
        #draw()

endWait()