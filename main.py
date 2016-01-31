import pygame
import sys
import time
from parentEntity import *
from World import *
from gameFunctions import *
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
YELLOW = (255, 255, 0)

pygame.init()


def main():
    running = True

    # initialize classes
    npcList = []
    npcList.append(NPC(200, 200, 3, DISPLAYSURF, RED, 'Kevin', 'Hi', 1))#kevin
    npcList.append(NPC(200, 700, 3, DISPLAYSURF, RED, 'Devon', 'Hi', 1))#diaLog (NO)
    npcList.append(NPC(1200, 1100, 3, DISPLAYSURF, RED, 'Arjun', 'Hi', 1))#Fire Escape (correct)
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Curtis', 'Hi', 1))#Dstancr (NO)
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Akrama', 'Hi', 1))#Akrama (NO)
    npcList.append(NPC(800, 920, 3, DISPLAYSURF, RED, 'Nathan', 'Hi', 1))#Copy
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'James', 'Hi', 1))#UoA2B
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Hassan', 'Hi', 1))#wordi
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Conner', 'Hi', 1))#Picknuc
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Steve', 'Hi', 1))#Cardinal
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Ali', 'Hi', 1))#Facebook
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Brad', 'Hi', 1))#boom boom
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Mohammad', 'Hi', 1))#3sexy5me
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Lin', 'Hi', 1))#FBspider
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Heyue', 'Hi', 1))#HS
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'John', 'Hi', 1))#children disco
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Rumman', 'Hi', 1))#John Cena
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Colin', 'Hi', 1))#hotboyz
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Indragie', 'Hi', 1))#ares
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Ross', 'Hi', 1))#Team Catan
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Andrew', 'Hi', 1))#Cache money
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Alain', 'Hi', 1))#project Starling
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Fred', 'Hi', 1))#ragtag
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Dominic', 'Hi', 1))#Transitr
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Abid', 'Hi', 1))#NS academic
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Liam', 'Hi', 1))#liam
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Luke', 'Hi', 1))#muffin busters
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Ian', 'Hi', 1))#Meta
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'Joel', 'Hi', 1))
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, RED, 'RDIZZLE', 'IAN SUXXX', 1))


    player = Player(100, 100, 5, DISPLAYSURF, WHITE)
    world = World()
    world.load("testlevel")
    walls = world.GetCollisionRects()
    camera = Camera(50, 50)
    Coins = []
    Coins.append(Item(40, 40, DISPLAYSURF, YELLOW, "money"))
    Coins.append(Item(40, 200, DISPLAYSURF, YELLOW, "money"))

    collidelist = [walls]

    # start music
    pygame.mixer.music.load("music/main1_1.ogg")
    pygame.mixer.music.play(-1)

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

        camera.update(player.rect)

        # DON'T DRAW ANYTHING ABOVE HERE
        DISPLAYSURF.fill(BLACK) #Should be first thing in draw order
        world.draw(DISPLAYSURF, camera)
        player.update(key, walls)
        player.draw(camera)

        for npc in npcList:
            npc.update(walls, DISPLAYSURF, player)
            npc.draw(camera)
            npc.drawtext(DISPLAYSURF, camera)

        for coin in Coins:
            if coin.update(player.rect):
                Coins.remove(coin)
                player.points += 1
            coin.draw(camera)
        # DON'T DRAW ANYTHING BELOW HERE

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
