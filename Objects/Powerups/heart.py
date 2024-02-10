import pygame
from Objects.gameobject import Gameobject
class Heart(Gameobject):
    def __init__(self, hearttexture, position: tuple, speed: float, healvalue: int):
        self.hearttexture = hearttexture
        self.position = position
        self.speed = speed
        self.healvalue = healvalue
        self.heartrect = self.hearttexture.get_rect(center=self.position)
    def move(self):
        self.heartrect.y += self.speed
        if self.heartrect.y < -100:
            import main
            main.objects.remove(self)
    def getID(self):
        return "Heart"
    def getrect(self):
        return self.heartrect
    def display(self, screen):
        screen.blit(self.hearttexture, self.heartrect)
    def heal(self):
        from main import objects
        for gameobject in objects:
            if gameobject.getID() == 'Ship':
                if gameobject.getrect().colliderect(self.heartrect):
                    gameobject.heal(self.healvalue)
                    objects.remove(self)
    def update(self):
        self.heal()
        self.move()
