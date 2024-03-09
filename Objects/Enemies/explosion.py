from Objects.gameobject import Gameobject
import pygame
class Explosion(Gameobject):
    def __init__(self, position:tuple, explosion):
        self.position = position
        self.explosion = explosion
        self.explosionrect = self.explosion.get_rect(center=self.position)
        self.dt = 0
    def draw(self, screen):
        screen.blit(self.explosion, self.explosionrect)

    def getrect(self):
        return self.explosionrect
    def getID(self):
        return "Explosion"

    def time(self):
        self.dt += 1
        if self.dt == 10:
            self.dt = 0
            return 1
    def update(self):
        import main
        if self.time() is not None:
            main.objects.remove(self)