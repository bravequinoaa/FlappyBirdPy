import pygame 

class Player():
    def __init__(self, surface, clock, width, height, color=None, sprite=None):
        self.Surface = surface
        self.Clock = clock
        self.Width  = width
        self.Height = height
        self.Color = color
        self.Spirte = sprite
        self.X = 400.0
        self.Y = 150.0
        self.collisionX = self.X + self.Width
        self.collisionY = self.Y + self.Height
        self.fallingConstant = 135
        self.vertSpeed = 0
        self.jumpSpeed = 180

    def getY(self):
        return self.Y

    def getX(self):
        return self.X

    def getBotY(self):
        return self.Y + self.Height

    def getCollision(self):
        return (self.collisionX, self.collisionY)

    def draw(self):
        pygame.draw.rect(self.Surface, self.Color, (self.X, self.Y, self.Width, self.Height))

    def update(self, timedelta, jump):
        if jump:
            self.vertSpeed = self.jumpSpeed
        self.Y -= self.vertSpeed * timedelta
        self.vertSpeed -= self.fallingConstant * timedelta
        self.collisionX = self.X + self.Width
        self.collisionY = self.Y + self.Height

    def gameover(self):
        self.fallingConstant = 0
        self.jumpSpeed = 0


