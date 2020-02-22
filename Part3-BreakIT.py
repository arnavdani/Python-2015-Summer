import pygame, sys, os
from pygame.locals import *
sys.path.append(os.environ['USERPROFILE']
                +'\Documents\Student Start\Python\MyClasses')  
#Import our classes
from Screen import Screen 
from Colors import Colors 
from Score import Score
from Level import Level
from Lives import Lives
from Ball import Ball
from Paddle import Paddle
#Main function has all code for the game loop 
def main():
    #initialize all imported pygame modules
    pygame.init()    
    #create the main screen
    screen = Screen('Break IT', 'img/star.png', 
                    'img/outerspace.png',600, 600,Colors.WHITE)

    #Create a score object
    score = Score(450, 25,Colors.GOLD , 2500, 
                  "sounds/BonusChime.ogg", screen.surface)	

    #Create a lives object
    lives = Lives(50, 25, 3,"img/heart3.png", screen.surface)	

    #Create a level object
    level = Level(230, 25,Colors.GOLD, 40, screen.surface)

    #Create a paddle object
    paddle = Paddle(80, 20, Colors.AQUAMARINE,
                    "sounds/beep1.ogg", screen.surface)	
    #Create Ball here
    ball = Ball(40, 0, 0, 600, 600,"img/star.png",
                "sounds/beep4.ogg", screen.surface)	



    #Initialize clock
    clock = pygame.time.Clock() 	
    #indicates if the game is paused
    paused = False	
    #set the variable that controls the main game loop
    playing = True
    #start the game loop
    while playing:    
        #maintain a frame rate of 100 fps
        clock.tick(100)	
        #get all the events since last time 
        #the events were checked
        for event in pygame.event.get():
            #if the user click exit stop playing	    
            if event.type == QUIT:
                playing = False			
            #if this is a keydown (pressing down of a key) 
            if event.type == KEYDOWN:
                if event.key == K_q:
                    playing = False	
                #switch the pause feature on or off	
                if event.key == K_ESCAPE:
                    paused = not paused	
                #set the paddle to move to the left	
                if event.key == K_LEFT:
                    paddle.setMoveLeft()					
                #set the paddle to move to the right		
                if event.key == K_RIGHT:
                    paddle.setMoveRight()
            #if this is a keyup (the player release 
            #the key so it is no longer down) 
            if event.type == KEYUP:
                #since the player released the key 
                #the paddle should be stationary
                if event.key == K_LEFT or event.key == K_RIGHT:
                    paddle.stop()  
        #move and draw only
        #if pause feature off	
        if not paused:

            #update and move things
            ball.move()
            paddle.move()   
            #Check for paddle hit
            if ball.checkCollision(paddle.rect):
                paddle.playSound()
                score.addScore(10)
            #if the ball leaves the screen
            if ball.lost():
                ball.reset()			
                lives.subtractLives(1)	
                if lives.getLives() == 0:				
                    #we are out of lives check for restart
                    if screen.restartPrompt("img/GameOver4.png"):
                        lives.reset()
                        score.reset()
                    else:
                        playing = False	
               


            #draw things
            #draw screen first so it does not
            #overwrite other objects
            screen.draw()
            score.draw()
            lives.draw()
            level.draw()
            ball.draw()
            paddle.draw()


            #update the changes to 
            #show on the main screen
            pygame.display.update()



    #Uninitialized all pygame modules that
    #have previously been initialized
    pygame.quit()	    

#run the main method 
#when this file is called directly
if __name__ == '__main__':
    main()	







