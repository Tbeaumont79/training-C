import pygame
import pygame.gfxdraw
from pygame.locals import *
import time
from random import *
blue = (113,117,227)
white = (255,255,255) #couleur blanche en rgb
yellow = (255,206,51)
orange = (255,141,51)
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




def timer(length):
    running = True
    start = time.time()
    test = 0
    while running:
        surface.fill(blue)
        pygame.gfxdraw.box(surface,(600,350,150,50),[0,0,255])
        write("Play",677,377,25)
        write("welcome to my game press enter to play the game",350,450,25)
        if test < 5:
            write(test,400,250,100) 
        if time.time() - start >= length:
            print ("Time's up!")
            running = False

        else:
            print("Only %.1f more seconds!" % (length - (time.time() - start)))
            test +=1
        pygame.display.update()
    return (length-(time.time() - start))
        


def main_menu():
    intro = True
    test = 0
    while intro:
        surface.fill(blue)
        pygame.gfxdraw.box(surface,(600,350,150,50),[0,0,255])
        write("Play",677,377,25)
        write("welcome to my game press enter to play the game",350,450,25)
 
        for event in pygame.event.get([pygame.KEYDOWN , pygame.KEYUP, pygame.QUIT]):
            if event.type == pygame.QUIT:

                pygame.quit()
                quit()
            elif event.type == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

                main()
            elif event.type == pygame.KEYUP:
                continue

            
            return event.key
        pygame.display.update()
   
        





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
            main_menu()
 
        return event.key
    return None

def write(Text_towrite,W_pos,H_pos,Lsize):
    Text_towrite = str(Text_towrite)
    ttw = pygame.font.Font('BradBunR.ttf',Lsize)
    ttw_surface, ttw_Rect = creaTextObj(Text_towrite, ttw)
    ttw_Rect.center = W_pos ,H_pos
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
    SmalltextSurface, SmalltextRect = creaTextObj("press a ESC to go to the main menue or a key to continue", small_text) 
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
    space_nuage = ballonH * 3
    nuages_speed = 6
    actual_score = 0  
    gameOver = False


    while not gameOver:
        
               
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                y_mouv = -7
            else:
                y_mouv = 7
               

        
  
        surface.fill(blue)
        ballon(x,y,img)
        nuages(x_nuage,y_nuage,space_nuage)
        score(actual_score)

        x_nuage -= nuages_speed
        y += y_mouv      

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
            write("BOD corporation",500,200,25)
        if actual_score >= 5 and actual_score <= 10:
            nuages_speed = 8
            space_nuage = ballonH * 2
            write("STEP 2",200,200,25)
            surface.fill(yellow)
            ballon(x,y,img)
            nuages(x_nuage,y_nuage,space_nuage)
            score(actual_score)
            pygame.display.update()


        if actual_score > 10:
            surface.fill(orange)
            ballon(x,y,img)
            nuages(x_nuage,y_nuage,space_nuage)
            score(actual_score)
            pygame.display.update()
        if actual_score >= 15:
            space_nuage = ballonH * 1.6 
            write("ENDLESS",200,200,25)
            nuages_speed = 7

        pygame.display.update()


main_menu()
main()
pygame.run()
quit()

