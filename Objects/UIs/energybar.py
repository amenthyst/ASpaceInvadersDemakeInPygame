
import pygame
class Energybar(pygame.sprite.Sprite):
    def __init__(self, maxenergy: int, energytexture):
        pygame.sprite.Sprite.__init__(self)
        self.image = energytexture
        self.energynew = pygame.transform.scale(self.image, (45,45))
        self.maxenergy = maxenergy
        self.rect = self.energynew.get_rect(center=(425,555))
    def draw(self, screen):

        import main
        self.currentenergy = main.shipobj.energyvalue


        ratio = self.currentenergy / self.maxenergy

        self.energytext = str(self.currentenergy)
        self.textsurface = main.font.render(self.energytext, False, "black")

        pygame.draw.rect(screen, "black", (425,545,125,25),4)
        if len(main.ship.sprites()) != 0:
            pygame.draw.rect(screen,"yellow",(430,549,117*ratio,17))
        else:
            self.currentenergy = 0

        screen.blit(self.textsurface, (450,545))
        screen.blit(self.energynew, self.rect)


    def update(self):
        pass
    def getrect(self):
        return self.rect
    def getID(self):
        return "Energybar"
    def damage(self,damage):
        pass