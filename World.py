import sys, pygame
pygame.init()

xlen = 60
ylen = 60

tilepic = pygame.image.load("tile.jpg")
tilerect = tilepic.get_rect()
tilelen = 10


size = width, height = (600, 600)
screen = pygame.display.set_mode(size)
black = (0,0,0)
white = (255, 255, 255)
blue = (0, 0, 255)

class World:
    def __init__(self):
        self.Tiles = [[0 for x in range(xlen)] for x in range(ylen)]
    
    
    def Load(self, fileName):
        x = 0
        y = 0
        f = open(fileName, 'r')

        for line in f:
            while x < len(line):
                self.Tiles[x][y] = line[x]
                x = x + 1
            x = 0
            y = y + 1

#def Render(screen):

world = World()
world.Load("testlevel")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)

    for y in range(ylen):
        for x in range(xlen):
            color = white
            if world.Tiles[x][y] == 'O':
                color = black
            elif world.Tiles[x][y] == 'X':
                color = blue
            pygame.draw.rect(screen, color, (tilelen*x, tilelen*y, tilelen, tilelen), 0)

    pygame.display.update()






# O = open space, no collision, no interaction
# X = wall, causes collision
# # = number defines another level to load

    
