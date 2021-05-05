import pygame
import configparser
import sys

ini_file = sys.argv[1]

config = configparser.ConfigParser()
config.read(ini_file)

backgroundcolor = config["generic"]["background-color"]
fontcolor = config["generic"]["font-color"]
fontfamily = config["generic"]["font-family"]
fontsize = int(config["generic"]["font-size"])
title = config["generic"]["title"]
footerimage = config["generic"]["footer-image"]
topimage = config["generic"]["top-image"]

ploegnaam_Thuis = config["teamA"]["naam"]
ploegnaam_Uit = config["teamB"]["naam"]

WIDTH = 800
HEIGHT = 600

thuis = 0
thuisset = 0
uit = 0
uitset = 0
vijfsetter = False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(fontfamily, fontsize)

# Start de klok
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                running = False
            elif event.key == pygame.K_LEFT:
                thuis += 1
                if thuisset == 2 and uitset == 2:
                    if thuis >= 15:
                        if uit < thuis - 1:
                            thuis = 0
                            uit = 0
                            thuisset += 1
                else:
                    if thuis >= 25:
                        if uit < thuis - 1:
                            thuis = 0
                            uit = 0
                            thuisset += 1
            elif event.key == pygame.K_RIGHT:
                uit += 1
                if thuisset == 2 and uitset == 2:
                    if uit >= 15:
                        if thuis < uit - 1:
                            thuis = 0
                            uit = 0
                            uitset += 1
                else:
                    if uit >= 25:
                        if thuis < uit - 1:
                            thuis = 0
                            uit = 0
                            uitset += 1
            elif event.key == pygame.K_UP:
                thuis -= 1
            elif event.key == pygame.K_DOWN:
                uit -= 1
            elif event.key == pygame.K_r:
                thuis = 0
                thuisset = 0
                uit = 0
                uitset = 0
            elif event.key == pygame.K_s:
                print(text.get_width())
                print(text.get_height())

    if vijfsetter == False:
        if thuisset == 4 and uitset == 0:
            print("Thuisploeg heeft gewonne")
            running = False

    if vijfsetter == False:    
        if thuisset == 3 and uitset == 1:
            print("Thuisploeg heeft gewonne")
            running = False

    if vijfsetter == False:
        if thuisset == 2 and uitset == 2:
            vijfsetter = True

    if vijfsetter == False:
        if uitset == 4 and thuisset == 0:
            print("Uitploeg heeft gewonne")
            running = False

    if vijfsetter == False:
        if uitset == 3 and thuisset == 1:
            print("Uitploeg heeft gewonne")
            running = False

    if vijfsetter == True:
        if thuisset == 3 and uitset == 2:
            print("Thuisploeg is gewonne")
            vijfsetter = False
            running = False
        if uitset == 3 and thuisset == 2:
            print("Uitploeg is gewonne")
            vijfsetter = False
            running = False

    screen.fill(backgroundcolor)

    text = font.render(f"{ploegnaam_Thuis}   {thuis} ({thuisset}) - ({uitset}) {uit}    {ploegnaam_Uit}", True, fontcolor)
    screen.blit(text, (WIDTH / 2 - (text.get_width() / 2), HEIGHT / 2 - (text.get_height() / 2)))

    pygame.display.flip()

    # Wacht zodanig dat we maximal 60 FPS halen
    clock.tick(60)