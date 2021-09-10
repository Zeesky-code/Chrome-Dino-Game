import pygame
pygame.init()

size = width,height = 640,480
gameDisplay = pygame.display.set_mode(size)
GROUND_HEIGHT = height -100

black = 0,0,0
white = 255,255,255
xPos = 0
yPos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, white, [0, GROUNDHEIGHT, width, height-GROUND_HEIGHT])
    xPos += 1
    yPos +=1

    pygame.display.update()