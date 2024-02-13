import pygame
from sys import exit
from Otherscripts import textandimages
from Objects.Ship.ship import ShipObject
from Objects.Enemies.enemypatterns import alienobject
from Objects.Enemies.enemyship import Enemyship
from Objects.UIs.healthbar import HealthBar
from Objects.UIs.energybar import Energybar
from Objects.UIs.dangerzone import Dangerzone
from Otherscripts import soundeffects
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Programming Project")
clock = pygame.time.Clock()

background = textandimages.renderbackground()
spaceshiphigh, spaceshipmid, spaceshiplow, spaceshiplaserlow, spaceshiplaserhigh, bullet, deflectbullettexture, dangerzone, superbullettexture, lasertexture, explosion = textandimages.rendergraphics()
alientexture, deflectalientexture, enemyshiptexture = textandimages.renderenemies()
hearttexture, energytexture = textandimages.renderpowerups()
shootsfx, superbulletsfx, lasersfx, boomsfx, chargesfx, damagesfx, healsfx = soundeffects.sfx()

font = pygame.font.Font('Graphics/ARCADECLASSIC.TTF', 25)

objects = [ShipObject(spaceshiphigh, spaceshipmid, spaceshiplow, (300,550), 8, 100, 100,0, 0.4), HealthBar(100, hearttexture), Dangerzone(dangerzone, (0,580)), Energybar(5,energytexture)]
alienobject()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for gameobject in objects:
        gameobject.update()
    screen.blit(background, (0,0))
    for gameobject in objects:
        gameobject.display(screen)



    pygame.display.update()
    clock.tick(60)