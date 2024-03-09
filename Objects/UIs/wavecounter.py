from Objects.Enemies import enemypatterns

class Wavecounter:
    def __init__(self, numberofwaves):
        self.numberofwaves = numberofwaves+1
        self.dt = 0
        self.currentwave = 1
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.dtcolor = 0
        self.dt = 0
        self.colorindex = 0


    def wavecounter(self):
        # counter of 1 second
        self.dt += 1
        if self.dt > 60:
            self.dt = 0
            return 1


    def checkwaves(self):
        # checking if there are no more enemies present then increments wave
        import main
        if len(main.enemies) == 0 and self.currentwave < self.numberofwaves:
            if self.wavecounter() is not None:
                enemypatterns.alienobject(int(30*self.currentwave//2.5), 5)
                self.currentwave += 1
                if self.currentwave > 2:
                    main.objects[0].addscore(20*self.currentwave/2)

    def draw(self, screen):
        import main
        # draws the wave counter
        self.textsurface = main.font.render(f"WAVE: {self.currentwave-1}", False, "white")
        self.textrect = self.textsurface.get_rect(center=(83,70))
        screen.blit(self.textsurface, self.textrect)
        if self.currentwave == self.numberofwaves:
            screen.blit(self.goaltext, (23,80))


    def update(self):
        self.changecolor()
        self.checkwaves()


    def getrect(self):
        return self.textrect


    def getID(self):
        return "Wavecounter"

    def cooldown(self):
        # buffer for 1/6th seconds
        self.dtcolor += 1
        if self.dtcolor == 10:
            self.dtcolor = 0
            return 0

    def changecolor(self):
        from main import font
        # flashes the text with rainbow colors
        self.goaltext = font.render("FINAL WAVE!", False, self.colors[self.colorindex])
        if self.cooldown() is not None:
            self.colorindex += 1
        if self.colorindex >= len(self.colors):
            self.colorindex = 0







