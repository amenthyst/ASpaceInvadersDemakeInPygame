from Objects.gameobject import Gameobject
import pygame
from Otherscripts import damagable

class Superbullet(Gameobject):
    def __init__(self, superbullettexture, position: tuple, speed: float, damage: int, piercing: int):
        self.superbullettexture = superbullettexture
        self.position = position
        self.speed = speed
        self.damage = damage
        self.piercing = piercing
        self.superbulletrect = self.superbullettexture.get_rect(center=self.position)
    def display(self, screen):
        screen.blit(self.superbullettexture, self.superbulletrect)
    def move(self):
        import main
        self.superbulletrect.y -= self.speed
        if self.superbulletrect.y < -100:
            main.objects.remove(self)
    def attack(self):
        import main
        for gameobject in main.objects:
            if gameobject == self or gameobject == main.objects[0]:
                continue
            if gameobject.getrect().colliderect(self.superbulletrect):
                if isinstance(gameobject, damagable.damagable):
                    gameobject.damage(self.damage)
                    self.piercing -= 1
                if self.piercing == 0:
                    try:
                        main.objects.remove(self)
                    except ValueError:
                        continue
    def getrect(self):
        return self.superbulletrect
    def getID(self):
        return "Superbullet"

    def update(self):
        self.move()
        self.attack()