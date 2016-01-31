import sys
import pygame
import random
from pygame.locals import *

pygame.init()

# Creates parent game entity class
# Create child class with this as parent like "class Entity(GameEntity):"calling GameEntity.__init__(dependencies) in class init function.

# Main constructor for entities
class GameEntity():
    def __init__(self, x, y, delta, surface, colour):
        # Defines what surface entity is drawn to
        self.surface = surface

        # Gets entity image and associated rect
        self.sprite = pygame.Surface([10, 10]) # Not sure how to get stuff from bitmap
        self.sprite.fill(colour)

        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y

        # sets movement speed
        self.delta = delta

    # Functions to be called to trigger entity movement
    # States should make it easier to detect collision with screen borders etc
    def move(self):
        self.rect.x += self.dx * self.delta
        self.rect.y += self.dy * self.delta

    # Checks for collisions
    def collisionDetect(self, walls):
        for wall in walls:
            if self.rect.colliderect(wall):
                if self.dy == -1:
                    self.rect.top = wall.bottom
                if self.dy == 1:
                    self.rect.bottom = wall.top
                if self.dx == -1:
                    self.rect.left = wall.right
                if self.dx == 1:
                    self.rect.right = wall.left

    # Draws each rect to the main surface
    def draw(self):
        self.surface.blit(self.sprite, self.rect.center())


class Player(GameEntity):
    def __init__(self, x, y, delta, surface, colour):
        # Constructs player with GameEntity as parent
        GameEntity.__init__(self, x, y, delta, surface, colour)

        # sets initial movement values
        self.dx = 0
        self.dy = 0

        # Defines player specific variables
        self.inventory = {}

    # Interprets player inputs
    def playerInput(self, key, walls):
        # Changes movement direction based on key press
        # Only resets to 0 when no key being pressed
        self.dx, self.dy = 0, 0

        if key [K_w]:
            self.dy = -1
        if key [K_s]:
            self.dy = 1
        if key [K_a]:
            self.dx = -1
        if key [K_d]:
            self.dx = 1

        self.move()
        self.collisionDetect(walls)

    # Updates entity x and y positions then draws to main surface
    def update(self, key, walls):
        self.playerInput(key, walls)
        self.draw()

# Could create "sphere of influence" around NPC that player can interact inside of
class NPC(GameEntity):
    def __init__(self, x, y, delta, surface, colour, name, dialogue, activity):
        # Constructs NPC with GameEntity as parent
        GameEntity.__init__(self, x, y, delta, surface, colour)

        # sets initial movement values
        self.dx = 0
        self.dy = 0

        # what NPCs will say when interacted with
        self.name = name
        self.dialogue = dialogue

        # How much NPCs move around
        self.activity = 25 * activity

    # Just basic random movements now, may add more complexity as collision is improved
    def computerAI(self, walls):
        self.dx, self.dy = 0, 0

        # Calculates random value to dictate probability of movement
        moveprob = random.randrange(1, self.activity)
        # Randomly selects direction to move in
        dirprob = random.randrange(0,4)

        # if meets criteria, changes direction based on random selection
        if moveprob == 9:
            if dirprob == 0:
                self.dy = -1
            if dirprob == 1:
                self.dy = 1
            if dirprob == 2:
                self.dx = -1
            if dirprob == 3:
                self.dx = 1

        self.move()
        self.collisionDetect(walls)

    # Updates entity x and y positions then draws to main surface
    def update(self, walls):
        self.computerAI(walls)

        self.draw()


class Item(GameEntity):
    def __init__(self, x, y, surface, colour, description):
        GameEntity.__init__(self, x, y, 0, surface, colour)
        self.pickedUp = false
        self.description = ""

    def update():
        self.draw()
