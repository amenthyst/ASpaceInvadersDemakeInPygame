import pygame

def renderbackground():
    background = pygame.image.load("Graphics/background.jpeg").convert_alpha()
    background = pygame.transform.scale(background, (600,600))
    return background

def rendergraphics():
    spaceshiphigh = pygame.image.load("Graphics/spaceships/spaceshiphigh.png").convert_alpha()
    spaceshiphigh = pygame.transform.scale(spaceshiphigh, (80,80))
    spaceshipmid = pygame.image.load("Graphics/spaceships/spaceshipmid.png").convert_alpha()
    spaceshipmid = pygame.transform.scale(spaceshipmid, (80, 80))
    spaceshiplow = pygame.image.load("Graphics/spaceships/spaceshiplow.png").convert_alpha()
    spaceshiplow = pygame.transform.scale(spaceshiplow, (80, 80))
    spaceshiplaserlow = pygame.image.load("Graphics/spaceships/spaceshiplaserlow.png").convert_alpha()
    spaceshiplaserlow = pygame.transform.scale(spaceshiplaserlow,(80,80))
    spaceshiplaserhigh = pygame.image.load("Graphics/spaceships/spaceshiplaserhigh.png").convert_alpha()
    spaceshiplaserhigh = pygame.transform.scale(spaceshiplaserhigh, (80,80))
    bullet = pygame.image.load("Graphics/bullets/bullet.png").convert_alpha()
    bullet = pygame.transform.scale(bullet,(15,15))
    deflectbullettexture = pygame.image.load("Graphics/bullets/deflectedbullet.png").convert_alpha()
    deflectedbullettexture = pygame.transform.scale(deflectbullettexture, (40,80))
    dangerzone = pygame.image.load("Graphics/dangerzone.png").convert_alpha()
    dangerzone = pygame.transform.scale(dangerzone, (600,20))
    superbullettexture = pygame.image.load("Graphics/bullets/superbullet.png").convert_alpha()
    superbullettexture = pygame.transform.scale(superbullettexture, (30,120))
    lasertexture = pygame.image.load("Graphics/bullets/laser.png").convert_alpha()
    lasertexture = pygame.transform.scale(lasertexture, (30,60))
    explosion = pygame.image.load("Graphics/explosion.png").convert_alpha()
    explosion = pygame.transform.scale(explosion, (60,60))
    missiletexture = pygame.image.load("Graphics/bullets/missile.png").convert_alpha()
    missiletexture = pygame.transform.scale(missiletexture, (20,50))
    return spaceshiphigh, spaceshipmid, spaceshiplow, spaceshiplaserlow, spaceshiplaserhigh, bullet, deflectedbullettexture, dangerzone, superbullettexture, lasertexture, explosion, missiletexture
def renderenemies():
    alientexture = pygame.image.load("Graphics/enemies/alien.png").convert_alpha()
    alientexture = pygame.transform.scale(alientexture, (40,40))

    alienhealthtexture = pygame.image.load("Graphics/enemies/alienhealth.png").convert_alpha()
    alienhealthtexture = pygame.transform.scale(alienhealthtexture, (50, 50))

    alienfasttexture = pygame.image.load("Graphics/enemies/alienfast.png").convert_alpha()
    alienfasttexture = pygame.transform.scale(alienfasttexture, (40, 40))

    aliendamagetexture = pygame.image.load("Graphics/enemies/aliendamage.png").convert_alpha()
    aliendamagetexture = pygame.transform.scale(aliendamagetexture, (40,40))

    deflectalienhealthtexture = pygame.image.load("Graphics/enemies/deflectalienhealth.png").convert_alpha()
    deflectalienhealthtexture = pygame.transform.scale(deflectalienhealthtexture, (50,50))

    deflectalienfasttexture = pygame.image.load("Graphics/enemies/deflectalienfast.png").convert_alpha()
    deflectalienfasttexture = pygame.transform.scale(deflectalienfasttexture, (40, 40))

    deflectaliendamagetexture = pygame.image.load("Graphics/enemies/deflectaliendamage.png").convert_alpha()
    deflectaliendamagetexture = pygame.transform.scale(deflectaliendamagetexture, (50,50))

    deflectalientexture = pygame.image.load("Graphics/enemies/deflectalien.png").convert_alpha()
    deflectalientexture = pygame.transform.scale(deflectalientexture, (50,50))

    enemyshiptexture = pygame.image.load("Graphics/enemies/enemyship.png").convert_alpha()
    enemyshiptexture = pygame.transform.scale(enemyshiptexture, (50,50))

    bosstexture = pygame.image.load("Graphics/enemies/boss.png").convert_alpha()
    bosstexture = pygame.transform.scale(bosstexture, (60,60))


    return alientexture, alienhealthtexture, alienfasttexture, aliendamagetexture, deflectalientexture, deflectalienhealthtexture, deflectalienfasttexture, deflectaliendamagetexture, enemyshiptexture, bosstexture
def renderpowerups():
    hearttexture = pygame.image.load("Graphics/powerups/heart.png").convert_alpha()
    hearttexture = pygame.transform.scale(hearttexture,(30,30))
    energytexture = pygame.image.load("Graphics/powerups/energy.png").convert_alpha()
    energytexture = pygame.transform.scale(energytexture, (30,30))
    return hearttexture, energytexture

def getstats():
    with open('highscore.txt', 'r') as f:
        highscore = int(f.readline()[11:])
        bestwave = int(f.readline()[11:])
        unlocksuperbullet = bool(f.readline()[19:])
        unlocklaser = bool(f.readline()[13:])
        unlockmissile = bool(f.readline()[15:])
    return highscore, bestwave, unlocksuperbullet, unlocklaser, unlockmissile

def savefile(savelist):
    import main



    score = main.uigroup.sprites()[3].score
    wave = main.uigroup.sprites()[4].currentwave-1

    updatelist = [score, wave]
    prefixlist = ['Highscore: ', 'Best Wave: ', 'UnlockSuperbullet: ', 'UnlockLaser: ', 'UnlockMissile: ']


    with open('highscore.txt', 'r') as f:
        lines = f.readlines()

    for index, item in enumerate(savelist):
        try:
            if updatelist[index] >= item:
                lines[index] = prefixlist[index] + str(updatelist[index]) + "\n"
        except IndexError:
            continue

    with open('highscore.txt', 'w') as f:
        f.writelines(lines)


