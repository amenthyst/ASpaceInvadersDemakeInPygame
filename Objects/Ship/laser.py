from Objects.gameobject import Gameobject
from Otherscripts.damagable import damagable
class Laser(Gameobject):

        def __init__(self, lasertexture, position: tuple, speed: float, damage: float, direction):
            self.lasertexture = lasertexture
            self.position = position
            self.speed = speed
            self.damage = damage
            self.direction = direction
            self.laserrect = self.lasertexture.get_rect(midright=self.position)

        def draw(self, screen):
            screen.blit(self.lasertexture, self.laserrect)

        def move(self):
            import main
            if self.direction == 'up':
                self.laserrect.y -= self.speed
                if self.laserrect.y < -100:
                    main.objects.remove(self)
            elif self.direction == 'left':
                self.laserrect.x -= self.speed
                if self.laserrect.x < -100:
                    main.objects.remove(self)
            elif self.direction == 'right':
                self.laserrect.x += self.speed
                if self.laserrect.x > 600:
                    main.objects.remove(self)
            elif self.direction == 'down':
                self.laserrect.y += self.speed
                if self.laserrect.y > 650:
                    main.objects.remove(self)

        def getrect(self):
            return self.laserrect

        def getID(self):
            return "Laser"

        def attack(self):
            import main
            for enemy in main.enemies:
                if enemy.getrect().colliderect(self.laserrect):
                    if isinstance(enemy, damagable):
                        enemy.damage(self.damage)
                        try:
                            main.objects.remove(self)
                        except ValueError:
                            continue

        def update(self):
            self.move()
            self.attack()