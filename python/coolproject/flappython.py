import pygame

pygame.init()

surfaceW = 800
surfaceH = 500

surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("ballont volant")
gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
pygame.QUIT()
quit()

