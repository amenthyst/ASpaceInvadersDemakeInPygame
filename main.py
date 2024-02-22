import pygame
from sys import exit
from Otherscripts import textandimages
from Objects.Ship.ship import ShipObject
from Objects.Enemies import enemypatterns
from Objects.Enemies.enemyship import Enemyship
from Objects.UIs.healthbar import HealthBar
from Objects.UIs.energybar import Energybar
from Objects.UIs.dangerzone import Dangerzone
from Objects.UIs.scoreboard import Scoreboard
from Otherscripts import soundeffects
from Objects.wavecounter import Wavecounter

pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Programming Project")
clock = pygame.time.Clock()

background = textandimages.renderbackground()
spaceshiphigh, spaceshipmid, spaceshiplow, spaceshiplaserlow, spaceshiplaserhigh, bullet, deflectbullettexture, dangerzone, superbullettexture, lasertexture, explosion = textandimages.rendergraphics()
alientexture, deflectalientexture, enemyshiptexture = textandimages.renderenemies()
hearttexture, energytexture = textandimages.renderpowerups()
shootsfx, superbulletsfx, lasersfx, boomsfx, chargesfx, damagesfx, healsfx = soundeffects.sfx()

font = pygame.font.Font('Graphics/joystix monospace.otf', 20)

objects = [ShipObject(spaceshiphigh, spaceshipmid, spaceshiplow, (300,550), 8, 100, 100,0, 0.2),
           HealthBar(100, hearttexture),
           Dangerzone(dangerzone, (0,580)),
           Energybar(5,energytexture),
           Scoreboard(),
           Wavecounter(5)]
enemies = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    # updates every object in the list objects
    for gameobject in objects:
        gameobject.update()


    # updates every object in the list enemies
    for enemy in enemies:
        enemy.update()


    screen.blit(background, (0,0))


    # displays every object in the list objects
    for gameobject in objects:
        gameobject.display(screen)


    # displays every enemy in the list enemies
    for enemy in enemies:
        enemy.display(screen)



    # updates display
    pygame.display.update()
    # updates clock
    clock.tick(60)