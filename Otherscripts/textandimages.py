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
    bullet = pygame.image.load("Graphics/bullets/bullet.png").convert_alpha()
    bullet = pygame.transform.scale(bullet,(15,15))
    deflectbullettexture = pygame.image.load("Graphics/bullets/deflectedbullet.png").convert_alpha()
    deflectedbullettexture = pygame.transform.scale(deflectbullettexture, (40,80))
    dangerzone = pygame.image.load("Graphics/dangerzone.png").convert_alpha()
    dangerzone = pygame.transform.scale(dangerzone, (600,20))
    superbullettexture = pygame.image.load("Graphics/bullets/superbullet.png").convert_alpha()
    superbullettexture = pygame.transform.scale(superbullettexture, (30,120))
    lasertexture = pygame.image.load("Graphics/bullets/laser.png").convert_alpha()
    lasertexture = pygame.transform.scale(lasertexture, (30,20))
    return spaceshiphigh, spaceshipmid, spaceshiplow, bullet, deflectedbullettexture, dangerzone, superbullettexture, lasertexture
def renderenemies():
    alientexture = pygame.image.load("Graphics/enemies/alien.png").convert_alpha()
    alientexture = pygame.transform.scale(alientexture, (40,40))
    deflectalientexture = pygame.image.load("Graphics/enemies/deflectalien.png").convert_alpha()
    deflectalientexture = pygame.transform.scale(deflectalientexture, (50,50))
    return alientexture, deflectalientexture
def renderpowerups():
    hearttexture = pygame.image.load("Graphics/powerups/heart.png").convert_alpha()
    hearttexture = pygame.transform.scale(hearttexture,(30,30))
    energytexture = pygame.image.load("Graphics/powerups/energy.png").convert_alpha()
    energytexture = pygame.transform.scale(energytexture, (30,30))
    return hearttexture, energytexture