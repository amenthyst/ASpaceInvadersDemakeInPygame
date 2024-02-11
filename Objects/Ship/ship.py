import pygame
from Objects.gameobject import Gameobject
from Objects.Ship.bullet import Bullet
from Otherscripts.damagable import damagable
from Objects.Ship.superbullet import Superbullet
from Objects.Ship.laser import Laser


class ShipObject(Gameobject, damagable):
    def __init__(self, spaceshiphigh, spaceshipmid, spaceshiplow, position: tuple, speed: float, health: float, maxhealth: float, energyvalue: int, bulletcooldown: float):

        self.spaceshiphigh = spaceshiphigh
        self.spaceshipmid = spaceshipmid
        self.spaceshiplow = spaceshiplow
        self.position = position
        self.speed = speed
        self.health = health
        self.maxhealth = maxhealth
        self.energyvalue = energyvalue
        self.bulletcooldown = bulletcooldown
        self.spaceship = spaceshiphigh
        self.shiprect = self.spaceship.get_rect(midbottom=self.position)
        self.bulletlastframe = False
        self.superbulletlastframe = False
        self.switchlastframe = False
        self.dt = 0
        self.cdcount = 0
        self.manualflag = True
        self.semiflag = False
        self.currentmode = 'MANUAL'



    def display(self, screen):
        import main
        screen.blit(self.spaceship, self.shiprect)
        self.switchdisplay = main.font.render(self.currentmode, False, 'black')
        screen.blit(self.switchdisplay, (240,550))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.shiprect.x -= self.speed
            # clamps it to the screen: prevents from going left
            if self.shiprect.left <= 0:
                self.shiprect.x += self.speed


        elif keys[pygame.K_RIGHT]:
            self.shiprect.x += self.speed
            # clamps it to the screen: prevents from going right
            if self.shiprect.right >= 600:
                self.shiprect.x -= self.speed


        elif keys[pygame.K_DOWN]:
            self.shiprect.y += self.speed
            if self.shiprect.y > 500:
                self.shiprect.y -= self.speed


        elif keys[pygame.K_UP]:
            self.shiprect.y -= self.speed
            if self.shiprect.y < 0:
                self.shiprect.y += self.speed



    def getrect(self):
        return self.shiprect
    def update(self):
        keys = pygame.key.get_pressed()
        self.move()
        self.checktexture()




        if self.manualflag:
            # only shoots 1 bullet per press, doesn't shoot continuously as the space key is held
            if self.bulletlastframe == False and keys[pygame.K_SPACE]:
                self.shoot()
            self.bulletlastframe = keys[pygame.K_SPACE]
        elif self.semiflag:
            if keys[pygame.K_SPACE]:
                self.semishoot()

        if keys[pygame.K_t] and self.switchlastframe == False:
            self.switch()
        self.switchlastframe = keys[pygame.K_t]

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
        self.checktexture()
        if self.health <= 0:
            import main
            main.objects.remove(self)

    def switch(self):
        self.manualflag, self.semiflag = self.semiflag, self.manualflag
        if self.manualflag:
            self.currentmode = 'MANUAL'
        elif self.semiflag:
            self.currentmode = 'SEMIAUTO'


    def getID(self):
        return "Ship"
    def semishoot(self):
        from main import objects,bullet
        if self.cooldown() is not None:
            bulletobject = Bullet(bullet, (self.shiprect.midtop[0]+10, self.shiprect.midtop[1]), 22.5, 1)
            objects.append(bulletobject)
    def shoot(self):
        from main import objects, bullet
        bulletobject = Bullet(bullet, (self.shiprect.midtop[0] + 10, self.shiprect.midtop[1]), 22.5, 1)
        objects.append(bulletobject)

    def heal(self, healvalue):
        self.health += healvalue
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        self.checktexture()
    def Harddamage(self, harddamage):
        self.maxhealth -= harddamage
        if self.maxhealth < self.health:
            self.health = self.maxhealth
        self.checktexture()
        if self.health <= 0:
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

    def energydrain(self):
        self.dt += 1
        if self.dt > 30:
            self.dt = 0
            return 1

    def cooldown(self):
        self.cdcount += 1
        if self.cdcount > int(self.bulletcooldown*60):
            self.cdcount = 0
            return 1


    def laser(self):
        import main
        self.spaceship = main.spaceshiplaserlow
        laserobject = Laser(main.lasertexture, (self.shiprect.midtop[0]+15, self.shiprect.midtop[1]+8),  20.0, 0.15, 'up')
        main.objects.append(laserobject)
        if self.energyvalue >= 3:
            self.spaceship = main.spaceshiplaserhigh
            laserobjectright = Laser(pygame.transform.rotate(main.lasertexture,90), (self.shiprect.midright[0]-10, self.shiprect.midright[1]-3), 20.0, 0.2,
                                'right')
            laserobjectleft = Laser(pygame.transform.rotate(main.lasertexture,270), (self.shiprect.midleft[0]+30, self.shiprect.midleft[1]-3), 20.0, 0.4,
                                'left')
            main.objects.append(laserobjectright)
            main.objects.append(laserobjectleft)
        if self.energydrain() is not None:
            self.energyvalue -= 1
        if self.energyvalue == 0:
            self.checktexture()
    def energycheat(self):
        self.energyvalue = 5


    def checktexture(self):
        if self.health > 80:
            self.spaceship = self.spaceshiphigh
        elif self.health < 80 and self.health > 20:
            self.spaceship = self.spaceshipmid
        elif self.health < 20 and self.health > 0:
            self.spaceship = self.spaceshiplow













