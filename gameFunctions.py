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
