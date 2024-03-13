
import pygame
class Deflectbullet(pygame.sprite.Sprite):
    def __init__(self, deflectbullettexture, position: tuple, speed: float, damage: int, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = deflectbullettexture
        self.position = position
        self.speed = speed
        self.damage = damage
        self.direction = direction
        self.rect = self.image.get_rect(center=self.position)
        self.CONTROLS = {
            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0)
        }
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def move(self):
        self.bulletdir = pygame.math.Vector2()
        self.bulletdir += self.CONTROLS[self.direction]

        if self.bulletdir.length():
            self.bulletdir.normalize_ip()

        self.bulletdir *= self.speed

        self.rect.x += self.bulletdir[0]
        self.rect.y += self.bulletdir[1]

        if self.rect.x < -50 or self.rect.x > 650 or self.rect.y < -50 or self.rect.y > 650:
            self.kill()

    def getrect(self):
        return self.rect
    def getID(self):
        return "Deflectbullet"
    def attack(self):
        import main
        if main.shipobj.rect.colliderect(self.rect):
            main.shipobj.damage(self.damage)
            self.kill()
    def update(self):
        self.move()
        self.attack()
