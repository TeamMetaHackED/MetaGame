# Stuff like cameras, menus, etc
import pygame

class Camera():
    # http://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame/14357169#14357169
    # used as reference
    def __init__(self, width, height):
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def applyRect(self, rect):
        return rect.move(self.state.topleft)

    def trackMethod(self, target):
        l, t, _, _ = target
        _, _, w, h = self.state
        return pygame.Rect(-l+400, -t+400, w, h)

    def update(self, target):
        self.state = self.trackMethod(target)

class Text():
    def __init__(self, message, size, textcolour, x, y):
        self.font = pygame.font.Font("npc_dialogue/8-BIT WONDER.TTF", size)
        self.surface = self.font.render(message, True, textcolour)
        self.rect = self.surface.get_rect()

    def display(self, surface):
        surface.blit(self.surface, self.rect)

    def update(self, surface):
        self.rect.centerx = x
        self.rect.centery = y

        self.display(surface)
