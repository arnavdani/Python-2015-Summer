import pygame, sys
from pygame.locals import *
from Colors import Colors 

class Ball(object):

    #Initializes the Screen object 
    #(called when it is first created)      
    def __init__(self,size,xMin,yMin,xMax,yMax,imageFile,
                 wallSoundFile,displaySurface):
        #left edge of screen
        self.xMin = xMin
        #right edge of screen
        self.xMax = xMax - size
        #top edge of screen
        self.yMin = yMin
        #bottom edge of screen
        self.yMax = yMax - size
        #right of movment left to right
        self.dx = -2
        #right of movment left to right
        self.dy = -4
        #size of ball
        self.size = size
        #surface to draw ball on
        self.displaySurface = displaySurface
        #rectangle for collisions
        self.rect = pygame.Rect((xMin+xMax)/2,(yMax+yMin)/2,
                                size-1, size-1)         
        #set up image for ball and create rect
        self.setImage(imageFile)
        #set sound to play it hits wall
        self.wallsound = pygame.mixer.Sound(wallSoundFile)
     
       
    def draw(self):
        #draw the ball image to the main screen
        self.displaySurface.blit(self.image,
                                 [self.rect.x ,self.rect.y])
   
    def setImage(self,imageFile):
        #save the file name of the ball image
        self.imageFile = imageFile
        #load the image from the file
        self.image = pygame.image.load(imageFile).convert()
        #set the color to be transparent
        self.image.set_colorkey(Colors.WHITE)
        #scale the image to the correct size 
        self.image = pygame.transform.scale(self.image,
                                            (self.size,self.size)) 
        #create the rectangle used for collision/position
        self.rect = pygame.Rect(self.rect.x,self.rect.x,
                                self.size-1, self.size-1)        
        
    def setSize(self,size):
        #change the size
        self.size = size
        #call the set image to resize
        #image and rectangle
        self.setImage(self.imageFile)     
        
    def move(self):
        #move the ball based on current speed 
        self.rect.x =  self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy        
        #if hitting right wall
        if self.rect.x > self.xMax :
            #set the postion to the max
            self.rect.x = self.xMax
            #reverse the direction
            self.dx = self.dx * -1
            #play the sound
            self.wallsound.play()      
        #if hitting left wall
        if self.rect.x < self.xMin :
            #set the postion to the min
            self.rect.x = self.xMin
            #reverse the direction
            self.dx = self.dx * -1
            #play the sound
            self.wallsound.play() 
        #if hitting top wall
        if self.rect.y < self.yMin :
            #set the postion to the min
            self.rect.y = self.yMin
            #reverse the direction
            self.dy = self.dy * -1
            #play the sound
            self.wallsound.play() 
 
    def lost(self):
        #if the ball is below max y 
        if self.rect.y > self.yMax:
            return True
        else:
            return False
        
    def checkCollision(self,rect):
        #if the ball is below max y 
        if self.rect.colliderect(rect) and self.dy > 0: 
              self.dy = self.dy * -1            
              return True
        else:
              return False
      

    def increaseSpeed(self):
        #if we are moving left
        if self.dx > 0:
            self.dx += 5
        else: # we are moving right
            self.dx -= 5           
        #if we are moving down    
        if self.dy > 0:
            self.dy += 5
        else:# we are moving up
            self.dy -= 5
               
    def reset(self):
        #reset values to orignal speed
        self.dx = -2
        self.dy = -4	
        #reset values to original center position
        self.rect.x = (self.xMin+self.xMax)/2
        self.rect.y = (self.yMax+self.yMin)/2     