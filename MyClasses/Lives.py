import pygame, sys
from pygame.locals import * 
from Colors import Colors

class Lives(object):

    def __init__(self,xPos,yPos,defaultLives,image,displaySurface):

        #set the position to draw the image
        self.xPos = xPos
        self.yPos = yPos
        #set the surface to draw image on
        self.displaySurface = displaySurface
        #set the current number of lives
        self.lives = defaultLives
        #set the default number of lives
        self.defaultLives = defaultLives	
        #load the image to display
        self.image = pygame.image.load(image).convert()
        #set the color the is transparent
        self.image.set_colorkey(Colors.WHITE)
        #convert the image for quicker display
        self.image = pygame.transform.scale(self.image, (40,40))	

    #return the current number of lives
    def getLives(self):
        return self.lives

    #Add to the number of lives
    def addLives(self,increaseLives):
        self.lives = self.lives + increaseLives

    #subtract from the number of lives
    def subtractLives(self,decreaseLives):
        self.lives = self.lives - decreaseLives 
        if self.lives < 0:
            self.lives = 0

    #reset the number of lives
    def reset(self):
        self.lives = self.defaultLives

    #Displays the current number of lives images on the screen
    def draw(self):
        for x in range(0, self.lives):
            self.displaySurface.blit(self.image,
                                     [self.xPos + x*20,self.yPos])
            