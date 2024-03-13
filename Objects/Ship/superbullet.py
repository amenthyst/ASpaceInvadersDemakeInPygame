
from Otherscripts import damagable
import pygame
class Superbullet(pygame.sprite.Sprite):
    def __init__(self, superbullettexture, position: tuple, speed: float, damage: int, piercing: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = superbullettexture
        self.position = position
        self.speed = speed
        self.damage = damage
        self.piercing = piercing
        self.rect = self.image.get_rect(center=self.position)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def move(self):
        import main
        self.rect.y -= self.speed
        if self.rect.y < -100:
            self.kill()
    def attack(self):
        import main
        for enemy in main.enemies:
            if enemy.getrect().colliderect(self.rect) and isinstance(enemy, damagable.damagable):
                enemy.damage(self.damage)
                self.piercing -= 1
            if self.piercing == 0:
                self.kill()

    def getrect(self):
        return self.rect
    def getID(self):
        return "Superbullet"

    def update(self):
        self.move()
        self.attack()