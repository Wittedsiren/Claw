from Horizon import *
from time import sleep

window = Horizon.OpenWindow(WindowName="Engine")

boxA = Sprite("box")

while Horizon.WindowOpen:  ## this is a loop or game loop.
    Horizon.RunWindow()
    color = (255, 0, 0)
 
    # Changing surface color
    window.fill(color)
    pygame.display.flip()
