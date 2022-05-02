from pygame_functions import makeSprite,moveSprite, showSprite, setBackgroundImage

class sideBar:

    def __init__(self):
        
        setBackgroundImage("textures/background.png")
        
        self.toolBarBack = makeSprite("textures/toolBar.png")
        moveSprite(self.toolBarBack , 1136.9, 0)
        showSprite(self.toolBarBack)
        
        self.optionRed = makeSprite("textures/optionRed.png")
        moveSprite(self.optionRed, 1136.9, 0.51)
        showSprite(self.optionRed)
        self.optionOrange = makeSprite("textures/optionOrange.png")
        moveSprite(self.optionOrange, 1136.9, 46.46)
        showSprite(self.optionOrange)
        self.optionYellow = makeSprite("textures/optionYellow.png")
        moveSprite(self.optionYellow, 1136.9, 93.46)
        showSprite(self.optionYellow)
        self.optionGreen = makeSprite("textures/optiongreen.png")
        moveSprite(self.optionGreen, 1136.9, 140.46)
        showSprite(self.optionGreen)
        self.optionBlue = makeSprite("textures/optionBlue.png")
        moveSprite(self.optionBlue, 1136.9, 187.46)
        showSprite(self.optionBlue)
        self.optionDarkBlue = makeSprite("textures/optionDarkBlue.png")
        moveSprite(self.optionDarkBlue, 1136.9, 234.46)
        showSprite(self.optionDarkBlue)
        self.optionPurple = makeSprite("textures/optionPurple.png")
        moveSprite(self.optionPurple, 1136.9, 281.46)
        showSprite(self.optionPurple)
        self.optionPink = makeSprite("textures/optionPink.png")
        moveSprite(self.optionPink, 1136.9, 328.46)
        showSprite(self.optionPink)
        self.optionSmall = makeSprite("textures/optionSmall.png")
        moveSprite(self.optionSmall, 1186.41, 406.5)
        showSprite(self.optionSmall)
        self.optionNormal = makeSprite("textures/optionNormal.png")
        moveSprite(self.optionNormal, 1179.41, 440.53)
        showSprite(self.optionNormal)
        self.optionBig = makeSprite("textures/optionBig.png")
        moveSprite(self.optionBig, 1194.41, 478.83)
        showSprite(self.optionBig)
        self.optionCircle = makeSprite("textures/optioncCircle.png")
        moveSprite(self.optionCircle, 1177.94, 536.09)
        showSprite(self.optionCircle)
        self.optionSquare = makeSprite("textures/optionSquare.png")
        moveSprite(self.optionSquare, 1178, 620)
        showSprite(self.optionSquare)
        self.toolBarArray = [self.toolBarBack,self.optionRed,self.optionOrange,self.optionYellow,self.optionGreen,self.optionBlue,self.optionDarkBlue,self.optionPurple,self.optionPink]
                    

def initializeTextures():
    return sideBar()

