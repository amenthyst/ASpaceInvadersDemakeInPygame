
import pygame


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, max_health: int, hearttexture):
        pygame.sprite.Sprite.__init__(self)
        self.max_health = max_health
        self.image = hearttexture
        self.hearttexturenew = pygame.transform.scale(self.image,(35,35))
        self.rect = self.hearttexturenew.get_rect(center=(45,560))
    def draw(self, screen):
        import main
        self.currenthealth = main.shipobj.health
        self.hard_health = main.shipobj.maxhealth



        if self.currenthealth > 70:
            self.color = "green"
        elif self.currenthealth <= 69 and self.currenthealth > 30:
            self.color = "yellow"
        elif self.currenthealth <= 30:
            self.color = "red"



        ratio = self.currenthealth / self.max_health

        if self.currenthealth < 0:
            self.currenthealth = 0

        self.healthtext = str(self.currenthealth)
        self.textsurface = main.font.render(self.healthtext, False, "black")


        # draws remaining health
        pygame.draw.rect(screen, "black", (50,550,125*self.hard_health/100+3,25),4)
        if len(main.ship.sprites()) != 0:
            pygame.draw.rect(screen,self.color,(55,554,117*ratio,17))
        else:
            self.currenthealth = 0



        screen.blit(self.textsurface, (70,549))
        screen.blit(self.hearttexturenew, self.rect)



    def update(self):
        pass
    def getrect(self):
        return self.rect
    def getID(self):
        return "Healthbar"
