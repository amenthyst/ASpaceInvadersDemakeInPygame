
import pygame
class Scoreboard(pygame.sprite.Sprite):

    def __init__(self):
        from main import font
        pygame.sprite.Sprite.__init__(self)
        self.previousscore = 0
        self.image = font.render(f"SCORE:{self.previousscore}", False, "white")
        self.rect = self.image.get_rect(center=(70, 15))
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.dt = 0
        self.dtcolor = 0
        self.colorindex = 0
    def draw(self, screen):
        import main

        self.score = main.shipobj.getscore()
        if self.score is not None:
            self.previousscore = self.score
        self.image = main.font.render(f"SCORE:{self.previousscore}", False, "white")

        if main.highscore <= self.score:
            screen.blit(self.scoretext, (445,0))
        screen.blit(self.image, self.rect)


    def getrect(self):
        return self.rect
    def getID(self):
        return "Scoreboard"

    def cooldown(self):
        # buffer for 1/6th seconds
        self.dtcolor += 1
        if self.dtcolor == 10:
            self.dtcolor = 0
            return 0
    def changecolor(self):
        from main import font
        # flashes the text with rainbow colors
        self.scoretext = font.render("HI-SCORE!", False, self.colors[self.colorindex])
        if self.cooldown() is not None:
            self.colorindex += 1
        if self.colorindex >= len(self.colors):
            self.colorindex = 0

    def update(self):
        self.changecolor()