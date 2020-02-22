import pygame,os,sys
from pygame.locals import *
sys.path.append(os.environ['USERPROFILE'] + '\Documents\Student Start\Python\MyClasses')
from Colors import Colors
from Screen import Screen
from Score import Score
from Level import Level
from Lives import Lives
from Ball import Ball
from Paddle import Paddle
from Brick import Brick




#Main function has all 
def main():
    #initialize all imported pygame modules
    pygame.init()
    #create the main screen
    screen = Screen('Break it!',
                    'img/star.png',
                    'img/outerspace.png',
                    600,
                    600,
                    Colors.WHITE)
    score = Score(450, 25,Colors.FIREBRICK, 1,
          "sounds/BonusChime.ogg", screen.Surface)
    #create a lives object'
    lives = Lives(50,25,3,"img/heart3.png", screen.Surface)
    level = Level(230, 25,Colors.AQUAMARINE, 40, screen.Surface)
    #create a ball object
    paddle = Paddle(160, 30, Colors.DEEPSKYBLUE,"sounds/beep4.ogg",screen.Surface)
    ball = Ball(40, 0, 0, 600, 600,"img/earth-icon.png","sounds/BonusSymbol.ogg",screen.Surface)
    #list of colors for brick
    colors = [Colors.RED, Colors.BLUE, Colors.GREEN, Colors.YELLOW]
    values = [100, 75, 50, 25]
    #create bricks
    bricks = Brick.createBricks(17, 100, 4, 10, 2,
                                colors, values, 
                                55, 20, screen.Surface)
    
    #rate to increase speed
    speedLevel = 15
    #initialize clock
    clock = pygame.time.Clock()
    
    #indicates if the game is paused
    paused = False
    #set the variable that controls the main game loop
    playing = True
    while playing:
        #maintain a frame rate of 100 fps
        clock.tick(100)
        #the events since last time
        for event in pygame.event.get():
            #if the user clicks exit stop playing
            if event.type == QUIT:
                playing = False
            if event.type == KEYDOWN:
                if event.key == K_q:
                    playing = False
                if event.key == K_p:
                    paused = not paused
                if  event.key == K_LEFT:
                    #move left
                    paddle.setMoveLeft()
                    #move right
                if event.key == K_RIGHT:
                    paddle.setMoveRight()
                
                    
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    paddle.stop()
                
        #move and draw only if the pause feature is off
        if not paused:
            #update and move things
            ball.move()
            paddle.move()
            
            #check for paddle hit
            if ball.checkCollision(paddle.rect):
                paddle.playSound()
                score.addScore(100)
                
            #if ball leaves screen
            if ball.lost():
                ball.reset()
                lives.subtractLives(1)
                if lives.getLives() ==0:
                    if screen.restartPrompt("img/GameOver4.png"):
                        lives.reset()
                        score.resetScore()
                       
                        
            #loop through all the bricks
            for brick in bricks:
                #is there a collision?
                if(brick.checkBallCollision(ball)):
                    if score.addScore(brick.value):
                        lives.addLives(0)
                if brick.gone:
                    bricks.remove(brick)
                    if level.addPartialLevel(1):
                        bricks = Brick.createBricks(17, 100, 4, 10, 2,
                                                    colors, values, 
                                                    55, 20, screen.Surface)  
                        ball.reset()
                              
                
            
    
            #draw things
            #draw screen first so it does nor overwrite other objects
            #screen.draw
            
            screen.draw()
            score.draw()
            lives.draw()
            level.draw()
            paddle.draw()
            ball.draw()
            #loops through all the bricks
            for brick in bricks:
                brick.draw()
            
            
            #update the changes to show on the main screen
            pygame.display.update()
            
            
    #Uninialize all pygame modules that have previously beeen inialized
    pygame.quit()
    
#run the main method when the file is called directly
if __name__=='__main__':
    main()
