import pygame
import sys
import time
from pygame.locals import *
from pygame.time import *

# Window setup
DISPLAYWIDTH = 720
DISPLAYHEIGHT = 480
DISPLAYSURF = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
pygame.display.set_caption('Hackathon 2016 THE GAME')

def main():

    running = True
    
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()




if __name__ == "__main__":
    main()
