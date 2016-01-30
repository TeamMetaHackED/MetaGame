import pygame
import sys
import time
from pygame.locals import *
from pygame.time import *

# Window setup
DISPLAYWIDTH = 1080
DISPLAYHEIGHT = 720
DISPLAYSURF = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
pygame.display.set_caption('Hackathon 2016 THE GAME')

# Some basic colours for use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)

def main():

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed() # Returns value for key as key currently being pressed

        DISPLAYSURF.fill(BLACK)


if __name__ == "__main__":
    main()
