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
class GameEntity():
    def __init__(self, x, y, delta, surface, colour):
        # Defines what surface entity is drawn to
        self.surface = surface

        # Gets entity image and associated rect
        self.sprite = pygame.Surface([20, 20]) # Not sure how to get stuff from bitmap
        self.sprite.fill(colour)

        self.rect = self.sprite.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

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
    def draw(self, cam):
        self.surface.blit(self.sprite, cam.applyRect(self.rect))


class Player(GameEntity):
    def __init__(self, x, y, delta, surface, colour):
        # Constructs player with GameEntity as parent
        GameEntity.__init__(self, x, y, delta, surface, colour)

        # sets initial movement values
        self.dx = 0
        self.dy = 0

        self.points = 0

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

    def draw(self, cam):
        pointMsg = Text("Points: " + str(self.points), 12, YELLOW, 0, 0)
        msgRect = self.rect.copy()
        msgRect.x -= 300
        msgRect.y += 250
        GameEntity.draw(self, cam)
        pointMsg.display(self.surface, cam.applyRect(msgRect))

    # Updates entity x and y positions then draws to main surface
    def update(self, key, walls):
        self.playerInput(key, walls)

# Could create "sphere of influence" around NPC that player can interact inside of
class NPC(GameEntity):
    def __init__(self, x, y, delta, surface, colour, name, dialogue, activity):
        # Constructs NPC with GameEntity as parent
        GameEntity.__init__(self, x, y, delta, surface, colour)

        # sets initial movement values
        self.dx = 0
        self.dy = 0

        self.talking = False
        self.speech = pygame.mixer.Sound("music/voices/Male2.ogg")

        # what NPCs will say when interacted with
        self.name = name
        self.dialogue = dialogue
        self.colour = colour

        # How much NPCs move around
        self.activity = 100 * activity

        self.rect = self.rect.inflate(30, 30)

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

        self.collisionDetect(walls)
        self.move()

    def interact(self, surface, player, camera):
        #call drawtext if conditions meat
        #Changes self.dialogue if conditions met
        if self.rect.colliderect(player.rect):
            if not self.talking:
                self.talking = True
                self.speech.play()
            self.messagetext(surface, camera)
        else:
            self.talking = False

    def nametext(self, surface, camera):
        name = gameFunctions.Text(self.name, 14, self.colour, self.rect.x, self.rect.y)
        textRect = self.rect.copy()
        textRect.x += 20
        name.display(surface, camera.applyRect(textRect))

    def messagetext(self, surface, camera):
        message = gameFunctions.Text(self.dialogue, 11, self.colour, self.rect.x, self.rect.y)
        textRect = self.rect.copy()
        textRect.x += 20
        textRect.y += 40
        message.display(surface, camera.applyRect(textRect))

    # Updates entity x and y positions then draws to main surface
    def update(self, walls, surface, player, camera):
        self.computerAI(walls)
        self.interact(surface, player, camera)


class Item(GameEntity):
    def __init__(self, x, y, surface, colour):
        GameEntity.__init__(self, x, y, 0, surface, colour)
        self.pickedUp = False
        self.sprite = pygame.Surface([10, 10])
        self.sprite.fill(YELLOW)

    # returns true when picked up
    def update(self, playerRect):
        if self.rect.colliderect(playerRect):
            self.pickedUp = True
            return True
        return False
