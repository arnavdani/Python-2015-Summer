import pygame, sys
from pygame.locals import *
from Colors import Colors

class Screen(object):
    
    #Inializes the Screen object
    #(called when it's first created)
    def __init__(self, caption, iconImageFile, backgroundImageFile, 
                 width, 
                 height, 
                 color):
        
        #how high the screen is vertically
        self.height = height
        #how wide the screen is horizontally
        self.width = width
        #the background if no image is used
        self.color = color
        #create the playing surface screen
        self.Surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        #if there is an icon image
        if iconImageFile != None:
            #load the image from the file
            icon = pygame.image.load(iconImageFile)
            #set the icon for the window
            pygame.display.set_icon(icon)
        #if no image was given
        if backgroundImageFile == None:
            #no image to load. Set background to None
            self.background_image = None
        else:
            #load image provided; set it for the background
            self.background_image = pygame.image.load(backgroundImageFile).convert()
            #resize it to match the window size
            self.background_image = pygame.transform.scale(self.background_image,
                                                           (width, height))
        
            
    def draw(self):
        #if no background image fill with color
        if self.background_image == None:
            self.Surface.fill(self.color)
        else:
            #copy Background image to screen
            self.Surface.blit(self.background_image, [0, 0])
            
    def restartPrompt(self, image):
        #keep the loop going
        waiting = True
        #load the image with the prompt
        image = pygame.image.load(image).convert()
        image.set_colorkey(Colors.WHITE)
        while waiting:
            print ('test')
            self.Surface.blit(image, [60, 200])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    #if the user hit the N they don't want to play again
                    if event.key == K_n:
                        return False
                    if event.key == K_y:
                        return True
                    
                    