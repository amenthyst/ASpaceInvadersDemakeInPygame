
import pygame

class Energy(pygame.sprite.Sprite):
    def __init__(self, energytexture, position: tuple, speed: float):
        pygame.sprite.Sprite.__init__(self)
        self.image = energytexture
        self.position = position
        self.speed = speed
        self.rect = self.image.get_rect(center=self.position)
    def move(self):
        self.rect.y += self.speed
        if self.rect.y < -100:
            self.kill()
    def getrect(self):
        return self.rect
    def getID(self):
        return "Energy"
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def charge(self):
        from main import shipobj
        if shipobj.rect.colliderect(self.rect):
            shipobj.charge(1)
            self.kill()
    def update(self):
        self.charge()
        self.move()
