import sys
import pygame
import random
from pygame.locals import *

pygame.init()

# Creates parent game entity class
# Create child class with this as parent like "class Entity(GameEntity):"calling GameEntity.__init__(dependencies) in class init function.

# Main constructor for entities
class GameEntity():
    def __init__(self, x, y, delta, surface):
        # sets initial x and y postion for entity
        self.xpos = x
        self.ypos = y

        # Defines what surface entity is drawn to
        self.surface = surface

        # Gets entity image and associated rect
        self.sprite = pygame.rect.Rect((self.xpos, self.ypos, 5, 5)) # Not sure how to get stuff from bitmap
        #self.rect = self.sprite.get_rect()

        # sets movement speed
        self.delta = delta

    # Functions to be called to trigger entity movement
    # States should make it easier to detect collision with screen borders etc
    def move(self, dx, dy):
        self.sprite.x += dx*self.delta
        self.sprite.y += dy*self.delta

    # Draws each rect to the main surface
    def draw(self):
        pygame.draw.rect(self.surface, (255, 255, 255), self.sprite)


class Player(GameEntity):
    def __init__(self, x, y, delta, surface):
        # Constructs player with GameEntity as parent
        GameEntity.__init__(self, x, y, delta, surface)

        # Defines player specific variables
        self.inventory = {}

    # Interprets player inputs
    def playerInput(self, key, walls):
        backupX = self.xpos
        backupY = self.ypos

        if key [K_w]:
            GameEntity.move(0, -1)
        if key [K_s]:
            GameEntity.move(0, 1)
        if key [K_a]:
            GameEntity.move(-1, 0)
        if key [K_d]:
            GameEntity.move(1, 0)

        for wall in walls:
            if self.sprite.colliderect(wall):
                if self.state == "UP":
                    self.sprite.top = wall.bottom
                if self.state == "DOWN":
                    self.sprite.bottom = wall.top
                if self.state == "LEFT":
                    self.sprite.left = wall.right
                if self.state == "RIGHT":
                    self.sprite.right = wall.left

    # Updates entity x and y positions then draws to main surface
    def update(self, key, walls):
        self.playerInput(key, walls)
        self.draw()

class Item(GameEntity):
    def __init__(self, x, y, surface):
        GameEntity.__init__(self, x, y, 0, surface)
        self.pickedUp = false

    def update():
        self.draw()


class NPC(GameEntity):
    def __init__(self, x, y, delta, surface, name, dialogue, activity):
        # Constructs NPC with GameEntity as parent
        GameEntity.__init__(self, x, y, delta, surface)
        self.name = name
        self.dialogue = dialogue
        self.activity = 100 * 1/activity

    # Just basic random movements now, may add more complexity as collision is improved
    def computerAI(self):
        # Calculates random value to dictate probability of movement
        moveprob = random.randrange(0, self.activity)
        # Randomly selects direction to move in
        dirprob = random.randrange(0,4)

        if moveprob == 9:
            if dirprob == 0:
                self.moveright()
            elif dirprob == 1:
                self.moveleft()
            elif dirprob == 2:
                self.moveup()
            elif dirprob == 3:
                self.movedown()

    # Updates entity x and y positions then draws to main surface
    def update(self):
        self.sprite.x = self.xpos
        self.sprite.y = self.ypos

        self.computerAI()

        self.draw()
