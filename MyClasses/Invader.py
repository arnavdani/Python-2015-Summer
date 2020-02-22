import pygame, sys, os
from pygame.locals import *
sys.path.append(os.environ['USERPROFILE']
                +'\Documents\Student Start\Python\MyClasses')
#Import our classes
from Bullet import Bullet
from Explosion import Explosion 
from Colors import Colors 


class Invader(object):
    #static variables
    down = 0
    left = True
    moveCounter = 0
    numberDestroyed = 0
    speed = 0
    moveAmount = 4
    landed = False
    MaxY = 600
    MaxX = 600

    def __init__(self, xPos, yPos, width, height, color,
                 value, displaySurface, imageIn, imageOut,
                 bulletImage, destroySound):

        #the explosion color for the invader
        self.color = color
        #surface to draw the invader on
        self.displaySurface = displaySurface	
        #create the rectangle for the invader 
        self.rect = pygame.Rect(xPos, yPos, width, height)
        #points score for destroying this invader
        self.value = value
        #indicates if this invader has been shot
        self.damaged = False
        #indicates if this invader has completely blown up
        self.gone = False	
        #image for bullets
        self.bulletImage = bulletImage
        #sound to play when blown up
        self.destroySound = destroySound  
        #converted surface will have the same pixel format as the displaySurface
        self.legIn = pygame.image.load(imageIn).convert(displaySurface)
        #make white transparent in the image
        self.legIn.set_colorkey(Colors.WHITE)
        #Resizes the Surface to a new resolution
        self.legIn = pygame.transform.scale(self.legIn, (width, height))
        #set the image to start animation on
        self.currentImage = self.legIn
        #converted surface will have the same pixel format as the displaySurface
        self.legOut = pygame.image.load(imageOut).convert(displaySurface)
        #make white transparent in the image
        self.legOut.set_colorkey(Colors.WHITE)
        #Resizes the Surface to a new resolution
        self.legOut = pygame.transform.scale(self.legOut, (width, height))
        
    def draw(self):
        if not self.damaged:
            #draw this current image on the surface 
            self.displaySurface.blit(self.currentImage,
                                     [self.rect.x ,self.rect.y])
        else:
            # check to see if the explosion has ended   
            if self.explosion.ended():
                # set gone to show is completely gone
                self.gone = True				
            else:
                #the explosion is still going on draw it    
                self.explosion.draw()

    def move(self):
        #if the group is moving down
        #move the position down
        if Invader.down > 0:
            self.rect.y = self.rect.y +  Invader.moveAmount
        #if the group is moving left move the position left
        elif Invader.left:
            self.rect.x = self.rect.x - Invader.moveAmount
        #not down or left so move right
        else:
            self.rect.x =  self.rect.x + Invader.moveAmount	

    def fire(self):
        #return a bullet headed down 
        #from the center of this invader
        return Bullet(14, 14, self.rect.centerx,
                      self.rect.centery,0, 2,
                      self.bulletImage, self.displaySurface) 	

    def hit(self):
        #indicates this invader is hit
        self.damaged = True
        #increase the speed of all the Invaders
        Invader.speed = Invader.speed + 2
        #increase the number of Invaders destroyed
        Invader.numberDestroyed = Invader.numberDestroyed + 1
        #change the amount moved based on how many destroyed
        #increase 1 for every 5 Invaders destroyed
        Invader.moveAmount = int(Invader.numberDestroyed/5) + 4
        #create an explosion to draw instead of the invader image
        self.explosion = Explosion(self.rect.centerx,    
                                   self.rect.centery, 4, 15, self.color, 
                                   self.destroySound, self.displaySurface)

    def moveGroup(invaders):
        #increase the counter  
        Invader.moveCounter = Invader.moveCounter + 1
        #used to find the larget x coord for all the Invaders
        maxXpos = 0
        #used to find the smallest x coord for all the Invaders
        minXpos = 1000
        #if we have reached the number actually move
        if Invader.moveCounter >= (125 - Invader.speed): 
            #reset the move counter 
            Invader.moveCounter = 1
            #loop through all the invaders
            for invader in invaders:
                #switch the image to the opposite
                if invader.currentImage == invader.legOut:
                    invader.currentImage = invader.legIn
                else:
                    invader.currentImage = invader.legOut
                #check if this invader is at the bottom
                if  invader.rect.y > Invader.MaxY:
                    Invader.landed = True
                #if this is larger than the current value update the max	
                if maxXpos < invader.rect.x:
                    maxXpos = invader.rect.x
                #if this is smaller than the current value update the min		
                if minXpos > invader.rect.x:
                    minXpos = invader.rect.x					
            #if this is a down move decrease the number of down moves left
            if Invader.down > 0:
                Invader.down -= 1
            else:
                #if we are going left and the 
                #leftmost invader is less than 25
                #start moving down instead
                if Invader.left and minXpos < 25 :
                    Invader.left = False
                    Invader.down = 3
                #if the rightmost invader is more
                #than the max start moving left instead				
                if not Invader.left and maxXpos + 45 > Invader.MaxX :
                    Invader.left = True
                    Invader.down = 3
            #now that we have figured out the 
            #direction move all the invaders	
            for invader in invaders:
                invader.move()        

    def createInvaders(startX, startY, rows, cols, spacing, width,
                       height, bulletImage, destroySound,colors,
                       imageIns, imageOuts, values, displaySurface):
        # the list of invaders to return
        invaders = list()	
        #create all the invaders
        for col in range(0, cols):
            for row in range(0, rows):		 
                invader = Invader(startX + col*(width + spacing),
                                  startY+row*(height + spacing), 
                                  width, height, colors[row],values[row],  
                                  displaySurface, imageIns[row],
                                  imageOuts[row], bulletImage, 
                                  destroySound)
                invaders.append(invader)
        return invaders
