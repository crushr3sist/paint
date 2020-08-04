from pygame_functions import *

screenSize(1280, 720)

setBackgroundImage("background.png")

toolBar = makeSprite("toolBar.png")
moveSprite(toolBar, 1136.9, 0)
showSprite(toolBar)

optionRed = makeSprite("optionRed.png")
moveSprite(optionRed, 1136.9, 0.51)
showSprite(optionRed)
optionOrange = makeSprite("optionOrange.png")
moveSprite(optionOrange, 1136.9, 46.46)
showSprite(optionOrange)
optionyellow = makeSprite("optionYellow.png")
moveSprite(optionyellow, 1136.9, 93.46)
showSprite(optionyellow)
optionGreen = makeSprite("optiongreen.png")
moveSprite(optionGreen, 1136.9, 140.46)
showSprite(optionGreen)
optionBlue = makeSprite("optionBlue.png")
moveSprite(optionBlue, 1136.9, 187.46)
showSprite(optionBlue)
optionDarkBlue = makeSprite("optionDarkBlue.png")
moveSprite(optionDarkBlue, 1136.9, 234.46)
showSprite(optionDarkBlue)
optionPurple = makeSprite("optionPurple.png")
moveSprite(optionPurple, 1136.9, 281.46)
showSprite(optionPurple)
optionPink = makeSprite("optionPink.png")
moveSprite(optionPink, 1136.9, 328.46)
showSprite(optionPink)

optionSmall = makeSprite("optionSmall.png")
moveSprite(optionSmall, 1186.41, 406.5)
showSprite(optionSmall)

optionNormal = makeSprite("optionNormal.png")
moveSprite(optionNormal, 1179.41, 440.53)
showSprite(optionNormal)

optionBig = makeSprite("optionBig.png")
moveSprite(optionBig, 1194.41, 478.83)
showSprite(optionBig)

optionCircle = makeSprite("optioncCircle.png")
moveSprite(optionCircle, 1177.94, 536.09)
showSprite(optionCircle)
optionSquare = makeSprite("optionSquare.png")
moveSprite(optionSquare, 1178, 620)
showSprite(optionSquare)

while True:
    if spriteClicked(optionSquare):
        print("optionSquare clicked")
