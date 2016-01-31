import sys
import pygame

pygame.init()

# Creates parent game entity class
# Create child class with this as parent like "class Entity(GameEntity):"calling GameEntity.__init__(dependencies) in class init function.

class GameEntity():

    # Constructor for entity
    def __init__(self, x, y, delta, surface):
        # sets initial x and y postion for entity
        self.xpos = x
        self.ypos = y

        # Defines what surface entity is drawn to
        self.surface = surface

        # Gets entity image and associated rect
        self.sprite = pygame.rect.Rect((self.xpos, self.ypos, 5, 5)) # Not sure how to get stuff from bitmap
        #self.rect = self.sprite.get_rect()

        # Can later be used for boolean state comparisons (Running, activated, etc)
        self.state = "STOP" # Set to not moving

        # sets movement speed
        self.delta = delta

    # Functions to be called to trigger entity movement
    # States should make it easier to detect collision with screen borders etc
    def moveup(self):
        self.sprite.y -= self.delta
        self.state = "UP"

    def movedown(self):
        self.sprite.y += self.delta
        self.state = "DOWN"

    def moveleft(self):
        self.sprite.x -= self.delta
        self.state = "LEFT"

    def moveright(self):
        self.sprite.x += self.delta
        self.state = "RIGHT"

    def stop(self):
        self.state = "STOP"

    # Draws each rect to the main surface
    def draw(self):
        pygame.draw.rect(self.surface, (255, 255, 255), self.sprite)

    # Updates entity x and y positions then draws to main surface
    def update(self):
        #self.sprite.x = self.xpos
        #self.sprite.y = self.ypos

        self.draw()
