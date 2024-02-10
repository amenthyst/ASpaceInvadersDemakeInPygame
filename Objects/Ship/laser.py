from Objects.gameobject import Gameobject
from Otherscripts.damagable import damagable
class Laser(Gameobject):

        def __init__(self, lasertexture, position: tuple, speed: float, damage: float):
            self.lasertexture = lasertexture
            self.position = position
            self.speed = speed
            self.damage = damage
            self.laserrect = self.lasertexture.get_rect(midright=self.position)

        def display(self, screen):
            screen.blit(self.lasertexture, self.laserrect)

        def move(self):
            import main
            self.laserrect.y -= self.speed
            if self.laserrect.y < -100:
                main.objects.remove(self)

        def getrect(self):
            return self.laserrect

        def getID(self):
            return "Laser"

        def attack(self):
            import main
            for gameobject in main.objects:
                if gameobject == self or gameobject == main.objects[0]:
                    continue
                if gameobject.getrect().colliderect(self.laserrect):
                    if isinstance(gameobject, damagable):
                        gameobject.damage(self.damage)
                        try:
                            main.objects.remove(self)
                        except ValueError:
                            continue

        def update(self):
            self.move()
            self.attack()