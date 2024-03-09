from Objects.gameobject import Gameobject
import pygame
class Energybar(Gameobject):
    def __init__(self, maxenergy: int, energytexture):
        self.energytexture = energytexture
        self.energynew = pygame.transform.scale(energytexture, (45,45))
        self.maxenergy = maxenergy
        self.energyrect = self.energynew.get_rect(center=(425,555))
    def draw(self, screen):

        import main
        for gameobject in main.objects:
            if gameobject.getID() == 'Ship':
                self.currentenergy = gameobject.getcharge()


        ratio = self.currentenergy / self.maxenergy

        self.energytext = str(self.currentenergy)
        self.textsurface = main.font.render(self.energytext, False, "black")

        pygame.draw.rect(screen, "black", (425,545,125,25),4)
        if main.objects[0].getID() == 'Ship':
            pygame.draw.rect(screen,"yellow",(430,549,117*ratio,17))
        else:
            self.currentenergy = 0

        screen.blit(self.textsurface, (450,545))
        screen.blit(self.energynew, self.energyrect)


    def update(self):
        pass
    def getrect(self):
        return self.energyrect
    def getID(self):
        return "Energybar"
    def damage(self,damage):
        pass