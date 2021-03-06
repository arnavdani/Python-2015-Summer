import pygame, sys
from pygame.locals import *
from Colors import Colors 
from Screen import Screen

class Paddle(object):

    #Initializes the Screen object 
    #(called when it is first created)  
    def __init__(self,width,height,color,soundFile,displaySurface):     
        #the color to make the paddle 		
        self.color = color
        #how far to move each game tick 	
        self.moveAmount = 4
        #width of the paddle
        self.width = width
        #height of the paddle
        self.height = height
        #the maximum x postion
        self.xMax = displaySurface.get_size()[0]
        #the minimum x postion
        self.xMin = 0 		
        #surface to draw the paddle on
        self.displaySurface = displaySurface
        #set the paddle to be stationary
        self.stop()
        #the paddle rectangle
        self.rect = pygame.Rect((self.xMax)/2,
                                displaySurface.get_size()[1] -20,
                                width, height)
        #set sound to play it hits wall
        self.sound = pygame.mixer.Sound(soundFile)
    def draw(self):
        #draw the rectangle on the surface
        pygame.draw.rect(self.displaySurface,
                         self.color , self.rect)

    def setColor(self,color):
        #change the paddle color
        self.color = color     

    def setMoveLeft(self):
        #set the paddle to move left
        self.moveLeft = True
        self.moveRight = False

    def setMoveRight(self):
        #set the paddle to move right
        self.moveRight = True
        self.moveLeft = False	

    def stop(self):
        #set the paddle to stationary
        self.moveLeft = False
        self.moveRight = False		

    def setWidth(self,width):
        #change the width
        self.width = width
        #recreate paddle rectangle
        self.rect = pygame.Rect(self.rect.x, self.rect.y,
                                self.width, self.height)

    def setHeight(self,height):
        #change the height
        self.height = height
        #recreate paddle rectangle
        self.rect = pygame.Rect(self.rect.x, self.rect.y,
                                self.width, height)    

    def move(self):
        #if the paddle is set to move left 
        #and it is not at the left edge of screen 
        if self.moveLeft and self.rect.x > self.xMin :
            #move the position of the rectangle left
            self.rect.x -=  self.moveAmount
        if self.moveRight and self.rect.x + self.width < self.xMax :
            #move the position of the rectangle left 
            self.rect.x +=  self.moveAmount		
            
    def playSound(self):
        #play the sound of the paddle
        self.sound.play()