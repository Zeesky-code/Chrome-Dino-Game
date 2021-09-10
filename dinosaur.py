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
        