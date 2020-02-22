import pygame, sys 
from pygame.locals import *

class Particle(object):

    #Initalizes the paritcle object (called when it is first created) 
    def __init__(self,X,Y,size,deltaX,deltaY,color, displaySurface):
        #surface to display the particle on
        self.displaySurface = displaySurface
        #color to make the particle
        self.color = color
        #how fast it moves on the X axis
        self.deltaX = deltaX
        #how far it moves on the Y axis
        self.deltaY = deltaY
        #create the particle rectangle
        self.rectangle = pygame.Rect(X,Y, size , size)

    #function to draw the particle image on the displaysurface 	
    def draw(self):
        #draw the particle
        pygame.draw.rect(self.displaySurface, 
                         self.color, self.rectangle)
        #move the particle so it is in a 
        #new location next time we draw
        self.rectangle.x = self.rectangle.x + self.deltaX
        self.rectangle.y = self.rectangle.y + self.deltaY	

    def setColor(self,color):
        #color to make the particle
        self.color = color		