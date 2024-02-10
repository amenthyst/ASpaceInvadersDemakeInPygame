from Objects.gameobject import Gameobject

class Deflectbullet(Gameobject):
    def __init__(self, deflectbullettexture, position: tuple, speed: float, damage: int):
        self.deflectbullet = deflectbullettexture
        self.position = position
        self.speed = speed
        self.damage = damage
        self.deflectbulletrect = self.deflectbullet.get_rect(center=self.position)
    def display(self, screen):
        screen.blit(self.deflectbullet, self.deflectbulletrect)
    def move(self):
        self.deflectbulletrect.y += self.speed
        if self.deflectbulletrect.y < -100:
            import main
            main.objects.remove(self)
    def getrect(self):
        return self.deflectbulletrect
    def getID(self):
        return "Deflectbullet"
    def attack(self):
        import main
        for gameobject in main.objects:
            if gameobject == self:
                continue
            if gameobject.getrect().colliderect(self.deflectbulletrect) and gameobject.getID() == 'Ship':
                gameobject.damage(self.damage)
                main.objects.remove(self)
    def update(self):
        self.move()
        self.attack()
