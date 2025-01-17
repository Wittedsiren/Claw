## needed imports should be imported here. so any file using the engine can just import this file

import pygame    
from Classes.Vector import Vector2
from Classes.Sprite import Sprite
from Stacks.SpriteEnv import SpriteEnv


class Horizon:
    
    FPS = 60
    Clock = pygame.time.Clock()
    DefaultWindowSize = Vector2(1000, 700)
    WindowOpen = False
    Window = None
    def RunWindow():
        # Horizon.Window.fill((0,0,0))
        # for sprite in SpriteEnv.Env:
        #     sprite.Update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Horizon.WindowOpen = False
        pygame.display.update()
        Horizon.Clock.tick(Horizon.FPS)
            
    def OpenWindow(WindowName = "Horizon Engine"):
        from Primary.PyGameWindow import surface_and_window
        programIcon = pygame.image.load('Images/DefIcon.png')
        pygame.display.set_icon(programIcon)
        pygame.init()
        pygame.display.set_caption(WindowName)
        Horizon.WindowOpen = True
        Horizon.Window = pygame.display.set_mode((Horizon.DefaultWindowSize.X, Horizon.DefaultWindowSize.Y))
        surface_and_window.surface = Horizon.Window
        
    def CloseWindow():
        Horizon.WindowOpen = False