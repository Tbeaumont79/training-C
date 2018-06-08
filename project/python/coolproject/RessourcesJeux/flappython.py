import pygame
import time
from random import *
blue = (113,117,227)
white = (255,255,255) #couleur blanche en rgb

pygame.init()
surfaceW = 800
surfaceH = 500
ballonW = 50
ballonH = 66
nuageW = 300
nuageH = 300
surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("ballont volant")
horloge = pygame.time.Clock()
img =  pygame.image.load('Ballon01.png')
img_nuage01 = pygame.image.load('NuageHaut.png')
img_nuage02 = pygame.image.load('NuageBas.png')

def score(count):
    police = pygame.font.Font('BradBunR.ttf',16)
    text = police.render("score : " + str(count), True,white)
    surface.blit(text,[10,0])



def nuages(x_nuage , y_nuage, space_nuage):
    surface.blit(img_nuage01,(x_nuage,y_nuage))
    surface.blit(img_nuage02,(x_nuage,y_nuage + nuageH + space_nuage))


def playornot():
    for event in pygame.event.get([pygame.KEYDOWN , pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            quit()
        return event.key
    return None

def write(Text_towrite):
    ttw = pygame.font.Font('BradBunR.ttf',25)
    ttw_surface, ttw_Rect = creaTextObj(Text_towrite, ttw)
    ttw_Rect.center = surfaceW / 2 , ((surfaceH/1.3)+ 50)
    surface.blit(ttw_surface,ttw_Rect)

def creaTextObj(text, Police):
    textSurface = Police.render(text,True,white)
    return textSurface,textSurface.get_rect()

def message(text):
    Big_text = pygame.font.Font('BradBunR.ttf', 150)
    small_text = pygame.font.Font('BradBunR.ttf', 20) 
    BigtextSurface, BigtextRect = creaTextObj(text,Big_text)
    BigtextRect.center = surfaceW/2 , ((surfaceH/2)-50)
    surface.blit(BigtextSurface,BigtextRect)
    SmalltextSurface, SmalltextRect = creaTextObj("press a ESC to quit or a key to continue", small_text) 
    SmalltextRect.center =  surfaceW / 2 , ((surfaceH/2)+50)
    surface.blit(SmalltextSurface,SmalltextRect)

    pygame.display.update()
    time.sleep(0.1)
    while playornot() == None :
        horloge.tick() 
    
    main()

def The_end(T_TEXT):
    message(T_TEXT)

def ballon(x,y,image):
    surface.blit(image,(x,y)) 

def main():
    x = 150
    y = 200
    y_mouv = 0
    x_mouv = 0
    x_nuage = surfaceW
    y_nuage = randint(-200,10)
    space_nuage = ballonH * 2
    nuages_speed = 6
    actual_score = 0  
    gameOver = False
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_mouv = -7
            else:
                y_mouv = 7
        y += y_mouv
        surface.fill(blue)
        ballon(x,y,img)
        nuages(x_nuage,y_nuage,space_nuage)
        score(actual_score)
        x_nuage -= nuages_speed
            
        if y > surfaceH - 40 or y < -10:
            The_end("THE END")

        

        if x + ballonW > x_nuage + 40:
                if y < y_nuage + nuageH -40:
                    if x-ballonW < x_nuage + nuageW -20:
                        The_end("THE END")
        if x + ballonW > x_nuage + 40:
            if y + ballonH > y_nuage + nuageH + space_nuage + 40:
                if x - ballonW < x_nuage + nuageW - 20:
                    The_end("THE END") 
        if x_nuage < (-1 *nuageW):
            x_nuage = surfaceW
            y_nuage = randint(-300,10)
        if x_nuage <= (x-nuageW) <= x_nuage + nuages_speed:
            actual_score += 1
        if actual_score < 2:
                write("BOD corporation")
        if actual_score >= 5 and actual_score <= 10:
            nuages_speed = 10
            space_nuage = ballonH * 2
            write("STEP 2")

        if actual_score >= 15:
            space_nuage = ballonH * 1.6
            write("ENDLESS")


            
        pygame.display.update()

main()
pygame.run()
quit()

