import pygame
from Classes.Vector import Vector2
from Stacks.SpriteEnv import SpriteEnv
from Primary.PyGameWindow import surface_and_window

def formatDefName(name):
    num = len(SpriteEnv.Env)

    def checkForMany():
        for sprite in Sprite:
            if sprite.Name == name + str(num):
                num += 1
                checkForMany()
    
    return name + str(num)

def drawSprite(sprite):
    pygame.draw.rect(surface_and_window.surface, (255,0,0), pygame.Rect(sprite.Position.X, sprite.Position.Y, sprite.Scale.X, sprite.Scale.Y))

class Sprite:
    def __init__(self, Name = f"NewSprite", Position = Vector2(), Scale = Vector2(), Rotation = 0, ZIndex = 1):
        self.Name = Name if Name != "NewSprite" else formatDefName(Name)
        self.ZIndex = ZIndex
        self.Position = Position
        self.Scale = Scale
        self.Rotation = Rotation
        SpriteEnv.Env.append(self)
        drawSprite(self)
    def Update(self):
        drawSprite(self)
        
class Line:
    def __init__(self, s, e):
        pygame.draw.line(surface_and_window.surface, (0,0,255), (s.X,s.Y), (e.X,e.Y))
        
        
        
    