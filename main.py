import pygame
from sys import exit
from Initializescripts import initialize
from Objects.Ship.ship import ShipObject
from Objects.UIs.healthbar import HealthBar
from Objects.UIs.energybar import Energybar
from Objects.UIs.dangerzone import Dangerzone
from Objects.UIs.scoreboard import Scoreboard
from Objects.Enemies.boss import Boss
from Initializescripts import soundeffects
from Objects.UIs.wavecounter import Wavecounter
from Objects.Enemies.deflectalien import Deflectalien
from Objects.Enemies.alien import Alien
from Objects.Enemies.enemyship import Enemyship
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((600,600))
border = pygame.Rect(0, 0, 600, 580)
pygame.display.set_caption("Programming Project")
clock = pygame.time.Clock()

background = initialize.renderbackground()

spaceshiphigh, spaceshipmid, spaceshiplow, spaceshiplaserlow, spaceshiplaserhigh, bullet, deflectbullettexture, dangerzone, superbullettexture, lasertexture, explosion, missiletexture = initialize.rendergraphics()

alientexture, alienhealthtexture, alienfasttexture, aliendamagetexture, deflectalientexture, deflectalienhealthtexture, deflectalienfasttexture, deflectaliendamagetexture, enemyshiptexture, bosstexture = initialize.renderenemies()

hearttexture, energytexture = initialize.renderpowerups()

highscore, bestwave, unlocksuperbullet, unlocklaser, unlockmissile = initialize.getstats()

shootsfx, superbulletsfx, lasersfx, boomsfx, chargesfx, damagesfx, healsfx = soundeffects.sfx()

font = pygame.font.Font('Graphics/joystix monospace.otf', 20)

ship = pygame.sprite.GroupSingle(ShipObject(spaceshiphigh, spaceshipmid, spaceshiplow, (300,550), 10, 100, 100,0, 0.2))
shipobj = ship.sprites()[0]

savelist = [highscore, bestwave, unlocksuperbullet, unlocklaser, unlockmissile]


uigroup = pygame.sprite.Group(HealthBar(100, hearttexture),
           Dangerzone(dangerzone, (0,580)),
           Energybar(5,energytexture),
           Scoreboard(),
           Wavecounter(8))

enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
#Boss(bosstexture, (300,200), 100,3.0, 100, 1))
powerups = pygame.sprite.Group()

explosions = pygame.sprite.Group()
run = True






while run:



    # updates every object in the list objects
    ship.update()
    if len(ship.sprites()) != 0:
        uigroup.update()
    enemies.update()
    bullets.update()
    powerups.update()
    explosions.update()

    screen.blit(background, (0,0))


    # displays every object in the list objects

    for object in ship.sprites():
        object.draw(screen)

    for object in uigroup.sprites():
        object.draw(screen)

    for object in enemies.sprites():
        object.draw(screen)

    for object in bullets.sprites():
        object.draw(screen)

    for object in powerups.sprites():
        object.draw(screen)

    for object in explosions.sprites():
        object.draw(screen)


    # updates display
    pygame.display.update()
    # updates clock
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()


initialize.savefile(savelist)

exit()
