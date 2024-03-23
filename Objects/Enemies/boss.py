
from Objects.Enemies.deflectbullet import Deflectbullet
from Objects.Enemies.explosion import Explosion
from Objects.Powerups.heart import Heart
from Objects.Powerups.energy import Energy
from Initializescripts.damagable import damagable
import pygame

class Boss(pygame.sprite.Sprite, damagable):
    def __init__(self, bosstexture, position: tuple, health: float, speed: float, attackvalue: int, score: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = bosstexture
        self.health = health
        self.speed = speed
        self.attackvalue = attackvalue
        self.score = score
        self.dt = 0
        self.stuncount = 0
        self.stunflag = False

        self.rect = self.image.get_rect(center=position)
        self.bulletcount = 0
        self.marked = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        import main
        if len(main.ship.sprites()) != 0:
            shippos = pygame.math.Vector2(main.shipobj.getposition())
            self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
            playerdir = shippos - self.position
            if playerdir.length():
                playerdir.normalize_ip()
            if self.stunflag == False:
                self.rect.x += (playerdir * self.speed)[0]
                self.rect.y += (playerdir * self.speed)[1]





    def cooldown(self):
        self.dt += 1
        if self.dt > 90:
            self.dt = 0
            return 1

    def stuntimer(self):
        self.stuncount += 1
        if self.stuncount > 180:
            self.stuncount = 0
            return 1

    def getID(self):
        return "Boss"

    def damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.death()

    def death(self):
        import main
        pygame.mixer.Sound.set_volume(main.boomsfx, 0.05)
        main.boomsfx.play()
        for i in range(0,3):
            heart = Heart(main.hearttexture, (self.rect.x, self.rect.y), 5.0, 25)
            main.powerups.add(heart)
        for i in range(0,3):
            energy = Energy(main.energytexture, (self.rect.x, self.rect.y), 5.0)
            main.powerups.add(energy)
        death = Explosion((self.rect.x, self.rect.y + 50), main.explosion)
        main.explosions.add(death)
        main.shipobj.addscore(50)
        self.kill()

    def shoot(self):
        import main
        deflectbullettexture = pygame.transform.scale(main.deflectbullettexture, (30,50))
        # shoots 3 bullets in each direction
        if self.cooldown() is not None and self.stunflag == False:
            for i in range(3):
                bossbullet = Deflectbullet(deflectbullettexture, (self.rect.x + i * 30, self.rect.y), 15.0, 5, "down")
                main.bullets.add(bossbullet)
            for i in range(3):
                bossbullet = Deflectbullet(pygame.transform.rotate(deflectbullettexture, 270), (self.rect.x, self.rect.y + i * 30 + 10), 15.0, 5, "left")
                main.bullets.add(bossbullet)
            for i in range(3):
                bossbullet = Deflectbullet(pygame.transform.rotate(deflectbullettexture, 90), (self.rect.x, self.rect.y + i * 30 + 10), 15.0, 5, "right")
                main.bullets.add(bossbullet)
            for i in range(3):
                bossbullet = Deflectbullet(pygame.transform.rotate(deflectbullettexture, 180), (self.rect.x + i * 30, self.rect.y), 15.0, 5, "up")
                main.bullets.add(bossbullet)
            main.shootsfx.play()

    def update(self):
        self.stun()
        self.move()
        self.shoot()


    def stun(self):
        import main
        # stuns the thing
        for bullet in main.bullets:
            if bullet.getID() == "Superbullet":
                self.stunflag = True
                return
        if self.stuntimer() is not None:
            self.stunflag = False
    def getrect(self):
        return self.rect