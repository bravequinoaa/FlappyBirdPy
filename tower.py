import pygame

class Tower:
    def __init__(self, surface, clock, width, height, color):
        self.Surface = surface
        self.Clock = clock
        self.Width  = width
        self.Height = height
        self.Color = color

        #Pos
        self.X1 = 400.0
        self.Y1 = 150.0
        self.X2 = 400.0
        self.Y2 = 150.0
    
