
import pygame
class Scoreboard(pygame.sprite.Sprite):

    def __init__(self):
        from main import font
        pygame.sprite.Sprite.__init__(self)
        self.previousscore = 0
        self.image = font.render(f"SCORE:{self.previousscore}", False, "white")
        self.rect = self.image.get_rect(center=(90, 25))
    def draw(self, screen):
        import main

        self.score = main.shipobj.getscore()
        if self.score is not None:
            self.previousscore = self.score
        self.image = main.font.render(f"SCORE:{self.previousscore}", False, "white")

        screen.blit(self.image, self.rect)


    def getrect(self):
        return self.rect
    def getID(self):
        return "Scoreboard"