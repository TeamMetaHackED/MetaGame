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
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 140, 60)
RYAN = (35, 255, 145)

pygame.init()


def main():
    running = True

    # initialize classes
    npcList = []

    npcList.append(NPC(200, 200, 0, DISPLAYSURF, RED, 'Kevin', 'KEEEVVVVVIIIIINNNNN', 1))#kevin
    npcList.append(NPC(1300, 50, 3, DISPLAYSURF, BLUE, 'Devon', 'Why doesn''t my code work?', 1))#diaLog (NO)
    npcList.append(NPC(1200, 1100, 3, DISPLAYSURF, YELLOW, 'Arjun', 'Blaze it lol', 1))#Fire Escape (correct)
    npcList.append(NPC(1400, 800, 3, DISPLAYSURF, CYAN, 'Curtis', 'Everything works perfectly! Ha, jk', 1))#Dstancr (NO)
    npcList.append(NPC(1400, 1400, 3, DISPLAYSURF, MAGENTA, 'Akrama', ':D', 1))#Akrama (NO)
    npcList.append(NPC(800, 920, 3, DISPLAYSURF, RED, 'Nathan', 'Honestly I''m surprised this much works', 1))#Copy
    npcList.append(NPC(500, 900, 3, DISPLAYSURF, BLUE, 'James', 'We should have chosen something easier', 1))#UoA2B
    npcList.append(NPC(900, 50, 3, DISPLAYSURF, YELLOW, 'Hassan', 'What''s sleep?', 1))#wordi
    npcList.append(NPC(800, 300, 3, DISPLAYSURF, CYAN, 'Conner', 'Why doesn''t my code work?', 1))#Picknuc
    npcList.append(NPC(800, 1200, 3, DISPLAYSURF, MAGENTA, 'Steve', 'GitHub has failed me again', 1))#Cardinal
    npcList.append(NPC(950, 800, 0, DISPLAYSURF, RED, 'Ali', 'Why doesn''t my code work?', 1))#Facebook
    npcList.append(NPC(1300, 1150, 3, DISPLAYSURF, BLUE, 'Brad', 'I didn''t know it was possible to get this many errors', 1))#boom boom
    npcList.append(NPC(1200, 200, 3, DISPLAYSURF, YELLOW, 'Mohammad', '24 hours is surprisingly little time', 1))#3sexy5me
    npcList.append(NPC(100, 900, 3, DISPLAYSURF, MAGENTA, 'Lin', 'At least there were pancakes', 1))#FBspider
    npcList.append(NPC(500, 700, 3, DISPLAYSURF, CYAN, 'Heyue', 'At least there was pizza', 1))#HS
    npcList.append(NPC(1300, 200, 3, DISPLAYSURF, RED, 'John', 'How''s your code coming?', 1))#children disco
    npcList.append(NPC(1400, 400, 3, DISPLAYSURF, YELLOW, 'Rumman', 'At least there was alcohol close by', 1))#John Cena
    npcList.append(NPC(800, 550, 3, DISPLAYSURF, ORANGE, 'Colin', 'So this connects to... what?', 1))#hotboyz
    npcList.append(NPC(1000, 900, 3, DISPLAYSURF, ORANGE, 'Indragie', 'I haven''t slept in weeks', 1))#ares
    npcList.append(NPC(340, 1400, 3, DISPLAYSURF, BLUE, 'Ross', 'So many errors...', 1))#Team Catan
    npcList.append(NPC(1300, 500, 3, DISPLAYSURF, YELLOW, 'Andrew', 'What does this even do?', 1))#Cache money
    npcList.append(NPC(1300, 900, 3, DISPLAYSURF, MAGENTA, 'Alain', 'I hope I win', 1))#project Starling
    npcList.append(NPC(1300, 1300, 3, DISPLAYSURF, CYAN, 'Fred', 'It''s a battle between me and bad coding', 1))#ragtag
    npcList.append(NPC(600, 600, 3, DISPLAYSURF, RED, 'Dominic', 'Hey, want to play more ping pong?', 1))#Transitr
    npcList.append(NPC(300, 1250, 3, DISPLAYSURF, ORANGE, 'Abid', 'Why doesn''t my code work?', 1))#NS academic
    npcList.append(NPC(100, 1400, 3, DISPLAYSURF, YELLOW, 'Liam', 'Why doesn''t my code work?', 1))#liam
    npcList.append(NPC(1000, 1250, 3, DISPLAYSURF, RED, 'Luke', 'I''m running on red bull and tears', 1))#muffin busters
    npcList.append(NPC(1100, 1500, 3, DISPLAYSURF, BLUE, 'Ian', 'How am use GitHub', 1))#Meta
    npcList.append(NPC(850, 1400, 0, DISPLAYSURF, RED, 'Brittany', 'I''m really tired but at least\n I don''t have to think', 1))
    npcList.append(NPC(400, 500, 3, DISPLAYSURF, MAGENTA, 'Joel', 'I feel so optimistic!', 1))
    npcList.append(NPC(600, 500, 3, DISPLAYSURF, RYAN, 'Ryan', 'SLEEP IS FOR THE WEAK', 1))

    player = Player(850, 450, 10, DISPLAYSURF, WHITE)
    world = World()
    world.load("testlevel")
    walls = world.GetCollisionRects()

    Coins = []
    Coins.append(Item(40, 50, DISPLAYSURF, YELLOW))
    Coins.append(Item(40, 200, DISPLAYSURF, YELLOW))
    Coins.append(Item(90, 120, DISPLAYSURF, YELLOW))
    Coins.append(Item(70, 250, DISPLAYSURF, YELLOW))
    Coins.append(Item(400, 500, DISPLAYSURF, YELLOW))
    Coins.append(Item(900, 500, DISPLAYSURF, YELLOW))
    Coins.append(Item(1200, 1100, DISPLAYSURF, YELLOW))

    # start music
    musiclist = ['music/main1_1.ogg','music/pizzle1.ogg','music/boss.ogg']
    pygame.mixer.music.load(random.choice(musiclist))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

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

        # DON'T DRAW ANYTHING ABOVE HERE
        DISPLAYSURF.fill(BLACK) #Should be first thing in draw order
        world.draw(DISPLAYSURF)
        player.update(key, walls)
        player.draw()
        for npc in npcList:
            npc.update(walls, player)
            npc.draw()
            npc.nametext()
        for coin in Coins:
            if coin.update(player.rect):
                Coins.remove(coin)
                player.points += 1
            coin.draw()
        # DON'T DRAW ANYTHING BELOW HERE

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
