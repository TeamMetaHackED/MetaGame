import sys, pygame
from parentEntity import Wall
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
        self.player = player

        # How much world has shifted in x or y
        self.worldShift = [0, 0]
        # self.leftViewbox = xlen / 2 - xlen / 10
        # self.rightViewbox = xlen / 2 + xlen / 5

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

        self.player.rect.x -= shift[0]
        self.player.rect.y -= shift[1]

    # Creates the player's view area
    # def viewbox(self):
    #     if self.player.rect.x <= self.leftViewbox:
    #         viewDiff = self.leftViewbox - self.player.rect.x
    #         self.player.rect.x = self.leftViewbox
    #         self.shiftWorld(viewDiff)
    #
    #     if self.player.rect.x >= self.rightViewbox:
    #         viewdiff = self.rightViewbox - self.player.rect.x
    #         self.player.rect.x = self.rightViewbox
    #         self.shiftWorld(viewDiff)

    # Loads the level file and interprets the data to create walls
    def load(self, filename):
        x = 0
        y = 0
        f = open(filename, 'r')

        for line in f:
            for x in range(len(line)):
                if line[x] == 'x':
                    self.wallList.add(Wall(x * tilelen, y * tilelen, self.surface, GREEN, tilelen))
                # if line [x] == "0":
                #     self.floorList.add(Floor class or something?)
            y += 1

        f.close()

    # Updates all entities
    def update(self):
        for wall in self.wallList:
            wall.update()

        for npc in self.npcList:
            npc.update(self.player)

        # Collision detection here?

# Draw all entities to screen
    def draw(self):
        self.update()

        self.wallList.draw(self.surface)
        self.floorList.draw(self.surface)
        self.npcList.draw(self.surface)

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
