import pygame, sys
from pygame.locals import *
from Colors import Colors 


class Screen(object):
    
    #Initializes the Screen object 
    #(called when it is first created) 
    def __init__(self,caption,iconImageFile,backgroundImageFile,
                 width,height,color):
        #how high the screen is vertically  
        self.height = height
        #how wide the screen is horizontally
        self.width = width 
        # the background if no image is used
        self.color = color
        #create the playing surface screen
        self.surface = pygame.display.set_mode((width , height))		
        #set the caption for the window
        pygame.display.set_caption(caption)
        #if an image was given for the icon
        #load it an add it to the display
        if iconImageFile != None:
            #load the image from file           
            icon = pygame.image.load(iconImageFile)
            #set the icon for the window
            pygame.display.set_icon(icon)        
        #if no image was given set image to None 
        if backgroundImageFile == None:
            #no image to load set background to None           
            self.background_image = None
        else:
            #load image provide so set it for the background
            self.background_image = pygame.image.load(backgroundImageFile).convert()
            #resize it to match the window size
            self.background_image = pygame.transform.scale(self.background_image,
                                                           (width,height))
            
    def draw(self):
        # if no background image fill with color 
        if self.background_image == None:
            self.surface.fill(self.color)
        else:
            #copy Background image to screen:
            self.surface.blit(self.background_image,  [0, 0])    
    
              
    def restartPrompt(self,image):
        #keep the loop going       
        waiting = True
        #load the image with the prompt
        image = pygame.image.load(image).convert()
        image.set_colorkey(Colors.WHITE)          
        #keep going util player gives an answer
        while waiting:               
            #blit the prompt image on the main surface
            self.surface.blit(image, [60 ,200])
            pygame.display.update()        
            #get an game events
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    #if the user hit N the want to play again
                    if event.key == K_n:
                        return False
                     #if the user hit Y the want to play again
                    if event.key == K_y :
                        return True            
        