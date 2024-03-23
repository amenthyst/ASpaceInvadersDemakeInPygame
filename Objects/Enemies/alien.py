import pygame.time


from Initializescripts.damagable import damagable
from Objects.Powerups.heart import Heart
from Objects.Powerups.energy import Energy
from Objects.Enemies.explosion import Explosion
import random
class Alien(pygame.sprite.Sprite, damagable):
    def __init__(self, alientexture, position: tuple, health: float, speed: float, attackvalue: int, score: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = alientexture
        self.position = position
        self.health = health
        self.speed = speed
        self.attackvalue = attackvalue
        self.score = score
        self.rect = self.image.get_rect(center=self.position)
        self.heartchance = random.randint(1, 5)
        self.energychance = random.randint(1,3)
        self.dt = 0
        self.marked = False

    def getrect(self):
        return self.rect
    def draw(self, screen):

        screen.blit(self.image, self.rect)


    def getID(self):
        return "Alien"
    def move(self):
        # moves down the screen
        if self.rect.y < 0:
            self.rect.y += (self.speed * 1.5)
        elif self.rect.y >= 800:
            self.kill()
        else:
            self.rect.y += self.speed
    def damage(self, damage):
        self.health -= damage
        self.speed += 0.2
        if self.health <= 0:
            self.death()


    def attack(self):
        import main
        if main.shipobj.rect.colliderect(self.rect):
            main.shipobj.damage(self.attackvalue)
            self.kill()
        elif main.uigroup.sprites()[1].rect.colliderect(self.rect):
            main.uigroup.sprites()[1].damage(self.attackvalue//4)
            self.kill()
    def update(self):
        self.attack()
        self.move()

    def death(self):
        import main
        pygame.mixer.Sound.set_volume(main.boomsfx, 0.05)
        main.boomsfx.play()
        if self.heartchance == 1:
            heart = Heart(main.hearttexture, (self.rect.x, self.rect.y), 5.0, 25)
            main.powerups.add(heart)
        if self.energychance == 1:
            energy = Energy(main.energytexture, (self.rect.x, self.rect.y), 5.0)
            main.powerups.add(energy)
        death = Explosion((self.rect.x, self.rect.y + 50), main.explosion)
        main.explosions.add(death)
        main.shipobj.addscore(5)
        self.kill()













