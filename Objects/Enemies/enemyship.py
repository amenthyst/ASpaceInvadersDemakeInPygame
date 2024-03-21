
from Objects.Enemies.deflectbullet import Deflectbullet
from Otherscripts.damagable import damagable
from Objects.Powerups.heart import Heart
from Objects.Powerups.energy import Energy
from Objects.Enemies.explosion import Explosion
import random
import pygame
class Enemyship(pygame.sprite.Sprite, damagable):
    def __init__(self, enemyshiptexture, position: tuple, attackvalue, speed: float, health: float, score: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemyshiptexture
        self.position = position
        self.attackvalue = attackvalue
        self.speed = speed
        self.health = health
        self.score = score
        self.rect = self.image.get_rect(center=self.position)
        self.heartchance = random.randint(1,2)
        self.energychance = random.randint(1,2)
        self.dt = 0
        self.marked = False
    def getrect(self):
        return self.rect

    def getID(self):
        return "Enemyship"

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.rect.y > 700:
            self.kill()

    def move(self):
        if self.rect.y > 50:
            self.rect.x += self.speed
            if self.rect.x <= 0:
                self.speed = -self.speed
                self.rect.y += 50
            elif self.rect.x >= 550:
                self.speed = -self.speed
                self.rect.y += 50
        else:
            self.rect.y += self.speed/4



    def shoot(self):
        import main
        if self.cooldown() is not None:
            shipbullet = Deflectbullet(pygame.transform.scale(main.deflectbullettexture,(30,30)), (self.rect.x, self.rect.y), 10, 10, "down")
            main.bullets.add(shipbullet)
            pygame.mixer.Sound.set_volume(main.shootsfx, 0.1)
            main.shootsfx.play()


    def cooldown(self):
        self.dt += 1
        if self.dt > 90:
            self.dt = 0
            return 1

    def update(self):
        self.move()
        if self.rect.y > 50:
            self.shoot()
        self.attack()

    def damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            import main
            pygame.mixer.Sound.set_volume(main.boomsfx, 0.05)
            main.boomsfx.play()
            main.shipobj.addscore(10)
            if self.heartchance == 1:
                heart = Heart(main.hearttexture, (self.rect.x, self.rect.y), 5.0, 25)
                main.powerups.add(heart)
            if self.energychance == 1:
                energy = Energy(main.energytexture, (self.rect.x, self.rect.y), 5.0)
                main.powerups.add(energy)
            death = Explosion((self.rect.x, self.rect.y+50), main.explosion)
            main.explosions.add(death)
            self.kill()
    def attack(self):
        import main
        if main.shipobj.rect.colliderect(self.rect):
            main.shipobj.damage(self.attackvalue)
            self.kill()
        elif main.uigroup.sprites()[1].rect.colliderect(self.rect):
            main.uigroup.sprites()[1].damage(self.attackvalue//4)
            self.kill()