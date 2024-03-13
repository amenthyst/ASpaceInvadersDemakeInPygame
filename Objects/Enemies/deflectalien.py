
from Otherscripts.damagable import damagable
from Objects.Enemies.deflectbullet import Deflectbullet
import random
from Objects.Powerups.heart import Heart
from Objects.Powerups.energy import Energy
from Objects.Enemies.explosion import Explosion
import pygame
class Deflectalien(pygame.sprite.Sprite, damagable):
    def __init__(self, deflectalientexture, position: tuple, health: float, speed: float, attackvalue: int, score: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = deflectalientexture
        self.position = position
        self.health = health
        self.speed = speed
        self.attackvalue = attackvalue
        self.score = score
        self.rect = self.image.get_rect(center = self.position)
        self.heartchance = random.randint(1,5)
        self.energychance = random.randint(1,5)
    def getrect(self):
        return self.rect
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def move(self):
        self.rect.y += self.speed
        if self.rect.y > 800:
            self.kill()

    def damage(self, damage):
        self.deflect()
        self.health -= damage
        if self.health <= 0:
            self.deflect()
            self.death()

    def getID(self):
        return "Deflectalien"
    def attack(self):
        import main
        if main.shipobj.rect.colliderect(self.rect):
            main.shipobj.damage(self.attackvalue)
            self.kill()
        elif main.uigroup.sprites()[1].rect.colliderect(self.rect):
            main.uigroup.sprites()[1].damage(self.attackvalue//4)
            self.kill()


    def deflect(self):
       import main
       self.hitlist = pygame.sprite.spritecollide(self, main.bullets, False)
       for bullet in self.hitlist:
           if bullet.getID() == "Laser" and self.health > 0:
               continue
           self.bullet = Deflectbullet(main.deflectbullettexture, (self.rect.x, self.rect.y), 15, 20, "down")
           main.bullets.add(self.bullet)

    def update(self):
        self.move()
        self.attack()

    def death(self):
        import main
        pygame.mixer.Sound.set_volume(main.boomsfx, 0.05)
        main.boomsfx.play()
        main.shipobj.addscore(3)
        if self.heartchance == 1:
            heart = Heart(main.hearttexture, (self.rect.x, self.rect.y), 5.0, 25)
            main.powerups.add(heart)
        if self.energychance == 1:
            energy = Energy(main.energytexture, (self.rect.x, self.rect.y), 5.0)
            main.powerups.add(energy)
        death = Explosion((self.rect.x, self.rect.y + 50), main.explosion)
        main.enemies.add(death)
        self.kill()