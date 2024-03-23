from Initializescripts import damagable
import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, bullet, position: tuple, speed: float, damage: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet
        self.position = position
        self.speed = speed
        self.damage = damage
        self.rect = self.image.get_rect(midright=self.position)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def move(self):
        import main
        self.rect.y -= self.speed
        if self.rect.y < -100:
            self.kill()
    def getrect(self):
        return self.rect
    def getID(self):
        return "Bullet"

    def attack(self):
        import main
        for enemy in main.enemies:
            if enemy.rect.colliderect(self.rect) and isinstance(enemy, damagable.damagable):
                enemy.damage(self.damage)
                self.kill()

    def update(self):
        self.move()
        self.attack()


