from Objects.gameobject import Gameobject
import pygame


class HealthBar(Gameobject, pygame.sprite.Sprite):
    def __init__(self, max_health: int, hearttexture):
        pygame.sprite.Sprite.__init__(self)
        self.max_health = max_health
        self.hearttexture = hearttexture
        self.hearttexturenew = pygame.transform.scale(self.hearttexture,(35,35))
        self.heartrect = self.hearttexturenew.get_rect(center=(45,560))
    def draw(self, screen):
        import main
        for gameobject in main.objects:
            if gameobject.getID() == 'Ship':
                self.currenthealth = gameobject.gethealth()
                self.hard_health = gameobject.getmaxhealth()



        if self.currenthealth > 70:
            self.color = "green"
        elif self.currenthealth <= 69 and self.currenthealth > 30:
            self.color = "yellow"
        elif self.currenthealth <= 30:
            self.color = "red"



        ratio = self.currenthealth / self.max_health

        self.healthtext = str(self.currenthealth)
        self.textsurface = main.font.render(self.healthtext, False, "black")



        # draws remaining health
        pygame.draw.rect(screen, "black", (50,550,125*self.hard_health/100+3,25),4)
        if main.objects[0].getID() == 'Ship':
            pygame.draw.rect(screen,self.color,(55,554,117*ratio,17))
        else:
            self.currenthealth = 0
        screen.blit(self.textsurface, (70,549))
        screen.blit(self.hearttexturenew, self.heartrect)


    def update(self):
        pass
    def getrect(self):
        return self.heartrect
    def getID(self):
        return "Healthbar"
    def addscore(self, score):
        pass
    def getscore(self):
        pass

    def getposition(self):
        pass