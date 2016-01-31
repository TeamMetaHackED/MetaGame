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
    def move(self):
        self.sprite.x += self.dx * self.delta
        self.sprite.y += self.dy * self.delta

    # Draws each rect to the main surface
    def draw(self):
        pygame.draw.rect(self.surface, (255, 255, 255), self.sprite)


class Player(GameEntity):
    def __init__(self, x, y, delta, surface):
        # Constructs player with GameEntity as parent
        GameEntity.__init__(self, x, y, delta, surface)

        # sets initial movement values
        self.dx = 0
        self.dy = 0

        # Defines player specific variables
        self.inventory = {}

    # Interprets player inputs
    def playerInput(self, key, walls):
        # Changes movement direction based on key press
        # Only resets to 0 when no key being pressed
        if key [K_w]:
            self.dy = -1
        elif key [K_s]:
            self.dy = 1
        elif key [K_a]:
            self.dx = -1
        elif key [K_d]:
            self.dx = 1
        else:
            self.dx, self.dy = 0, 0
        self.move()

        for wall in walls:
            if self.sprite.colliderect(wall):
                if self.dy == -1:
                    self.sprite.top = wall.bottom
                if self.dy == 1:
                    self.sprite.bottom = wall.top
                if self.dx == -1:
                    self.sprite.left = wall.right
                if self.dx == 1:
                    self.sprite.right = wall.left

    # Updates entity x and y positions then draws to main surface
    def update(self, key, walls):
        self.playerInput(key, walls)
        self.draw()


class NPC(GameEntity):
    def __init__(self, x, y, delta, surface, name, dialogue, activity):
        # Constructs NPC with GameEntity as parent
        GameEntity.__init__(self, x, y, delta, surface)

        # sets initial movement values
        self.dx = 0
        self.dy = 0

        # what NPCs will say when interacted with
        self.name = name
        self.dialogue = dialogue

        # How much NPCs move around
        self.activity = 100 * 1.5 * activity

    # Just basic random movements now, may add more complexity as collision is improved
    def computerAI(self, walls):
        # Calculates random value to dictate probability of movement
        moveprob = random.randrange(1, self.activity)
        # Randomly selects direction to move in
        dirprob = random.randrange(0,4)

        # if meets criteria, changes direction based on random selection
        if moveprob == 9:
            if dirprob == 0:
                self.dy = -1
            elif dirprob == 1:
                self.dy = 1
            elif dirprob == 2:
                self.dx = -1
            elif dirprob == 3:
                self.dx = 1
            else:
                self.dx, self.dy = 0, 0
            self.move()

        for wall in walls:
            if self.sprite.colliderect(wall):
                if self.dy == -1:
                    self.sprite.top = wall.bottom
                if self.dy == 1:
                    self.sprite.bottom = wall.top
                if self.dx == -1:
                    self.sprite.left = wall.right
                if self.dx == 1:
                    self.sprite.right = wall.left

    # Updates entity x and y positions then draws to main surface
    def update(self, walls):
        self.sprite.x = self.xpos
        self.sprite.y = self.ypos

        self.computerAI(walls)

        self.draw()
