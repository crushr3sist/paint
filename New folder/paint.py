from pygame_functions import *

screenSize(1680, 1050)

WHITE = (255, 255, 255)

setBackgroundColour(WHITE)

sideBar = makeSprite("background.png")
showSprite(sideBar)
moveSprite(sideBar, 1580, 0)

brushSize = 25

Red = False
RED = (255, 0, 0)

Green = False
GREEN = (0, 255, 0)

Blue = False
BLUE = (0, 0, 255)


def DispColors():
    red_selection = drawRect(1590, 86, brushSize, brushSize, RED)
    green_selection = drawRect(1590, 111, brushSize, brushSize, GREEN)
    blue_selection = drawRect(1590, 136, brushSize, brushSize, BLUE)


DispColors()


def Drawing():

    print(f"y = {brushY}")
    print(f"x = {brushX}")
