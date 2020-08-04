from pygame_functions import mouseX, mouseY, mousePressed,drawRect

class paintChoice:
    def __init__(self, paintColor, BrushSize):
        self.paintColor = paintColor
        self.BrushSize = BrushSize

class paintBrush:
    
    def __init__(self,x,y,Color):
        self.x = mouseX()
        self.y = mouseY()
        self.Color = Color

    
    def draw(self,paint):
        if paintChoice.paintColor == "Red":
            self.paint = drawRect(self.x, self.y, self.BrushSize, self.BrushSize, self.RED)
        
        

    def BounceBack(self,x,y):
        pass