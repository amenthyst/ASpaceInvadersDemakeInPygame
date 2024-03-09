from Objects.gameobject import Gameobject
from Otherscripts.damagable import damagable
from Objects.Enemies.deflectbullet import Deflectbullet
import random
from Objects.Powerups.heart import Heart
from Objects.Powerups.energy import Energy
from Objects.Enemies.explosion import Explosion
import pygame
class Deflectalien(Gameobject, damagable):
    def __init__(self, deflectalientexture, position: tuple, health: float, speed: float, attackvalue: int, score: int):
        self.deflectalien = deflectalientexture
        self.position = position
        self.health = health
        self.speed = speed
        self.attackvalue = attackvalue
        self.score = score
        self.deflectalienrect = self.deflectalien.get_rect(center = self.position)
        self.heartchance = random.randint(1,5)
        self.energychance = random.randint(1,5)
    def getrect(self):
        return self.deflectalienrect
    def draw(self, screen):
        screen.blit(self.deflectalien, self.deflectalienrect)
    def move(self):
        self.deflectalienrect.y += self.speed
        if self.deflectalienrect.y > 800:
            import main
            main.enemies.remove(self)

    def damage(self, damage):
        self.deflect()
        self.health -= damage
        if self.health <= 0:

            import main
            pygame.mixer.Sound.set_volume(main.boomsfx, 0.05)
            main.boomsfx.play()
            main.objects[0].addscore(3)
            if self.heartchance == 1:
                heart = Heart(main.hearttexture, (self.deflectalienrect.x, self.deflectalienrect.y), 5.0, 25)
                main.objects.append(heart)
            if self.energychance == 1:
                energy = Energy(main.energytexture, (self.deflectalienrect.x, self.deflectalienrect.y), 5.0)
                main.objects.append(energy)
            for gameobject in main.objects:
                if gameobject.getID() == 'Laser':
                    if gameobject.getrect().colliderect(self.deflectalienrect):
                        deflectbullet = Deflectbullet(main.deflectbullettexture, (self.deflectalienrect.x, self.deflectalienrect.y), 20.0, 25, "down")
                        main.objects.append(deflectbullet)
            death = Explosion((self.deflectalienrect.x, self.deflectalienrect.y + 50), main.explosion)
            main.objects.append(death)

            main.enemies.remove(self)
    def getID(self):
        return "Deflectalien"
    def attack(self):
        import main
        for gameobject in main.objects:
            if gameobject.getrect().colliderect(self.deflectalienrect) and gameobject.getID() == 'Ship':
                main.objects[0].damage(self.attackvalue)
                try:
                    main.enemies.remove(self)
                except ValueError:
                    continue
            elif gameobject.getrect().colliderect(self.deflectalienrect) and gameobject.getID() == "Dangerzone":
                main.objects[2].damage(self.attackvalue//3)
                try:
                    main.enemies.remove(self)
                except ValueError:
                    continue


    def deflect(self):
       from main import objects, deflectbullettexture
       for gameobject in objects:
            if gameobject.getID() == "Bullet":
                if gameobject.getrect().colliderect(self.deflectalienrect):
                    deflectbullet = Deflectbullet(deflectbullettexture, (self.deflectalienrect.x, self.deflectalienrect.y), 20.0, 25, "down")
                    objects.append(deflectbullet)
            elif gameobject.getID() == "Superbullet":
                if gameobject.getrect().colliderect(self.deflectalienrect):
                    deflectbullet = Deflectbullet(deflectbullettexture, (self.deflectalienrect.x, self.deflectalienrect.y), 20.0, 25, "down")
                    objects.append(deflectbullet)


    def update(self):
        self.move()
        self.attack()

