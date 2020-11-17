import pygame 

class Player():
    def __init__(self, surface, clock, width, height, color):
        self.Surface = surface
        self.Clock = clock
        self.Width  = width
        self.Height = height
        self.Color = color
        self.X = 400.0
        self.Y = 150.0
        self.fallingConstant = 90
        self.vertSpeed = 0
        self.jumpSpeed = 140

    def getY(self):
        return self.Y

    def getX(self):
        return self.X

    def getBotY(self):
        return self.Y + self.Height

    def draw(self):
        pygame.draw.rect(self.Surface, self.Color, (self.X, self.Y, self.Width, self.Height))

    def update(self, timedelta, jump):
        if jump:
            self.vertSpeed = self.jumpSpeed
        self.Y -= self.vertSpeed * timedelta
        self.vertSpeed -= self.fallingConstant * timedelta

    def gameover(self):
        pass


