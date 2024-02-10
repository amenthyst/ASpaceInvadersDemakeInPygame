import pygame
from Objects.gameobject import Gameobject
from Objects.Ship.bullet import Bullet
from Otherscripts.damagable import damagable
from Objects.Ship.superbullet import Superbullet
from Objects.Ship.laser import Laser


class ShipObject(Gameobject, damagable):
    def __init__(self, spaceshiphigh, spaceshipmid, spaceshiplow, position: tuple, speed: float, health: float, maxhealth: float, energyvalue: int):
        self.spaceshiphigh = spaceshiphigh
        self.spaceshipmid = spaceshipmid
        self.spaceshiplow = spaceshiplow
        self.position = position
        self.speed = speed
        self.health = health
        self.maxhealth = maxhealth
        self.energyvalue = energyvalue
        self.spaceship = spaceshiphigh
        self.shiprect = self.spaceship.get_rect(midbottom=self.position)
        self.bulletlastframe = False
        self.superbulletlastframe = False
        self.dt = 0
        self.bulletcooldown = 0

    def display(self, screen):
        screen.blit(self.spaceship, self.shiprect)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.shiprect.x -= self.speed
            # clamps it to the screen: prevents from going left
            if self.shiprect.left <= 0:
                self.shiprect.x += self.speed
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.shiprect.x += self.speed
            # clamps it to the screen: prevents from going right
            if self.shiprect.right >= 600:
                self.shiprect.x -= self.speed
    def getrect(self):
        return self.shiprect
    def update(self):
        keys = pygame.key.get_pressed()
        self.move()
        # only shoots 1 bullet per press, doesn't shoot continuously as the space key is held
        if self.bulletlastframe == False and keys[pygame.K_SPACE]:
            self.shoot()
        self.bulletlastframe = keys[pygame.K_SPACE]
        if self.superbulletlastframe == False and keys[pygame.K_r] and self.energyvalue > 0:
            self.releasesuperbullet()
            self.energyvalue -= 1
        self.superbulletlastframe = keys[pygame.K_r]
        if keys[pygame.K_e] and self.energyvalue > 0:
            self.laser()
        if keys[pygame.K_q]:
            self.energycheat()
    def damage(self, damage):
        self.health -= damage
        if self.health > 80:
            self.spaceship = self.spaceshiphigh
        if self.health < 80 and self.health > 20:
            self.spaceship = self.spaceshipmid
        elif self.health < 20 and self.health > 0:
            self.spaceship = self.spaceshiplow
        elif self.health <= 0:
            import main
            main.objects.remove(self)
    def getID(self):
        return "Ship"
    def shoot(self):
        from main import objects,bullet
        bulletobject = Bullet(bullet, (self.shiprect.midtop[0]+10, self.shiprect.midtop[1]), 22.5, 1)
        objects.append(bulletobject)
    def heal(self, healvalue):
        self.health += healvalue
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        if self.health > 80:
            self.spaceship = self.spaceshiphigh
        elif self.health <= 60 and self.health > 20:
            self.spaceship = self.spaceshipmid
        elif self.health <= 20:
            self.spaceship = self.spaceshiplow
    def Harddamage(self, harddamage):
        self.maxhealth -= harddamage
        if self.maxhealth <= self.health:
            self.health -= harddamage
        if self.health > 80:
            self.spaceship = self.spaceshiphigh
        if self.health < 80 and self.health > 20:
            self.spaceship = self.spaceshipmid
        elif self.health < 20 and self.health > 0:
            self.spaceship = self.spaceshiplow
        elif self.health <= 0:
            import main
            main.objects.remove(self)
    def gethealth(self):
        return self.health
    def getmaxhealth(self):
        return self.maxhealth

    def getcharge(self):
        return self.energyvalue

    def charge(self, chargevalue):
        self.energyvalue += chargevalue
        if self.energyvalue > 5:
            self.energyvalue = 5

    def releasesuperbullet(self):
        import main
        superbulletobject = Superbullet(main.superbullettexture, (self.shiprect.midtop[0]+5, self.shiprect.midtop[1]),  25.0, 3, 3)
        main.objects.append(superbulletobject)

    def cooldown(self):
        self.dt += 1
        if self.dt > 30:
            self.dt = 0
            return 1

    def laser(self):
        import main
        laserobject = Laser(main.lasertexture, (self.shiprect.midtop[0]+14, self.shiprect.midtop[1]),  20.0, 0.15)
        main.objects.append(laserobject)
        if self.cooldown() is not None:
            self.energyvalue -= 1
    def energycheat(self):
        self.energyvalue = 5















