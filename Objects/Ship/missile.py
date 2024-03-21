import pygame
import random
import math
class Missile(pygame.sprite.Sprite):
    def __init__(self, image, position: tuple, speed, damage):
        from main import enemies
        pygame.sprite.Sprite.__init__(self)
        self.target = enemies.sprites()[random.randint(0, len(enemies.sprites()) - 1)]
        if self.target.marked == True:
            self.target = enemies.sprites()[random.randint(0, len(enemies.sprites()) - 1)]

        self.targetrect = self.target.rect
        self.target.marked = True

        self.image = image
        self.speed = speed
        self.damage = damage
        self.rect = self.image.get_rect(center=position)
        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)

        # gets the velocity so the getangle method will work
        self.velocity = pygame.math.Vector2(self.targetrect.x, self.targetrect.y) - self.position
        self.image = pygame.transform.rotate(self.image, self.getangle())


    def attack(self):
        import main
        self.hitlist = pygame.sprite.spritecollide(self, main.enemies, False)
        for enemy in self.hitlist:
            enemy.damage(self.damage)
            self.kill()

    def move(self):
        from main import enemies

        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.targetpos = pygame.math.Vector2(self.targetrect.x, self.targetrect.y)

        if self.targetrect not in [enemy.rect for enemy in enemies.sprites()]:
            self.targetrect = enemies.sprites()[random.randint(0, len(enemies.sprites()) - 1)].rect


        self.targetpos = pygame.math.Vector2(self.targetrect.x, self.targetrect.y)

        self.velocity = self.targetpos - self.position



        if self.velocity.length():
            self.velocity.normalize_ip()

        self.rect.x += (self.velocity * self.speed)[0]

        self.rect.y += (self.velocity * self.speed)[1]

    def draw(self, screen):
        from main import enemies

        if len(enemies.sprites()) != 0:


            screen.blit(self.image, self.rect)
        else:
            self.kill()

    def update(self):
        from main import enemies
        if len(enemies.sprites()) != 0:
            self.move()
            self.attack()
        else:
            self.kill()

    def getID(self):
        return "Missile"

    def getangle(self):
        # complicated maths that gets the angle of the image idk what this does i got it from stack overflow it just works
        return math.degrees(math.atan2(self.velocity.x, self.velocity.y))