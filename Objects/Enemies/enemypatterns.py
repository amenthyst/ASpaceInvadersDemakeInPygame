import random
numberofenemies = 30
enemiesinrow = 5
rows = int(numberofenemies/enemiesinrow)
def patterns():
    pattern = []
    # random generation of enemy types
    posy = -100
    for i in range(0,rows):
        for j in range(1,enemiesinrow+1):
            enemydata = []
            index = random.randint(1,2)
            enemydata.append((j*100, posy))
            enemydata.append(index)
            pattern.append(enemydata)
        posy -= 100
    return pattern
# note: use linear search to search for remaining enemy objects in main.objects, if not then move on to the next wave

def alienobject():
    import main
    from Objects.Enemies.alien import Alien
    from Objects.Enemies.deflectalien import Deflectalien
    pattern = patterns()
    for i in range(len(pattern)):
        if pattern[i][1] == 1:
            main.objects.append(Alien(main.alientexture, tuple(pattern[i][0]), 2, 0.8, 15))
        elif pattern[i][1] == 2:
            main.objects.append(Deflectalien(main.deflectalientexture, tuple(pattern[i][0]), 1, 1.2, 15))


