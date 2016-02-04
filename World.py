import sys, pygame

xlen = 80
ylen = 80

tilelen = 10


# Some basic colours for use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class World(pygame.sprite.Sprite):
    def __init__(self, player):
        super(World, self).__init__()

        self.Tiles = [[0 for x in range(xlen)] for x in range(ylen)]

        # Lists for actors/objects in world
        self.wallList = pygame.sprite.Group()
        self.floorList = pygame.sprite.Group()
        self.npcList = pygame.sprite.Group()
        self.player = player

        self.wallImg = pygame.Surface([tilelen, tilelen])
        self.wallImg.fill((255, 255, 255))
        self.wallRect = self.wallImg.get_rect()

        # How much world has shifted in x or y
        self.worldShift = ((0, 0))
        self.leftViewbox = xlen / 2 - xlen / 10
        self.rightViewbox = xlen / 2 + xlen / 5

    def shiftWorld(self, shift):
        self.worldShift += shift

        for wall in self.wallList:
            wall.rect.x += shift(0)
            wall.rect.y += shift(1)

        for floor in self.floorList:
            floor.rect.x += shift(0)
            floor.rect.y += shift(1)

        for NPC in self.NPCList:
            NPC.rect.x += shift(0)
            NPC.rect.y += shift(1)

    def viewbox(self):
        if self.player.rect.x <= self.leftViewbox:
            viewDiff = self.leftViewbox - self.player.rect.x
            self.player.rect.x = self.leftViewbox
            self.shiftWorld(viewDiff)

        if self.player.rect.x >= self.rightViewbox:
            viewdiff = self.rightViewbox - self.player.rect.x
            self.player.rect.x = self.rightViewbox
            self.shiftWorld(viewDiff)

    def load(self, fileName):
        x = 0
        y = 0
        f = open(fileName, 'r')

        for y in range(ylen):
            for x in range(xlen):
                color = BLACK
                if self.Tiles[x][y] == 'x':
                    self.wallList.append()
                #if self.Tiles[x][y] == '0':

        # for line in f:
        #     while x < len(line):
        #         self.Tiles[x][y] = line[x]
        #         if line[x] == 's':
        #             self.spawnrect = pygame.Rect(tilelen*x, tilelen*y, tilelen, tilelen)
        #         x = x + 1
        #     x = 0
        #     y = y + 1

    def GetCollisionRects(self):
        rects = []
        for y in range(ylen):
            for x in range(xlen):
                color = BLACK
                if self.Tiles[x][y] == 'x':
                    rects.append(pygame.Rect(tilelen*x, tilelen*y, tilelen, tilelen))
        return rects

    # Updates all entities
    def update(self):
        self.wallList.update()
        self.npcList.update()

# Draw all entities to screen
    def draw(self, screen):
        self.wallList.draw(screen)
        self.floorList.draw(screen)
        self.npcList.draw(screen)

        # for y in range(ylen):
        #     for x in range(xlen):
        #         color = BLACK
        #         if self.Tiles[x][y] == '0':
        #             color = BLACK
        #         elif self.Tiles[x][y] == 'x':
        #             color = GREEN
        #
        #         sprite = pygame.Surface([tilelen,tilelen])
        #         sprite.fill(color)
        #         (tilelen*x, tilelen*y, tilelen, tilelen)
        #
        #         #tileRect = sprite.get_rect()
        #
        #         screen.blit(sprite,
        #                     (pygame.Rect(tilelen*x, tilelen*y, tilelen, tilelen)))

# Startup Edmonton Level
class hackOffice(World):
    def __init__(self, player):
        World.__init__(self, player)

# O = open space, no collision, no interaction
# X = wall, causes collision
# # = number defines another level to load
# $ = coin
