import pygame, sys, os
from pygame.locals import *
sys.path.append(os.environ['USERPROFILE']
                +'\Documents\Student Start\Python\MyClasses')  
#Import our Explosion class
from Explosion import Explosion 

class Brick(object):

    def __init__(self, xPos, yPos, width, height,
                 color, value, displaySurface):
        #the color this brick will be
        self.color = color
        #the width this brick will be
        self.width = width
        #the height this brick will be
        self.height = height
        #the surface to draw this brick on
        self.displaySurface = displaySurface
        #this brick's rectangle
        self.rect = pygame.Rect(xPos, yPos, width, height)
        #set the point value of this brick
        self.value = value
        #this brick is not broken
        self.broke = False
        #Has this brick's explosion ended?
        self.gone = False


    def hit(self):
        #set true to indicate the brick was hit 
        self.broke = True
        #create explosion to draw instead of brick rectangle
        self.explosion = Explosion(self.rect.centerx, self.rect.centery,
                                   4, 25,self.color,
                                   "sounds/shortbreak.ogg", self.displaySurface)

    def draw(self):
        #if this brick is not hit
        if not self.broke:
            #draw the brick rectangle  
            pygame.draw.rect(self.displaySurface,
                             self.color , self.rectangle)	
        else:
            # check to see if the explosion has ended   
            if self.explosion.ended():
                # set gone to show is completely gone
                self.gone = True				
            else:
                #the explosion is still going on draw it    
                self.explosion.draw()

    def createBricks(startX, startY, rows, cols, spacing, colors,
                     values, width, height, displaySurface ):
        #create a list to hold the bricks
        bricks = list()
        #go through the number of cols requested
        for col in range(0,cols):
            #go through the number of cols requested
            for row in range(0,rows):
                brick = Brick(startX + col*(width+spacing), 
                              startY+row*(height+spacing), width, height,
                              colors[row],values[row] ,displaySurface)	
        #return the list of
        #bricks just created        
        return bricks

    def checkBallCollision(self, ball):

        #if this brick isn't already 
        #broken see if the ball hit it
        if self.rect.colliderect(brick.rect) and not brick.broke : 
            # have the ball bounce (reverse)
            ball.dy = ball.dy * -1 
            #reposition the ball to the edge of the brick 
            if(ball.dy > 0 ):
                ball.rect.y = self.rect.y + self.rect.width/2 
            else:
                ball.rect.y = self.getRect().y 
            #the brick is broken now
            self.hit()
            return True
        else:
            #no collision return false      
            return False

