
from Initializescripts.damagable import damagable
import pygame

class Dangerzone(pygame.sprite.Sprite, damagable):
    def __init__(self, dangerzone, position: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image = dangerzone
        self.position = position
        self.rect = self.image.get_rect(topleft=self.position)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def getrect(self):
        return self.rect
    def getID(self):
        return "Dangerzone"
    def damage(self, damage):
        import main
        main.shipobj.addscore(-damage*4)
        main.shipobj.Harddamage(damage)
    def update(self):
        pass