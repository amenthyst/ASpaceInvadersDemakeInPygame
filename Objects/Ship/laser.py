
from Initializescripts.damagable import damagable
import pygame
class Laser(pygame.sprite.Sprite):

        def __init__(self, lasertexture, position: tuple, speed: float, damage: float, direction):
            pygame.sprite.Sprite.__init__(self)
            self.image = lasertexture
            self.position = position
            self.speed = speed
            self.damage = damage
            self.direction = direction
            self.rect = self.image.get_rect(midright=self.position)
            self.CONTROLS = {
                "up": (0, -1),
                "down": (0, 1),
                "left": (-1, 0),
                "right": (1, 0)
            }

        def draw(self, screen):
            screen.blit(self.image, self.rect)

        def move(self):

            self.laserdir = pygame.math.Vector2()
            self.laserdir += self.CONTROLS[self.direction]

            if self.laserdir.length():
                self.laserdir.normalize_ip()

            self.laserdir *= self.speed

            self.rect.x += self.laserdir[0]
            self.rect.y += self.laserdir[1]

            if self.rect.x < -50 or self.rect.x > 650 or self.rect.y < -50 or self.rect.y > 650:
                self.kill()

        def getrect(self):
            return self.rect

        def getID(self):
            return "Laser"

        def attack(self):
            import main
            for enemy in main.enemies:
                if enemy.getrect().colliderect(self.rect) and isinstance(enemy, damagable):
                    enemy.damage(self.damage)
                    self.kill()

        def update(self):
            self.move()
            self.attack()