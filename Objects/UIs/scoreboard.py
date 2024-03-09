from Objects.gameobject import Gameobject

class Scoreboard(Gameobject):


    def draw(self, screen):
        from main import objects, font

        self.score = objects[0].getscore()
        if self.score is not None:
            self.previousscore = self.score

        self.textsurface = font.render(f"SCORE:{self.previousscore}", False, "white")


        self.scorerect = self.textsurface.get_rect(center=(90,25))
        screen.blit(self.textsurface, self.scorerect)

    def update(self):
        pass

    def getrect(self):
        return self.scorerect
    def getID(self):
        return "Scoreboard"