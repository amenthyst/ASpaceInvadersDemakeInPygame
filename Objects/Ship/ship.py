import pygame
from Objects.Ship.bullet import Bullet
from Otherscripts.damagable import damagable
from Objects.Ship.superbullet import Superbullet
from Objects.Ship.laser import Laser
from Objects.Enemies.explosion import Explosion
from Objects.Ship.missile import Missile

class ShipObject(pygame.sprite.Sprite, damagable):
    def __init__(self, spaceshiphigh, spaceshipmid, spaceshiplow, position: tuple, speed: float, health: float,
                 maxhealth: float, energyvalue: int, bulletcooldown: float):

        pygame.sprite.Sprite.__init__(self)
        self.image = spaceshiphigh
        self.spaceshiphigh = spaceshiphigh
        self.spaceshipmid = spaceshipmid
        self.spaceshiplow = spaceshiplow
        self.speed = speed
        self.health = health
        self.maxhealth = maxhealth
        self.energyvalue = energyvalue
        self.bulletcooldown = bulletcooldown
        self.spaceship = spaceshiphigh
        self.rect = self.spaceship.get_rect(midbottom=position)
        self.bulletlastframe = False
        self.superbulletlastframe = False
        self.missilelastframe = False
        self.switchlastframe = False
        self.dt = 0
        self.cdcount = 0
        self.manualflag = True
        self.semiflag = False
        self.currentmode = 'MANUAL'
        self.score = 0
        # dictionary that stores vectors for each control
        self.CONTROLS = {
            pygame.K_UP: (0, -1),
            pygame.K_DOWN: (0, 1),
            pygame.K_LEFT: (-1, 0),
            pygame.K_RIGHT: (1, 0)
        }


    def draw(self, screen):
        import main
        screen.blit(self.image, self.rect)
        self.switchdisplay = main.font.render(self.currentmode, False, 'black')
        screen.blit(self.switchdisplay, (240, 550))


    def move(self):
        from main import border
        # let's see which keys are pressed, and create a
        # movement vector from all pressed keys.
        self.playerdir = pygame.math.Vector2()

        pressed = pygame.key.get_pressed()

        for vec in (self.CONTROLS[k] for k in self.CONTROLS if pressed[k]):
            self.playerdir += vec


        # checks if the vector is 0 if it isn't then normalize it (reduce it in the range of -1 and 1)
        if self.playerdir.length():
            self.playerdir.normalize_ip()

        self.playerdir *= self.speed

     
        # clamps the ship to the screen
        self.rect.x += self.playerdir[0]

        self.rect.y += self.playerdir[1]
        self.rect.clamp_ip(border)



    def getrect(self):
        return self.rect

    def update(self):
        import main
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

        if keys[pygame.K_q] and self.switchlastframe == False:
            self.switch()
        self.switchlastframe = keys[pygame.K_q]

        if self.superbulletlastframe == False and keys[pygame.K_r] and self.energyvalue > 0:
            self.releasesuperbullet()
            self.energyvalue -= 1
        self.superbulletlastframe = keys[pygame.K_r]

        if keys[pygame.K_t]:
            self.energycheat()

        if keys[pygame.K_e] and self.energyvalue > 0:
            self.laser()
            pygame.mixer.Sound.set_volume(main.lasersfx, 0.2)
            main.lasersfx.play()
        else:
            main.lasersfx.stop()

        if keys[pygame.K_f] and self.missilelastframe == False and self.energyvalue > 0:
            self.missile()
        self.missilelastframe = keys[pygame.K_f]


    def damage(self, damage):
        import main
        self.health -= damage
        self.addscore(-damage // 5)
        pygame.mixer.Sound.set_volume(main.damagesfx, 0.2)
        main.damagesfx.play()
        self.checktexture()
        if self.health <= 0:
            self.death()

    def switch(self):
        self.manualflag, self.semiflag = self.semiflag, self.manualflag
        if self.manualflag:
            self.currentmode = 'MANUAL'
        elif self.semiflag:
            self.currentmode = 'SEMIAUTO'

    def getID(self):
        return "Ship"

    def semishoot(self):
        from main import bullet, shootsfx, bullets
        if self.cooldown() is not None:
            bulletobject = Bullet(bullet, (self.rect.midtop[0] + 10, self.rect.midtop[1]), 22.5, 1)
            bullets.add(bulletobject)
            pygame.mixer.Sound.set_volume(shootsfx, 0.2)
            shootsfx.play()

    def shoot(self):
        from main import bullets, bullet, shootsfx
        bulletobject = Bullet(bullet, (self.rect.midtop[0] + 10, self.rect.midtop[1]), 22.5, 1)
        bullets.add(bulletobject)
        pygame.mixer.Sound.set_volume(shootsfx, 0.2)
        shootsfx.play()

    def heal(self, healvalue):
        import main
        pygame.mixer.Sound.set_volume(main.healsfx, 0.2)
        main.healsfx.play()
        self.health += healvalue
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        self.checktexture()

    def Harddamage(self, harddamage):
        import main
        self.maxhealth -= harddamage
        self.addscore(harddamage // 3)
        pygame.mixer.Sound.set_volume(main.damagesfx, 0.2)
        main.damagesfx.play()
        if self.maxhealth < self.health:
            self.health = self.maxhealth
        self.checktexture()
        if self.health <= 0:
            self.death()



    def charge(self, chargevalue):
        from main import chargesfx
        self.energyvalue += chargevalue
        pygame.mixer.Sound.set_volume(chargesfx, 0.2)
        chargesfx.play()
        if self.energyvalue > 5:
            self.energyvalue = 5

    def releasesuperbullet(self):
        import main
        superbulletobject = Superbullet(main.superbullettexture, (self.rect.midtop[0], self.rect.midtop[1]),
                                        25.0, 2, 3)
        main.bullets.add(superbulletobject)
        pygame.mixer.Sound.set_volume(main.superbulletsfx, 0.1)
        main.superbulletsfx.play()

    def energydrain(self):
        self.dt += 1
        if self.dt > 30:
            self.dt = 0
            return 1

    def cooldown(self):
        self.cdcount += 1
        if self.cdcount > int(self.bulletcooldown * 60):
            self.cdcount = 0
            return 1

    def getposition(self):
        return (self.rect.x, self.rect.y)

    def laser(self):
        import main
        self.image = main.spaceshiplaserlow
        laserobject = Laser(main.lasertexture, (self.rect.midtop[0] + 15, self.rect.midtop[1]), 20.0, 0.2,
                            'up')
        main.bullets.add(laserobject)
        if self.energyvalue >= 3:
            self.image = main.spaceshiplaserhigh
            laserobjectright = Laser(pygame.transform.rotate(main.lasertexture, 90),
                                     (self.rect.midright[0] + 30, self.rect.midright[1] - 3), 20.0, 0.2,
                                     'right')
            laserobjectleft = Laser(pygame.transform.rotate(main.lasertexture, 270),
                                    (self.rect.midleft[0] + 30, self.rect.midleft[1] - 3), 20.0, 0.2,
                                    'left')
            laserobjectdown = Laser(main.lasertexture, (self.rect.midbottom[0] + 15, self.rect.midbottom[1]), 20.0, 0.2,
                            'down')
            main.bullets.add(laserobjectright)
            main.bullets.add(laserobjectleft)
            main.bullets.add(laserobjectdown)
        if self.energydrain() is not None:
            self.energyvalue -= 1
        if self.energyvalue == 0:
            self.checktexture()

    def energycheat(self):
        self.energyvalue = 5

    def checktexture(self):
        if self.health > 80:
            self.image = self.spaceshiphigh
        elif self.health < 80 and self.health > 20:
            self.image = self.spaceshipmid
        elif self.health < 20 and self.health > 0:
            self.image = self.spaceshiplow

    def addscore(self, score):
        self.score += int(score)

    def getscore(self):
        return self.score

    def death(self):
        import main
        main.explosion = pygame.transform.scale(main.explosion, (100, 100))
        death = Explosion((self.rect.x, self.rect.y), main.explosion)
        main.explosions.add(death)
        pygame.mixer.Sound.set_volume(main.boomsfx, 0.5)

        main.boomsfx.play()
        self.remove(main.ship)
        main.lasersfx.stop()

    def missile(self):
        from main import missiletexture, bullets, enemies
        if len(enemies.sprites()) != 0:
            for i in range(0,2):
                self.missileobj = Missile(missiletexture, (self.rect.x+20, self.rect.y), 10, 1)
                bullets.add(self.missileobj)
            self.energyvalue -= 1
