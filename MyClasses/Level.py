import pygame, sys
from pygame.locals import *

class Level(object):

    def __init__(self,xPos,yPos,color,newLevelAmount,displaySurface):
        #color to display level in 		
        self.color =  color
        #postion to display level at
        self.xPos = xPos
        self.yPos = yPos
        #surface to display the level on
        self.displaySurface = displaySurface
        #font to use for displaying text
        self.font= pygame.font.SysFont(None, 30)
        #make the font bold
        self.font.set_bold(True)
        #start level at 1
        self.level = 1
        #set the amount needed to Increase level
        self.newLevelAmount = newLevelAmount
        #current amount of level completed
        self.currentPartComplete = 0
        #current amount of level completed
        self.initialnewLevelAmount = newLevelAmount             

    #get the current level		
    def getLevel(self):
        return self.level        

    def setLevelIncreaseAmount(self,newLevelAmount):
        #set the amount needed to Increase level
        self.newLevelAmount = newLevelAmount

    def getLevelIncreaseAt(self):
        #get the amount needed to Increase level
        return self.newLevelAmount            

    #get the percent complete of the current level	
    def getPercentComplete(self):
        #return the current percentage complete
        return int(100* self.currentPartComplete/self.newLevelAmount) 

    def reset(self):
        #reset the level to 1
        self.level  = 1	
        #reset the partial level to 0
        self.currentPartComplete = 0   
        #Reset the amount need to increase level 
        self.newLevelAmount = self.initialnewLevelAmount        

    #reset the current part level complete to 0
    def resetCurrentLevel(self):
        #reset the partial level to 0
        self.currentPartComplete = 0   	

    def setColor(self,color):
        #color to display level in 		
        self.color =  color

    #increase the level 
    def increaseLevel(self): 
        self.level = self.level + 1        
        #reset the partial level to 0
        self.currentPartComplete = 0       

    #Add to the partial level
    def addPartialLevel(self, increaseBy):
        #add to the amount of how much of the current level is complete
        self.currentPartComplete = self.currentPartComplete + increaseBy
        #if the current partial level is now equal/greater to the complete value
        if self.currentPartComplete >= self.newLevelAmount:
            self.increaseLevel()	
            return True	
        else:
            return False    

    #Displays the current level on the screen
    def draw(self):
        strLevel = '   Level ' + str(self.level)
        #create the surface with the text on it
        resultSurf = self.font.render(strLevel, True, self.color)
        #display the levle on the main surface
        self.displaySurface.blit(resultSurf,(self.xPos,self.yPos))    