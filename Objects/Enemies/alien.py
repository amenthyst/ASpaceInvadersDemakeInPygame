import pygame.time

from Objects.gameobject import Gameobject
from Otherscripts.damagable import damagable
from Objects.Powerups.heart import Heart
from Objects.Powerups.energy import Energy
from Objects.Enemies.explosion import Explosion
import random
class Alien(Gameobject, damagable):
    def __init__(self, alientexture, position: tuple, health: float, speed: float, attackvalue: int, score: int):
        self.alien = alientexture
        self.position = position
        self.health = health
        self.speed = speed
        self.attackvalue = attackvalue
        self.score = score
        self.alienrect = self.alien.get_rect(center=self.position)
        self.heartchance = random.randint(1, 5)
        self.energychance = random.randint(1,3)
        self.dt = 0

    def getrect(self):
        return self.alienrect
    def display(self, screen):

        screen.blit(self.alien, self.alienrect)


    def getID(self):
        return "Alien"
    def move(self):
        # moves down the screen
        self.alienrect.y += self.speed
        if self.alienrect.y >= 800:
            import main
            main.enemies.remove(self)
    def damage(self, damage):
        self.health -= damage
        self.speed += 0.2
        if self.health <= 0:
            import main
            pygame.mixer.Sound.set_volume(main.boomsfx, 0.05)
            main.boomsfx.play()
            if self.heartchance == 1:
                heart = Heart(main.hearttexture, (self.alienrect.x, self.alienrect.y), 5.0, 25)
                main.objects.append(heart)
            if self.energychance == 1:
                energy = Energy(main.energytexture, (self.alienrect.x, self.alienrect.y), 5.0)
                main.objects.append(energy)
            death = Explosion((self.alienrect.x, self. alienrect.y + 50), main.explosion)
            main.objects.append(death)
            main.objects[0].addscore(5)
            main.enemies.remove(self)

    def attack(self):
        import main

        for gameobject in main.objects:
            if gameobject == self:
                continue
            if gameobject.getrect().colliderect(self.alienrect) and gameobject.getID() == "Ship":
                main.objects[0].damage(self.attackvalue)
                try:
                    main.enemies.remove(self)
                except ValueError:
                    continue
            elif gameobject.getrect().colliderect(self.alienrect) and gameobject.getID() == "Dangerzone":
                main.objects[2].damage(self.attackvalue//3)
                try:
                    main.enemies.remove(self)
                except ValueError:
                    continue
    def update(self):
        self.attack()
        self.move()















