import pygame
dinocolour = 255,255,255
DINOHEIGHT = 40
DINOWIDTH = 20

class Dinosaur:
    def __init__(self, surfaceHeight):
        self.x = 60
        self.y = 0
        self.yvelocity = 0
        self.height = DINOHEIGHT
        self.width = DINOWIDTH
        self.surfaceHeight = surfaceHeight
    def jump(self):
        if(self.y == 0):   #so the dino oly jumps when it's on the ground
            self.yvelocity = 300
    def update(self,deltaTime):
        self.yvelocity += -500*deltaTime   #gravity
        self.y +=self.yvelocity*deltaTime
        if self.y < 0:
            self.y = 0
            self.yvelocity =0
    def draw(self,display):
        pygame.draw.rect(display,dinocolour,[self.x,self.surfaceHeight-self.y-self.height,self.width,self.height])