import sys, pygame

xlen = 80
ylen = 80

tilepic = pygame.image.load("tile.jpg")
tilerect = tilepic.get_rect()
tilelen = 10

# Some basic colours for use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 255)
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
                x = x + 1
            x = 0
            y = y + 1

<<<<<<< HEAD
=======
    def GetCollisionRects(self):
        rects = []
        for y in range(ylen):
            for x in range(xlen):
                color = BLACK
                if self.Tiles[x][y] == 'X':
                    rects.append(pygame.Rect(tilelen*x, tilelen*y, tilelen, tilelen))
        return rects


>>>>>>> 1b3266e54f735df3296a2bc0a76577959b97f0df
    def draw(self, screen):
        for y in range(ylen):
            for x in range(xlen):
                color = BLACK
                if self.Tiles[x][y] == 'O':
                    color = BLACK
                elif self.Tiles[x][y] == 'X':
                    color = GREEN
                pygame.draw.rect(screen, color, (tilelen*x, tilelen*y, tilelen, tilelen), 0)


# O = open space, no collision, no interaction
# X = wall, causes collision
# # = number defines another level to load
