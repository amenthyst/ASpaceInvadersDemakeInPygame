import random


def patterns(numberofenemies, enemiesinrow):
    rows = int(numberofenemies / enemiesinrow)
    pattern = []
    # random generation of enemy types
    posy = -100
    for i in range(0,rows):
        for j in range(1,enemiesinrow+1):
            enemydata = []
            index = random.randint(1,2)

            shipchance = random.randint(1, 7)
            blankchance = random.randint(1,10)
            if blankchance == 1:
                index = None

            if shipchance == 1:
                index = 3


            enemydata.append((j*100, posy))
            enemydata.append(index)
            pattern.append(enemydata)
        posy -= 100
    return pattern


def alienobject(numberofenemies, enemiesinrow):
    import main
    from Objects.Enemies.alien import Alien
    from Objects.Enemies.deflectalien import Deflectalien
    from Objects.Enemies.enemyship import Enemyship
    pattern = patterns(numberofenemies, enemiesinrow)

    #
    for i in range(len(pattern)):
        if pattern[i][1] == 1:
            main.enemies.append(Alien(main.alientexture, tuple(pattern[i][0]), 2, 0.6, 15, 2))
        elif pattern[i][1] == 2:
            main.enemies.append(Deflectalien(main.deflectalientexture, tuple(pattern[i][0]), 1, 0.8, 15, 2))
        elif pattern[i][1] == 3:
            main.enemies.append(Enemyship(main.enemyshiptexture, tuple(pattern[i][0]), 20, 3, 4, 2))




