import sys, pygame
from parentEntity import *
from constants import *

# Number of tiles in a level
xlen = 80
ylen = 80

# Length of a tile in pixels
tilelen = 30

class World():
    def __init__(self, player, surface):
        self.Tiles = [[0 for x in range(xlen)] for x in range(ylen)]

        self.surface = surface

        # Lists for actors/objects in world
        self.wallList = pygame.sprite.Group()
        self.floorList = pygame.sprite.Group()
        self.npcList = pygame.sprite.Group()
        self.coinList = pygame.sprite.Group()
        self.collideList = pygame.sprite.Group()
        self.player = player

        # How much world has shifted in x or y
        self.worldShift = [0, 0]

    # Loads the level file and interprets the data to create walls
    def load(self, filename):
        x = 0
        y = 0
        f = open(filename, 'r')

        for line in f:
            for x in range(len(line)):
                if line[x] == 'X':
                    self.wallList.add(Wall(x * tilelen, y * tilelen, self.surface, GREEN, tilelen))
                # elif line [x] == "0":
                #     self.floorList.add(Floor class or something?)
                elif line [x] == "$":
                    self.coinList.add(Item(x * tilelen, y * tilelen, self.surface, YELLOW, 10))

                #else:
                    # make an npc based on letter in text file
                    # Like R for a random character where it doesn't matter and a specific letter for event characters or something like that
            y += 1

        f.close()

        self.collideList.add(self.wallList)

    # Moves all objects and entities in the opposite direction as the player is moving, to make it appear as though the player stays at the center of the screen
    def shiftWorld(self, shift):
        self.worldShift += shift

        for wall in self.wallList:
            wall.rect.x -= shift[0]
            wall.rect.y -= shift[1]

        for floor in self.floorList:
            floor.rect.x -= shift[0]
            floor.rect.y -= shift[1]

        for NPC in self.npcList:
            NPC.rect.x -= shift[0]
            NPC.rect.y -= shift[1]

        for coin in self.coinList:
            coin.rect.x -= shift[0]
            coin.rect.y -= shift[1]

        self.player.rect.x -= shift[0]
        self.player.rect.y -= shift[1]

    # Checks for collisions
    def collisionDetect(self):
        entity = pygame.sprite.spritecollideany(self.player, self.collideList, False)

        if entity != None: # This part works
            if self.player.dy == -1:
                self.player.rect.top = entity.rect.bottom # Stopping motion doesn't work
            if self.player.dy == 1:
                self.player.rect.bottom = entity.rect.top
            if self.player.dx == -1:
                self.player.rect.left = entity.rect.right
            if self.player.dx == 1:
                self.player.rect.right = entity.rect.left

            print ("HI THERE BITCH")

    # Updates all entities
    def update(self, key):
        self.collisionDetect()

        for wall in self.wallList:
            wall.update()

        for npc in self.npcList:
            npc.update(self.player, self.collideList)

        for coin in self.coinList:
            if coin.update(self.player.rect):
                self.coinList.remove(coin)
                self.player.points += 1

        self.player.update(key)

    # Draw all entities to screen
    def draw(self, key):
        self.update(key)

        self.floorList.draw(self.surface)
        self.coinList.draw(self.surface)
        self.npcList.draw(self.surface)
        self.player.draw()
        self.wallList.draw(self.surface)


# Create all levels here:

# Startup Edmonton Level
class hackOffice(World):
    def __init__(self, player, surface):
        World.__init__(self, player, surface)
        filename = "Rooms/testlevel"
        self.load(filename)


# O = open space, no collision, no interaction
# X = wall, causes collision
# # = number defines another level to load
# $ = coin
