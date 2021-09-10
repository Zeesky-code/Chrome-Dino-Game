import pygame
from dinosaur import Dinosaur
pygame.init()

size = width,height = 640,480
gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('Chrome Dino')
GROUND_HEIGHT = height -100

black = 0,0,0
white = 255,255,255
xPos = 0
yPos = 0

dinosaur = Dinosaur(GROUND_HEIGHT)
lastFrame = pygame.time.get_ticks()

while True:
    t = pygame.time.get_ticks()
    deltaTime = (t-lastFrame)/1000.0
    lastFrame = t
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dinosaur.jump()

    gameDisplay.fill(black)

    dinosaur.update(deltaTime)
    dinosaur.draw(gameDisplay)
    
    pygame.draw.rect(gameDisplay, white, [0, GROUND_HEIGHT, width, height-GROUND_HEIGHT])
    pygame.display.update()