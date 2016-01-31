import sys
import pygame
import random

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


class Player(GameEntity):
    def __init__(self, x, y, delta, surface):
        # Constructs player with GameEntity as parent
        GameEntity.__init__(self, x, y, delta, surface)

        # Defines player specific variables
        self.inventory = {}

    # Updates entity x and y positions then draws to main surface
    def update(self):
        #self.sprite.x = self.xpos
        #self.sprite.y = self.ypos

        self.draw()


class NPC(GameEntity):
    def __init__(self, x, y, delta, surface, name, dialogue):
        # Constructs NPC with GameEntity as parent
        GameEntity.__init__(self, x, y, delta, surface)
        self.name = name
        self.dialogue = dialogue
        self.activity = 1/activity

    # Just basic random movements now, may add more complexity as collision is improved
    def computerAI(self):
        moveprob = random.randrange(0, self.activity)
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
