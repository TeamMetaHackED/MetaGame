import pygame
import sys
from pygame.locals import *

# Creates parent game entity class
# Create child class with this as parent like "class Entity(GameEntity):"calling GameEntity.__init__(dependencies) in class init function.

class GameEntity():

    # Constructor for entity
    def __init__(self, x, y, state, delta, health):
        # sets initial x and y postion for entity
        self.xpos = x
        self.ypos = y

        # Can later be used for boolean state comparisons (Running, activated, etc)
        self.state = ""

        self.health = health

        # sets movement speed
        self.delta = delta

    # Functions to be called to trigger entity movement
    def moveup(self):
        self.ypos -= self.delta

    def movedown(self):
        self.ypos += self.delta

    def moveleft(self):
        self.xpos -= self.delta

    def moveright(self):
        self.xpos += self.delta

    def update(self):
