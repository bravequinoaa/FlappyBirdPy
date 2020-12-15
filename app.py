import pygame
from random import randint
from player import Player
from tower import Tower

DEBUG = False 
ACTIVE = True 

WIN_WIDTH = 1200 
WIN_HEIGHT = 700
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50 
FRAMERATE = 60
SCORE = 0
RUNNING_TIME = 0
TOWER_COUNTDOWN = TOWER_RESPAWN = 140
FIRST_TOWER = 300


playersprite = pygame.image.load("sprites/flappybutt.jpg")
towersprite = "sprites/"

# COLORS
black = pygame.Color('#000000')
white = pygame.Color('#FFFFFF')
sky = pygame.Color('#40A1E6')

pygame.init()
pygame.font.init()

Game_Window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Butts")

# INIT GAME OBJECTS
clock = pygame.time.Clock()
font = pygame.font.SysFont('FreeSans.ttf', 20)

background = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
background.fill(sky)

player = Player(background, clock, PLAYER_WIDTH, PLAYER_HEIGHT, white)
tower1 = Tower(background, clock, 1000, WIN_WIDTH, WIN_HEIGHT - 80, black)

# Stack of towers
towers = []

def checkLost():
    if (player.getBotY() >= WIN_HEIGHT or player.getY()  <= 0):
        GameOver()
        player.gameover()
        pass

    collisionBot = player.getCollisionBot()
    collisionTop = player.getCollisionTop()
    if DEBUG:
        print(f'CollisionBot: {collisionBot}')
        print(f'CollisionTop: {collisionTop}')
    for tower in towers:
        # need to fix to work with a tuple of towers
        tower1Pos = tower[0].getPosition()
        tower2Pos = tower[1].getPosition()
        if ((collisionBot[0] > tower1Pos[0] and collisionBot[1] >= tower1Pos[1]) and (
             collisionBot[0] < tower1Pos[0] + tower[0].getWidth() and 
             collisionBot[1] < tower1Pos[1] + tower[0].getHeight())) or (
             collisionTop[0] > tower2Pos[0] and collisionTop[1] >= tower2Pos[1]) and (
             collisionTop[0] < tower2Pos[0] + tower[1].getWidth() and
             collisionTop[1] < tower2Pos[1] + tower[1].getHeight()):
             print("collision detected")
             GameOver()
             player.gameover()


def GameOver():
    global ACTIVE 
    ACTIVE = False

def createTower():
    Y = randint(000, 500)
    towerBot = Tower(background, clock, 1000, WIN_WIDTH, WIN_HEIGHT - Y, black)
    towerTop = Tower(background, clock, towerBot.getY() - 200, WIN_WIDTH, 0, black)
    towers.append((towerBot, towerTop))

def updateTowers():
    for tower in towers:
        tower[0].update()
        tower[1].update()

def drawTowers():
    for tower in towers:
        tower[0].draw()
        tower[1].draw()

def destroyTower():
    t = towers[0]
    towers.pop(0)

    
if __name__ == "__main__":
    createTower()
    while ACTIVE:
        jumping = False
        time_delta = clock.tick(FRAMERATE)/1000.0
        RUNNING_TIME += time_delta

        if DEBUG:
            #pygame.draw.rect(background, black, (0, 0, 100, 100))
            #print(str(round(RUNNING_TIME, 3)))
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ACTIVE = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    SCORE += 1
                    jumping = True
                    #print(ACTIVE)
        # TEXT
        scoretext = font.render(f'SCORE: {SCORE}', True, (0, 0, 0))
        timetext = font.render(f'TIME: {str(round(RUNNING_TIME, 3))}', True, (0, 0, 0))

        # Need to be ran every frame
        TOWER_RESPAWN -= 1
        if TOWER_RESPAWN == 0:
            TOWER_RESPAWN = TOWER_COUNTDOWN
            createTower()

        player.update(time_delta, jumping)
        updateTowers()
        tower1.update()
        checkLost()

        # DRAW
        background.fill(sky)
        drawTowers()
        player.draw()
        drawTowers()

        Game_Window.blit(background, (0,0))
        Game_Window.blit(scoretext, (0,0))
        Game_Window.blit(timetext, (0,20))

        pygame.display.update()
    
