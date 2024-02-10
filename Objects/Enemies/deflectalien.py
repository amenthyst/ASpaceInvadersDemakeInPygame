from Objects.gameobject import Gameobject
from Otherscripts.damagable import damagable
from Objects.Enemies.deflectbullet import Deflectbullet
import random
from Objects.Powerups.heart import Heart
from Objects.Powerups.energy import Energy
class Deflectalien(Gameobject, damagable):
    def __init__(self, deflectalientexture, position: tuple, health: float, speed: float, attackvalue: int):
        self.deflectalien = deflectalientexture
        self.position = position
        self.health = health
        self.speed = speed
        self.attackvalue = attackvalue
        self.deflectalienrect = self.deflectalien.get_rect(center = self.position)
        self.heartchance = random.randint(1,5)
        self.energychance = random.randint(1,5)
    def getrect(self):
        return self.deflectalienrect
    def display(self, screen):
        screen.blit(self.deflectalien, self.deflectalienrect)
    def move(self):
        self.deflectalienrect.y += self.speed
        if self.deflectalienrect.y >= 800:
            import main
            main.objects.remove(self)

    def damage(self, damage):
        self.deflect()
        self.health -= damage
        if self.health <= 0:
            import main
            if self.heartchance == 1:
                heart = Heart(main.hearttexture, (self.deflectalienrect.x, self.deflectalienrect.y), 5.0, 20)
                main.objects.append(heart)
            if self.energychance == 1:
                energy = Energy(main.energytexture, (self.deflectalienrect.x, self.deflectalienrect.y), 5.0)
                main.objects.append(energy)
            for gameobject in main.objects:
                if gameobject.getID() == 'Laser':
                    if gameobject.getrect().colliderect(self.deflectalienrect):
                        deflectbullet = Deflectbullet(main.deflectbullettexture, (self.deflectalienrect.x, self.deflectalienrect.y), 20.0, 25)
                        main.objects.append(deflectbullet)
            main.objects.remove(self)
    def getID(self):
        return "Deflectalien"
    def attack(self):
        import main
        for gameobject in main.objects:
            if gameobject == self:
                continue
            if gameobject.getrect().colliderect(self.deflectalienrect) and gameobject.getID() == 'Ship':
                main.objects[0].damage(self.attackvalue)
                main.objects.remove(self)
            elif gameobject.getrect().colliderect(self.deflectalienrect) and gameobject.getID() == "Dangerzone":
                main.objects[2].damage(self.attackvalue//4)
                try:
                    main.objects.remove(self)
                except ValueError:
                    continue


    def deflect(self):
       from main import objects, deflectbullettexture
       for gameobject in objects:
            if gameobject.getID() == "Bullet":
                if gameobject.getrect().colliderect(self.deflectalienrect):
                    deflectbullet = Deflectbullet(deflectbullettexture, (self.deflectalienrect.x, self.deflectalienrect.y), 20.0, 25)
                    objects.append(deflectbullet)
            elif gameobject.getID() == "Superbullet":
                if gameobject.getrect().colliderect(self.deflectalienrect):
                    deflectbullet = Deflectbullet(deflectbullettexture, (self.deflectalienrect.x, self.deflectalienrect.y), 20.0, 25)
                    objects.append(deflectbullet)


    def update(self):
        self.move()
        self.attack()

