import pygame
import sys
import time
from parentEntity import *
from pygame.locals import *
from pygame.time import *

# Window setup
DISPLAYWIDTH = 1080
DISPLAYHEIGHT = 720
DISPLAYSURF = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
pygame.display.set_caption('Hackathon 2016 THE GAME')

# Framerate options
clock = pygame.time.Clock()
FPS = 30

# Some basic colours for use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)

pygame.init()

# Interprets player inputs
# If no key being pressed, returns player to STOP state
def playerInput(key, player):
    if key [K_w]:
        player.moveup()
    if key [K_s]:
        player.movedown()
    if key [K_a]:
        player.moveleft()
    if key [K_d]:
        player.moveright()
    else:
        player.stop()

def main():

    running = True

    # initialize classes
    player = GameEntity(100, 100, 5, DISPLAYSURF)


    while running:
        clock.tick(FPS)
        key = pygame.key.get_pressed() # Returns value for key as key currently being pressed

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        # Call to input handler
        playerInput(key, player)

        # DON'T DRAW ANYTHING ABOVE HERE
        DISPLAYSURF.fill(BLACK) #Should be first thing in draw order
        player.update()

        pygame.display.update()


if __name__ == "__main__":
    main()
