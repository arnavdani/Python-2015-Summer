 import pygame, sys
from pygame.locals import *

#Height of game window
WINDOW_HEIGHT = 700
#Width of our game window
WINDOW_WIDTH = 700

#Height of width of the game ball
BALL_SIZE = 15
#Color of game ball
YELLOW = pygame.Color("Yellow")
ORANGE = pygame.Color("Red")

#Start Main Function
def main():
    #initialize all imported pygame modules
    pygame.init()
        #create the playing surface screen
    mainSurface = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
        #set the caption for the window
    pygame.display.set_caption('Space Pong! Woohoo!')
    #load image for the background
    background_image = pygame.image.load("img/space.gif").convert()
    #resize it to match the window size
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    #set positions of graphics
    background_position = [0, 0]

    #create the rectangle that is the ball
    ball = pygame.Rect(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, BALL_SIZE, BALL_SIZE)
    #create the rectangle that is the paddle
    paddle = pygame.Rect(WINDOW_WIDTH/2,
                         WINDOW_HEIGHT -40, 80, 20)
    #set the variable that controls
    #the main game loop
    playing=True
    
    #Initialize clock
    clock = pygame.time.Clock()  
    #set the variable that controls
    #the main game loop
    playing=True
    #set the paddle to not move
    paddleMove = 0
    #variables to control movement of ball
    ballDx = 3
    ballDy = 3
    #start the game loop
    
    while playing:
            clock.tick(90)
            #get all the events since last
            #time the events were checked
            for event in pygame.event.get():
                if event.type == QUIT:
                    playing = False
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        playing = False
                #set the paddle to move to the left
                    if event.key == K_LEFT:
                        paddleMove = -7
                #set the paddle to move to the right
                    if event.key == K_RIGHT:
                        paddleMove = 7 
            #if  this is a keyup(the player releases the key so the paddle shouldn't move)
                if event.type == KEYUP:
                    #since the player released the key
                    #the paddle should be stationary
                    if event.key == K_a or event.key == K_d:
                        paddleMove = 0
            #if the ball is moving upward(ballDy < 0)
            #and it's going off the top of the board
            #(y-coordinate < 0) reverse it's direction
            if ball.y <= 0 and ballDy <0:
                ballDy = - ballDy
            
            #if the ball is moving left
            #and off the board (x < 0)
            if ball.x <= 0 and ballDx < 0:
                ballDx = - ballDx
            if ball.x >= WINDOW_WIDTH - BALL_SIZE and ballDx > 0:
                ballDx = -ballDx
            if ball.y >= WINDOW_HEIGHT and ballDy > 0:
                ball.y = 20
            #collision with paddle
            if ball.colliderect(paddle) and ballDy > 0:
                ballDy = - ballDy
            #update the position of the ball
            ball.x = ball.x + ballDx*2
            ball.y = ball.y + ballDy*2            
            #update the position of the paddle
            #paddleMove is for the x-coordinate
            #0 is for the y-coordinate(not changing)
            paddle = paddle.move(paddleMove, 0)
            #copy background image to screen
            mainSurface.blit(background_image,background_position)
            #draw the ball rectangle
            pygame.draw.rect(mainSurface, YELLOW, ball)
            pygame.draw.rect(mainSurface, ORANGE, paddle)
            
            #update the display on the main screen
            pygame.display.update()
                     
                
                        
#run the main method when this file is loaded
if __name__=='__main__':
    main()    
    
    







    
    

