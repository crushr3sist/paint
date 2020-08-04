from pygame_functions import *

from init import *

from paintBrush import *

screenSize(1280,720)

initializeTextures()

ifMouseIsOnToolbar = True
ifMouseIsPressedOnToolbar1 = True 
ifMouseIsPressedOnToolbar2 = True 

while True:
    paint = drawInit()
    #print(f"mouse X :{paint.brushX}")
    #print(f"mouse y :{paint.brushY}")
    
    #print(f"state is :{paint.limitFlag}")
    if ifMouseIsOnToolbar:
        if mousePressed():
            paint.Draw()
            if paint.brushX > 1135:
                paint.state()
                
    if ifMouseIsPressedOnToolbar1:
        paint.checker()
        if ifMouseIsPressedOnToolbar2:
            paint.state()
    
        
    if paint.brushX > 1135:
        ifMouseIsOnToolbar = False
    
        ifMouseIsPressedOnToolbar1 = True
        ifMouseIsPressedOnToolbar2 = True
    else:
        ifMouseIsOnToolbar = True
        ifMouseIsPressedOnToolbar1 = False
        ifMouseIsPressedOnToolbar2 = False
    


            
    if keyPressed("space"):
        break

endWait()