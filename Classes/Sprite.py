from Classes.Vector import *
from Stacks.SpriteEnv import SpriteEnv
import pygame
def formatDefName(name):
    num = len(SpriteEnv.Env)

    def checkForMany():
        for sprite in Sprite:
            if sprite.Name == name + str(num):
                num += 1
                checkForMany()
    
    return name + str(num)

# def drawSprite(sprite):
#     pygame.draw.rect

class Sprite:
    def __init__(self, Name = f"NewSprite", Position = Vector2(), Scale = Vector2(), Rotation = 0, ZIndex = 1):
        self.Name = Name if Name != "NewSprite" else formatDefName(Name)
        self.ZIndex = ZIndex
        self.Position = Position
        self.Scale = Scale
        self.Rotation = Rotation
        SpriteEnv.Env.append(self)


        
        
        
    