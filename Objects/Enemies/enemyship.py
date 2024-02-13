from Objects.gameobject import Gameobject
from Objects.Enemies.deflectbullet import Deflectbullet
from Otherscripts.damagable import damagable
from Objects.Powerups.heart import Heart
from Objects.Powerups.energy import Energy
from Objects.Enemies.explosion import Explosion
import random
import pygame
class Enemyship(Gameobject, damagable):
    def __init__(self, enemyshiptexture, position: tuple, attackvalue, speed: float, health: float):
        self.enemyship = enemyshiptexture
        self.position = position
        self.attackvalue = attackvalue
        self.speed = speed
        self.health = health
        self.enemyshiprect = self.enemyship.get_rect(center=self.position)
        self.heartchance = random.randint(1,2)
        self.energychance = random.randint(1,2)
        self.dt = 0
    def getrect(self):
        return self.enemyshiprect

    def getID(self):
        return "Enemyship"

    def display(self, screen):
        screen.blit(self.enemyship, self.enemyshiprect)

    def move(self):
        if self.enemyshiprect.y > 50:
            self.enemyshiprect.x += self.speed
            if self.enemyshiprect.x <= 0:
                self.speed = -self.speed
                self.enemyshiprect.y += 50
            elif self.enemyshiprect.x >= 550:
                self.speed = -self.speed
                self.enemyshiprect.y += 50
        else:
            self.enemyshiprect.y += self.speed/4



    def shoot(self):
        import main
        if self.cooldown() is not None:
            shipbullet = Deflectbullet(pygame.transform.scale(main.deflectbullettexture,(30,30)), (self.enemyshiprect.x, self.enemyshiprect.y), 15, 10)
            main.objects.append(shipbullet)
            pygame.mixer.Sound.set_volume(main.shootsfx, 0.1)
            main.shootsfx.play()


    def cooldown(self):
        self.dt += 1
        if self.dt > 90:
            self.dt = 0
            return 1

    def update(self):
        self.move()
        if self.enemyshiprect.y > 50:
            self.shoot()
        self.attack()

    def shipstop(self):
        self.lastspeed = self.speed
        self.speed = 0
    def damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            import main
            pygame.mixer.Sound.set_volume(main.boomsfx, 0.05)
            main.boomsfx.play()
            if self.heartchance == 1:
                heart = Heart(main.hearttexture, (self.enemyshiprect.x, self.enemyshiprect.y), 5.0, 25)
                main.objects.append(heart)
            if self.energychance == 1:
                energy = Energy(main.energytexture, (self.enemyshiprect.x, self.enemyshiprect.y), 5.0)
                main.objects.append(energy)
            death = Explosion((self.enemyshiprect.x, self.enemyshiprect.y+50), main.explosion)
            main.objects.append(death)

            main.objects.remove(self)
    def attack(self):
        import main
        for gameobject in main.objects:
            if gameobject == self:
                continue
            if gameobject.getrect().colliderect(self.enemyshiprect) and gameobject.getID() == "Ship":
                main.objects[0].damage(self.attackvalue)
                main.objects.remove(self)
            elif gameobject.getrect().colliderect(self.enemyshiprect) and gameobject.getID() == "Dangerzone":
                main.objects[2].damage(self.attackvalue)
                main.objects.remove(self)