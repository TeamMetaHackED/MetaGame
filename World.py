import sys, pygame

xlen = 80
ylen = 80

tilelen = 20


# Some basic colours for use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class World:
    def __init__(self):
        self.Tiles = [[0 for x in range(xlen)] for x in range(ylen)]

    def load(self, fileName):
        x = 0
        y = 0
        f = open(fileName, 'r')

        for line in f:
            while x < len(line):
                self.Tiles[x][y] = line[x]
                if line[x] == 's':
                    self.spawnrect = pygame.Rect(tilelen*x, tilelen*y, tilelen, tilelen)
                x = x + 1
            x = 0
            y = y + 1

    def GetCollisionRects(self):
        rects = []
        for y in range(ylen):
            for x in range(xlen):
                color = BLACK
                if self.Tiles[x][y] == 'x':
                    rects.append(pygame.Rect(tilelen*x, tilelen*y, tilelen, tilelen))
        return rects

    def draw(self, screen, cam):
        for y in range(ylen):
            for x in range(xlen):
                color = BLACK
                if self.Tiles[x][y] == '0':
                    color = BLACK
                elif self.Tiles[x][y] == 'x':
                    color = GREEN

                sprite = pygame.Surface([tilelen,tilelen])
                sprite.fill(color)
                (tilelen*x, tilelen*y, tilelen, tilelen)

                #tileRect = sprite.get_rect()

                screen.blit(sprite,
                            cam.applyRect(pygame.Rect(tilelen*x, tilelen*y, tilelen, tilelen)))


# O = open space, no collision, no interaction
# X = wall, causes collision
# # = number defines another level to load
# $ = coin
