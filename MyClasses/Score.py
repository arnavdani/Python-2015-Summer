import pygame, sys
from pygame.locals import *

class Score(object):

	def __init__(self,xPos,yPos,color,bonusEvery,
	             bonusSound,displaySurface):                  
		#set color of score
		self.color = color
		#set postion to display score on surface 
		self.xPos = xPos
		self.yPos = yPos				
		#surface to draw score on
		self.displaySurface = displaySurface
		#font to use   
		self.font= pygame.font.SysFont(None, 30)
		#set font to bold
		self.font.set_bold(True)
		#set initial score to 0
		self.score = 0                
		#set the amount bonus will happen at
		self.bonusEvery = bonusEvery
		#set first bonus level
		self.bonusScore = bonusEvery
		#set sound to play when a bonus is reached
		self.bonusSound = pygame.mixer.Sound(bonusSound)      
		#create the surface with the "Score" text on it
		self.scoreTextSurf = self.font.render('   Score ', True, self.color)
			
	#subtract from score
	def subtractScore(self,decreaseScore):
		self.score = self.score - decreaseScore

	#Add to the score
	def addScore(self,increaseScore):
		self.score = self.score + increaseScore
		#check if we have reached a bonus level
		if self.score >= self.bonusScore:
			#increase the bonus to the next higher level
			self.bonusScore += self.bonusEvery
			#play bonus
			self.bonusSound.play()
			#return a true value to indicate a bonus
			return True
		#since we reached this point not a bonus yet
		return False                

	#set the score to a certain score
	def setScore(self,score):
		self.score = score  
		self.bonusScore =  self.score + self.bonusEvery   

	#reset the score back to zero
	def resetScore(self):
		self.score  = 0	
		#set first bonus level
		self.bonusScore = self.bonusEvery          

	def setColor(self,color):
		#color to display level in 		
		self.color =  color


	#displays the current score on the screen
	def draw(self):
		#display the text Score rectangle on the main surface
		self.displaySurface.blit(self.scoreTextSurf,(self.xPos,self.yPos))
		#turn the numeric score into a string
		strScore = str(self.score)
		#create the surface with the text on it (zfill makes it at least 8 numbers)
		scoreSurf = self.font.render('%s' %(strScore.zfill(8)), True, self.color)
		#display the text rectangle on the main surface
		#(yPos+20) so it is below "Score" text
		self.displaySurface.blit(scoreSurf,(self.xPos,self.yPos + 20))	        