from Objects.gameobject import Gameobject
import pygame

class Energy(Gameobject):
    def __init__(self, energytexture, position: tuple, speed: float):
        self.energytexture = energytexture
        self.position = position
        self.speed = speed
        self.energyrect = self.energytexture.get_rect(center=self.position)
    def move(self):
        self.energyrect.y += self.speed
        if self.energyrect.y < -100:
            import main
            main.objects.remove(self)
    def getrect(self):
        return self.energyrect
    def getID(self):
        return "Energy"
    def display(self, screen):
        screen.blit(self.energytexture, self.energyrect)
    def charge(self):
        from main import objects
        for gameobject in objects:
            if gameobject.getID() == 'Ship':
                if gameobject.getrect().colliderect(self.energyrect):
                    gameobject.charge(1)
                    objects.remove(self)
    def update(self):
        self.charge()
        self.move()
