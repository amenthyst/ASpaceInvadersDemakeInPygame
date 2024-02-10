from Otherscripts import damagable


from Objects.gameobject import Gameobject
class Bullet(Gameobject):

    def __init__(self, bullet, position: tuple, speed: float, damage: int):
        self.bullet = bullet
        self.position = position
        self.speed = speed
        self.damage = damage
        self.bulletrect = self.bullet.get_rect(midright=self.position)
    def display(self, screen):
        screen.blit(self.bullet, self.bulletrect)
    def move(self):
        import main
        self.bulletrect.y -= self.speed
        if self.bulletrect.y < -100:
            main.objects.remove(self)
    def getrect(self):
        return self.bulletrect
    def getID(self):
        return "Bullet"

    def attack(self):
        import main
        for gameobject in main.objects:
            if gameobject == self or gameobject == main.objects[0]:
                continue
            if gameobject.getrect().colliderect(self.bulletrect):
                if isinstance(gameobject, damagable.damagable):
                    gameobject.damage(self.damage)
                    try:
                        main.objects.remove(self)
                    except ValueError:
                        continue
    def update(self):
        self.move()
        self.attack()


