import pygame
from sys import exit
from Otherscripts import textandimages
from Objects.Ship.ship import ShipObject
from Objects.UIs.healthbar import HealthBar
from Objects.UIs.energybar import Energybar
from Objects.UIs.dangerzone import Dangerzone
from Objects.UIs.scoreboard import Scoreboard
from Objects.Enemies.boss import Boss
from Otherscripts import soundeffects
from Objects.UIs.wavecounter import Wavecounter

pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((600,600))
border = pygame.Rect(0, 0, 600, 580)
pygame.display.set_caption("Programming Project")
clock = pygame.time.Clock()

background = textandimages.renderbackground()
spaceshiphigh, spaceshipmid, spaceshiplow, spaceshiplaserlow, spaceshiplaserhigh, bullet, deflectbullettexture, dangerzone, superbullettexture, lasertexture, explosion = textandimages.rendergraphics()
alientexture, deflectalientexture, enemyshiptexture, bosstexture = textandimages.renderenemies()
hearttexture, energytexture = textandimages.renderpowerups()
shootsfx, superbulletsfx, lasersfx, boomsfx, chargesfx, damagesfx, healsfx = soundeffects.sfx()

font = pygame.font.Font('Graphics/joystix monospace.otf', 20)

objects = [ShipObject(spaceshiphigh, spaceshipmid, spaceshiplow, (300,550), 8, 10, 100,0, 0.2),
           HealthBar(100, hearttexture),
           Dangerzone(dangerzone, (0,580)),
           Energybar(5,energytexture),
           Scoreboard(),
           Wavecounter(0)]

ship = pygame.sprite.GroupSingle(ShipObject(spaceshiphigh, spaceshipmid, spaceshiplow, (300,550), 8, 100, 100,0, 0.2))
shipobj = ship.sprites()[0]

uigroup = pygame.sprite.Group(HealthBar(100, hearttexture),
           Dangerzone(dangerzone, (0,580)),
           Energybar(5,energytexture),
           Scoreboard(),
           Wavecounter(5))

enemies = pygame.sprite.Group()
#Boss(bosstexture, (300,200), 4,3.0, 100, 1)
bullets = pygame.sprite.Group()

powerups = pygame.sprite.Group()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    # updates every object in the list objects
    ship.update()
    uigroup.update()
    enemies.update()
    bullets.update()
    powerups.update()


    screen.blit(background, (0,0))


    # displays every object in the list objects

    for object in ship.sprites():
        object.draw(screen)
    for object in uigroup.sprites():
        object.draw(screen)
    for object in enemies.sprites():
        object.draw(screen)
    for object in bullets.sprites():
        bullets.draw(screen)
    for object in powerups.sprites():
        powerups.draw(screen)



    # updates display
    pygame.display.update()
    # updates clock
    clock.tick(60)