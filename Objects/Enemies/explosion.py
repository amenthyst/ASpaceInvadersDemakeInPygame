
import pygame
class Explosion(pygame.sprite.Sprite):
    def __init__(self, position:tuple, explosion):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = explosion
        self.rect = self.image.get_rect(center=self.position)
        self.dt = 0
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def getrect(self):
        return self.rect
    def getID(self):
        return "Explosion"

    def time(self):
        self.dt += 1
        if self.dt == 10:
            self.dt = 0
            return 1
    def update(self):
        if self.time() is not None:
            self.kill()