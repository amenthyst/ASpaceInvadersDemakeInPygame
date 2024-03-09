from Objects.gameobject import Gameobject
from Otherscripts.damagable import damagable
import pygame

class Dangerzone(pygame.sprite.Sprite, Gameobject, damagable):
    def __init__(self, dangerzone, position: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.dangerzone = dangerzone
        self.position = position
        self.dangerzonerect = self.dangerzone.get_rect(topleft=self.position)
    def draw(self, screen):
        screen.blit(self.dangerzone, self.dangerzonerect)
    def getrect(self):
        return self.dangerzonerect
    def getID(self):
        return "Dangerzone"
    def damage(self, damage):
        import main
        main.objects[0].addscore(-damage*4)
        main.objects[0].Harddamage(damage)
    def checkdeath(self):
        import main
        if main.objects[0].getID() != 'Ship':
            main.objects.remove(self)
    def update(self):
        self.checkdeath()