from init import *
from pygame_functions import *


class drawInit:
    def __init__(self):
        self.brushSize = 15
        self.brushX = mouseX()
        self.brushY = mouseY()
        self.red = (254, 0, 0)
        self.orange = (242, 101, 34)
        self.yellow = (255, 254, 0)
        self.green = (0, 166, 81)
        self.blue = (0, 173, 239)
        self.darkBlue = (0, 53, 113)
        self.purple = (102, 46, 145)
        self.pink = (236, 0, 140)
        self.limitFlag = True
        self.redFlag = True
        self.orangeFlag = False
        self.yellowFlag = False
        self.greenFlag = False
        self.blueFlag = False
        self.darkBlueFlag = False
        self.purpleFlag = False
        self.pinkFlag = False
        self.color = (0, 0, 0)

    def state(self):
        if self.brushX > 1135:
            self.limitFlag = False
            pygame.display.update()

    def checker(self):
        colorObj = sideBar()

        if spriteClicked(colorObj.optionRed):
            self.redFlag == True
            self.color == self.red

        if spriteClicked(colorObj.optionOrange):
            self.orangeFlag == True
            self.color == self.orange

        if spriteClicked(colorObj.optionYellow):
            self.yellowFlag == True
            self.color == self.yellow

        if spriteClicked(colorObj.optionGreen):
            self.green == True
            self.color == self.green

        if spriteClicked(colorObj.optionBlue):
            self.blueFlag == True
            self.color == self.blue

        if spriteClicked(colorObj.optionDarkBlue):
            self.darkBlueFlag == True
            self.color == self.darkBlue

        if spriteClicked(colorObj.optionPurple):
            self.purpleFlag == True
            self.color == self.purple

        if spriteClicked(colorObj.optionPink):
            self.pinkFlag = True
            self.color == self.pink

    def Draw(self):
        colorObj = sideBar()
        print(f"{self.orangeFlag}")
        if self.limitFlag:
            if self.redFlag:
                self.color = self.red

                if spriteClicked(colorObj.optionRed):
                    self.color == self.red
                    self.redFlag == True

                elif self.orangeFlag:
                    if spriteClicked(colorObj.optionOrange):
                        self.orangeFlag == True
                        self.color == self.orange

                elif self.yellowFlag:
                    if spriteClicked(colorObj.optionYellow):
                        self.yellowFlag == True
                        self.color == self.yellow

                elif self.green:
                    if spriteClicked(colorObj.optionGreen):
                        self.green == True
                        self.color == self.green

                elif self.blueFlag:
                    if spriteClicked(colorObj.optionBlue):
                        self.blueFlag == True
                        self.color == self.blue

                elif self.darkBlueFlag:
                    if spriteClicked(colorObj.optionDarkBlue):
                        self.darkBlueFlag == True
                        self.color == self.darkBlue

                elif self.purpleFlag:
                    if spriteClicked(colorObj.optionPurple):
                        self.purpleFlag == True
                        self.color == self.purple

                elif self.pinkFlag:
                    if spriteClicked(colorObj.optionPink):
                        self.pinkFlag = True
                        self.color == self.pink

                self.color = self.color
            self.draw = drawRect(
                self.brushX, self.brushY, self.brushSize, self.brushSize, self.color
            )


def test():
    drawInit()
