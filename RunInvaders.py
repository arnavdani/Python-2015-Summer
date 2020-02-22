import pygame, sys, os
from pygame.locals import *
sys.path.append(os.environ['USERPROFILE']+'\Documents\Student Start\Python\MyClasses')
#IMPORT CLASSES
from Screen import Screen
from Colors import Colors
from Score import Score
from Level import Level
from Lives import Lives
from Bullet import Bullet
from Explosion import Explosion
from Invader import Invader
from BattleGun import BattleGun
import random

#main function
def main():
    pygame.init()
    #create screen
    screen = Screen('Space Invaders!', 'img/lightning.png',
                    'img/outerspace.png', 700, 700, Colors.WHITE)
    score = Score(450, 25, Colors.BLUE, 2500,"sounds/BonusChime.ogg", screen.Surface)
    #create lives
    lives = Lives(50,25,3,"img/shield.png", screen.Surface)
    #level
    level = Level(230,25,Colors.YELLOW,70,screen.Surface)
    #gun
    gun = BattleGun(80, 20, Colors.AQUAMARINE, 50,
                    "sounds/Laser_Shoot.ogg",screen.Surface)
    #list of bullets
    bullets = list()
    #the explosion colors = 
    colors = [Colors.YELLOW, Colors.RED, Colors.GREEN, Colors.BLUE]
    #the In leg images
    imageIns = ["img/CyanIn.png","img/PurpleIn.png","img/RedIn.png","img/smallInLeg1.png"]
    #the out images
    imageOuts = ["img/CyanOut.png","img/PurpleOut.png","img/RedOut.png","img/smallOutLeg1.png"]
    #the score values
    values = [200, 150, 100, 50]
    #create list of attacking invaders
    invaders = Invader.createInvaders(17,100,4,15,5,20,20,
                                       "img//lightning.png","sounds//shortbreak.ogg",
                                       colors, imageIns, imageOuts, values, screen.Surface)
    alienBullets = list()
    clock = pygame.time.Clock()
    #indicates if the game is paused
    paused = False
    #set var to control game loop
    playing = True
    #start game
    while playing:
        #maintain 100 fps
        clock.tick(100)
        for event in pygame.event.get():
            #if user click exit
            if event.type == QUIT:
                playing = False
            if event.type == KEYDOWN:
                if event.key == K_q:
                    playing = False
                if event.key == K_p:
                    paused = not paused
                #set gun to move left
                if event.key == K_LEFT:
                    gun.setMoveLeft()
                #move right
                if event.key == K_RIGHT:
                    gun.setMoveRight()
                if event.key == K_SPACE:
                    #if gun can fire
                    if gun.reloadCount ==0:
                        #add new bullet
                        bullets.append(gun.fire())
                if event.key == K_n:
                    event.type == QUIT
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    gun.stop()
                
                    
                    
                
                    

        #move and draw if not paused
        if not paused:
            
            #update + move things
            gun.move()
            for bullet in bullets:
                bullet.move()
                if bullet.shotMissed():
                    bullets.remove(bullet)
            for bullet in alienBullets:
                bullet.move()
                if bullet.shotMissed():
                    alienBullets.remove(bullet)
                if bullet.checkCollision(gun.rect):
                    alienBullets.remove(bullet)
                    lives.subtractLives(1)
            Invader.moveGroup(invaders)
            for invader in invaders:
                if random.randrange(5000)<2:
                    alienBullets.append(invader.fire())
                for bullet in bullets:
                    if bullet.checkCollision(invader.rect):
                        bullets.remove(bullet)
                        if score.addScore(invader.value):
                            lives.addLives(1)
                        invader.hit() 
            if len(invaders) == 0:
                level.increaseLevel()
                invaders = Invader.createInvaders(17,100,4,15,5,20,20,
                                                  "img//lightning.png","sounds//shortbreak.ogg",
                                                  colors, imageIns, imageOuts, values, screen.Surface)
                Invader.speed = level.getLevel()*2
                Invader.numberDestroyed = 0
            
            if Invader.landed or lives.lives == 0:
                if screen.restartPrompt("img//GameOver4.png"):
                    lives.reset()
                    invaders = Invader.createInvaders(17,100,4,15,5,20,20,
                                       "img//lightning.png","sounds//shortbreak.ogg",
                                       colors, imageIns, imageOuts, values, screen.Surface)
                    
      
        
                
                
           
            #draw things screen first so not overide other objects
            screen.draw()  
            score.draw()
            lives.draw()
            level.draw()
            gun.draw()
            for bullet in bullets:
                bullet.draw()
            for bullet in alienBullets:
                bullet.draw()            
            
            Invader.moveGroup(invaders)
            
                        
            for invader in invaders:
                if invader.gone:
                    invaders.remove(invader)
                else:
                    invader.draw()           
            #update changes on screen
            pygame.display.update()
    #uninitialize pygame mods have have benn inited
    pygame.quit()
#run main when called directly
if __name__=='__main__':
    main()
            
                    