## needed imports should be imported here. so any file using the engine can just import this file

import pygame    
from Classes.Vector import Vector2
from Classes.Sprite import Sprite, SpriteEnv


class Horizon:
    DefaultWindowSize = Vector2(1000, 700)
    WindowOpen = False
    def RunWindow():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Horizon.WindowOpen = False
            
    def OpenWindow(WindowName = "Horizon Engine"):
        programIcon = pygame.image.load('Images/DefIcon.png')
        pygame.display.set_icon(programIcon)
        pygame.init()
        pygame.display.set_caption(WindowName)
        Horizon.WindowOpen = True
        return  pygame.display.set_mode((Horizon.DefaultWindowSize.x, Horizon.DefaultWindowSize.y))
        
    def CloseWindow():
        Horizon.WindowOpen = False