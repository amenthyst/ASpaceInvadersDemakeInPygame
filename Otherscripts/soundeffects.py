import pygame
pygame.mixer.init()
def sfx():
    shootsfx = pygame.mixer.Sound("SFXandmusic/shootsfx.wav")
    superbulletsfx = pygame.mixer.Sound("SFXandmusic/superbulletsfx.wav")
    lasersfx = pygame.mixer.Sound("SFXandmusic/lasersfx.mp3")
    boomsfx = pygame.mixer.Sound("SFXandmusic/boom.mp3")
    chargesfx = pygame.mixer.Sound("SFXandmusic/charge.mp3")
    damagesfx = pygame.mixer.Sound("SFXandmusic/damage.mp3")
    healsfx = pygame.mixer.Sound("SFXandmusic/heal.mp3")
    return shootsfx, superbulletsfx, lasersfx, boomsfx, chargesfx, damagesfx, healsfx