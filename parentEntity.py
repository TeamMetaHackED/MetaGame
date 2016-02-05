import sys
import pygame
import random
import gameFunctions
from pygame.locals import *
from gameFunctions import *

pygame.init()

YELLOW = (255, 255, 0)

# Creates parent game entity class
# Create child class with this as parent like "class Entity(GameEntity):"calling GameEntity.__init__(dependencies) in class init function.

# Main constructor for entities
class GameEntity(pygame.sprite.Sprite):
    def __init__(self, x, y, delta, surface, colour):
        # Defines what surface entity is drawn to
        super(GameEntity, self).__init__()
        self.surface = surface

        # Gets entity image and associated rect
        self.image = pygame.Surface([20, 20]) # Not sure how to get stuff from bitmap
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # creates special rect to see if entities can interact
        self.influenceRange = self.rect.copy()
        self.influenceRange = self.influenceRange.inflate(25, 25)
        self.influenceRange.center = self.rect.center

        # sets movement speed
        self.delta = delta

    # Functions to be called to trigger entity movement
    # States should make it easier to detect collision with screen borders etc
    def move(self):
        if self.dx != 0:
            self.rect.centerx += self.dx * self.delta
            self.dy = 0

        elif self.dy !=0:
            self.rect.centery += self.dy * self.delta
            self.dx = 0

    # Checks for collisions
    # def collisionDetect(self, walls):
    #     for wall in walls:
    #         if self.rect.colliderect(wall):
    #             if self.dy == -1:
    #                 self.rect.top = wall.bottom
    #             if self.dy == 1:
    #                 self.rect.bottom = wall.top
    #             if self.dx == -1:
    #                 self.rect.left = wall.right
    #             if self.dx == 1:
    #                 self.rect.right = wall.left

    # Draws each rect to the main surface
    def draw(self):
        self.surface.blit(self.image, self.rect)


class Player(GameEntity):
    def __init__(self, x, y, delta, surface, colour):
        # Constructs player with GameEntity as parent
        GameEntity.__init__(self, x, y, delta, surface, colour)

        # sets initial movement values
        self.dx = 0
        self.dy = 0

        # Defines player specific variables
        self.inventory = {}
        self.points = 0

    # Interprets player inputs
    def playerInput(self, key):
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
        #self.collisionDetect()

    def draw(self):
        pointMsg = Text("Points: " + str(self.points), 18, YELLOW, 0, 0)
        msgRect = self.rect.copy()
        msgRect.x -= 300
        msgRect.y += 250
        GameEntity.draw(self)
        pointMsg.update(self.surface, 50, 700)

    # Updates entity x and y positions then draws to main surface
    def update(self, key):
        self.playerInput(key)
        self.influenceRange.center = self.rect.center


class NPC(GameEntity):
    def __init__(self, x, y, delta, surface, colour, name, dialogue, activity):
        # Constructs NPC with GameEntity as parent
        GameEntity.__init__(self, x, y, delta, surface, colour)

        # sets initial movement values
        self.dx = 0
        self.dy = 0

        self.talking = False
        self.speech = pygame.mixer.Sound("music/voices/Female1.ogg")

        # what NPCs will say when interacted with
        self.name = name
        self.dialogue = dialogue
        self.colour = colour

        # How much NPCs move around
        self.activity = 100 * activity

    # Just basic random movements now, may add more complexity as collision is improved
    def computerAI(self):
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

        #self.collisionDetect()
        self.move()

    def interact(self, player):
        #call drawtext if conditions meat
        #Changes self.dialogue if conditions met
        if self.influenceRange.colliderect(player.influenceRange):
            if not self.talking:
                self.talking = True
                self.speech.play()
            self.messagetext()
        else:
            self.talking = False

    # Uses text class from gameFunctions.py
    # Displays name of NPC next to them
    def nametext(self):
        name = gameFunctions.Text(self.name, 18, self.colour, self.rect.x, self.rect.y)
        textRect = self.rect.copy()
        name.update(self.surface, textRect.x + 20, textRect.y)

    # Displays predefined message when NPC interacted with
    def messagetext(self):
        message = gameFunctions.Text(self.dialogue, 15, self.colour, self.rect.x, self.rect.y)
        textRect = self.rect.copy()
        message.update(self.surface, textRect.x + 20, textRect.y + 40)

    # Updates entity x and y positions then draws to main surface
    def update(self, player):
        self.computerAI()
        self.interact(player)
        self.influenceRange.center = self.rect.center


class Item(GameEntity):
    def __init__(self, x, y, surface, colour):
        GameEntity.__init__(self, x, y, 0, surface, colour)
        self.pickedUp = False
        self.image = pygame.Surface([10, 10])
        self.image.fill(YELLOW)

    # returns true when picked up
    def update(self, playerRect):
        if self.rect.colliderect(playerRect):
            self.pickedUp = True
            return True
        return False

# Creates class for walls.  Might make it easier to do collisions because of spritecollide
class Wall(GameEntity):
    def __init__(self, x, y, surface, colour):
        GameEntity.__init__(self, x, y, 0, surface, colour)
