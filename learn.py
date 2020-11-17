import pygame
from player import Player

WIN_WIDTH = 1200 
WIN_HEIGHT = 700
FRAMERATE = 60
DEBUG = True

# COLORS
black = pygame.Color('#000000')
white = pygame.Color('#FFFFFF')
sky = pygame.Color('#40A1E6')

pygame.init()

Game_Window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Butts")

clock = pygame.time.Clock()
ACTIVE = True 

background = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
background.fill(sky)

player = Player(background, clock, 110, 110, white)


def checkLost():
    if player.getBotY() >= WIN_HEIGHT or player.getY()  <= 0:
        player.gameover()
        GameOver()
        

def GameOver():
    print("GG") 
    ACTIVE = False 

        
    
if __name__ == "__main__":
    while ACTIVE:
        jumping = False
        time_delta = clock.tick(FRAMERATE)/1000.0
        if DEBUG:
            #print(time_delta)
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ACTIVE = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumping = True

        player.update(time_delta, jumping)

        checkLost()

        background.fill(sky)

        player.draw()
        pygame.draw.rect(background, black, (0, 0, 100, 100))

        Game_Window.blit(background, (0,0))

        pygame.display.update()
