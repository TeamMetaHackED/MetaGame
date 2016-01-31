# Stuff like cameras, menus, etc
import pygame

class Camera():
    # http://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame/14357169#14357169
    # used as reference
    def __init__(self, width, height):
        self.state = pygame.Rect(0, 0, width, height)

    # transform rectangle coordinates into camera space
    # call this on any rects you pass to a render
    def applyRect(self, rect):
        return rect.move(self.state.topleft)

    # camera follows target
    def trackMethod(self, target):
        l, t, _, _ = target
        _, _, w, h = self.state
        return pygame.Rect(-l+400, -t+400, w, h)

    def update(self, target):
        self.state = self.trackMethod(target)

class Text():
    def __init__(self, message, size, textcolour, x, y):
        self.font = pygame.font.Font("npc_dialogue/slkscreb.ttf", size)
        self.surface = self.font.render(message, True, textcolour)
        self.rect = self.surface.get_rect()

    def display(self, surface, cam):
        surface.blit(self.surface, cam)

    def update(self, surface):
        self.rect.x = x - 50
        self.rect.y = y - 100

        self.display(surface)
