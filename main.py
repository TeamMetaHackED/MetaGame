import pygame
import sys
import time
from parentEntity import *
from World import *
from pygame.locals import *
from pygame.time import *

# Window setup
DISPLAYWIDTH = 800
DISPLAYHEIGHT = 800
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

<<<<<<< HEAD
=======
# Interprets player inputs
# If no key being pressed, returns player to STOP state
def playerInput(key, player, walls):
    dx = 0
    dy = 0
    if key [K_w]:
        dy = -1
    if key [K_s]:
        dy = 1
    if key [K_a]:
        dx = -1
    if key [K_d]:
        dx = 1
    player.move(dx, dy)
    for wall in walls:
        if player.sprite.colliderect(wall):
            if dy == -1:
                player.sprite.top = wall.bottom
            if dy == 1:
                player.sprite.bottom = wall.top
            if dx == -1:
                player.sprite.left = wall.right
            if dx == 1:
                player.sprite.right = wall.left

>>>>>>> c57670512da5f9f59a12c9dd40e18e632310e0e6
def main():
    running = True

    # initialize classes
    npcList = []
    npcList.append(NPC(200, 200, 3, DISPLAYSURF, 'Kevin', 'Hi', 1))

    player = Player(100, 100, 5, DISPLAYSURF)
    world = World()
    world.load("testlevel")
    walls = world.GetCollisionRects()


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
        playerInput(key, player, walls)

        # DON'T DRAW ANYTHING ABOVE HERE
        DISPLAYSURF.fill(BLACK) #Should be first thing in draw order
        world.draw(DISPLAYSURF)
        player.update()
        for npc in npcList:
            npc.update()

        pygame.display.update()


if __name__ == "__main__":
    main()
