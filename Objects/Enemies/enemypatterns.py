import random
from enum import Enum

class Enemies(Enum):
    ALIEN = [1, 2, 3, 4]
    DEFLECTALIEN = [5, 6, 7, 8]
    ENEMYSHIP = [9]
    BLANK = [10]

def patterns(numberofenemies, enemiesinrow):
    global modifierchancedict
    from main import uigroup
    currentwave = uigroup.sprites()[4].currentwave

    modifierchancedict = {"ALIENSPEED": [x for x in range(1,currentwave)],

    "ALIENHEALTH" : [x for x in range(currentwave,currentwave*2)],

    "ALIENDAMAGE" : [x for x in range(currentwave*2,currentwave*3)],

    "DEFLECTALIENSPEED" : [x for x in range(currentwave*3,currentwave*4)],

    "DEFLECTALIENHEALTH" : [x for x in range(currentwave*4,currentwave*5)],

    "DEFLECTALIENDAMAGE" : [x for x in range(currentwave*5,currentwave*6)]}


    rows = int(numberofenemies / enemiesinrow)

    pattern = []

    # random generation of enemy types
    posy = -100
    for i in range(0,rows):
        for j in range(1,enemiesinrow+1):
            enemydata = []
            index = random.randint(1,10)
            modifierindex = random.randint(1, 120)
            enemydata.append((j*100, posy))

            for enemy in Enemies:
                if index in enemy.value:
                    enemydata.append(str(enemy))

            for enemy in modifierchancedict:
                if modifierindex in modifierchancedict[enemy]:
                    enemydata[1] = str(enemy)

            pattern.append(enemydata)

        posy -= 100
    return pattern


def alienobject(numberofenemies, enemiesinrow):
    import main
    from Objects.Enemies.alien import Alien
    from Objects.Enemies.deflectalien import Deflectalien
    from Objects.Enemies.enemyship import Enemyship
    pattern = patterns(numberofenemies, enemiesinrow)
    for i in range(len(pattern)):
        enemydict = {"Enemies.ALIEN": Alien(main.alientexture, tuple(pattern[i][0]), 1, 1, 15, 2),

                     "Enemies.DEFLECTALIEN": Deflectalien(main.deflectalientexture, tuple(pattern[i][0]), 1, 1, 15,2, 25),

                     "Enemies.ENEMYSHIP": Enemyship(main.enemyshiptexture, tuple(pattern[i][0]), 20, 3, 3, 2)}


        modifierdict = {"ALIENSPEED": Alien(main.alienfasttexture, tuple(pattern[i][0]), 1, 2.5, 15, 2),

                     "ALIENHEALTH": Alien(main.alienhealthtexture, tuple(pattern[i][0]), 3, 1, 15, 2),

                    "ALIENDAMAGE": Alien(main.aliendamagetexture, tuple(pattern[i][0]), 1, 1, 25, 2),

                     "DEFLECTALIENSPEED": Deflectalien(main.deflectalienfasttexture, tuple(pattern[i][0]), 1, 2.5, 15, 2, 25),

                     "DEFLECTALIENHEALTH": Deflectalien(main.deflectalienhealthtexture, tuple(pattern[i][0]), 2, 1, 15, 2, 25),

                    "DEFLECTALIENDAMAGE": Deflectalien(main.deflectaliendamagetexture, tuple(pattern[i][0]), 1, 1, 25, 2, 40)
                     }



        if pattern[i][1] == "Enemies.BLANK":
            continue
        if pattern[i][1] in [str(enemy) for enemy in Enemies]:
            main.enemies.add(enemydict[pattern[i][1]])
        elif pattern[i][1] in [str(modifier) for modifier in modifierchancedict]:
            main.enemies.add(modifierdict[pattern[i][1]])


