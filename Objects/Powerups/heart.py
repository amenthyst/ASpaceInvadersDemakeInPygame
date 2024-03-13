import pygame

class Heart(pygame.sprite.Sprite):
    def __init__(self, hearttexture, position: tuple, speed: float, healvalue: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = hearttexture
        self.position = position
        self.speed = speed
        self.healvalue = healvalue
        self.rect = self.image.get_rect(center=self.position)
    def move(self):
        self.rect.y += self.speed
        if self.rect.y < -100:
            self.kill()
    def getID(self):
        return "Heart"
    def getrect(self):
        return self.rect
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def heal(self):
        from main import shipobj
        if shipobj.rect.colliderect(self.rect):
            shipobj.heal(self.healvalue)
            self.kill()
    def update(self):
        self.heal()
        self.move()
