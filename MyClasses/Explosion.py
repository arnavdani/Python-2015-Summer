import pygame, sys
from pygame.locals import *
from Particle import Particle


class Explosion(object):
    
        #Initalizes the paritcle object (called when it is first created) 
        def __init__(self,X,Y,size,duration,color, sound, displaySurface):
        
                self.duration = duration
                self.particles = list()
                self.particles.append(Particle(X, Y, size, 1, 1, color, displaySurface))
                self.particles.append(Particle(X, Y, size, 1, -1, color, displaySurface))
                self.particles.append(Particle(X, Y, size, 1, 0, color, displaySurface))
                self.particles.append(Particle(X, Y, size, -1, 1, color, displaySurface))
                self.particles.append(Particle(X, Y, size, -1, -1, color, displaySurface))
                self.particles.append(Particle(X, Y, size, -1, 0, color, displaySurface)) 
                self.particles.append(Particle(X, Y, size, 0, 1, color, displaySurface))
                self.particles.append(Particle(X, Y, size, 0, -1, color, displaySurface))  
                #Play Sound if it is not none (there is a sound to play)

                if sound != None:
                        pygame.mixer.Sound(sound).play()   
                        
        #function to draw the particle image on the displaysurface 	
        def draw(self):
                if self.duration > 0:
                        self.duration = self.duration - 1
                        #draw all the particles
                        for particle in self.particles:
                                particle.draw()      
                                
        def setColor(self,color):
                #draw all the particles
                for particle in particles:
                        particle.color(color)
                        
        #see if the explosion duration is over                
        def ended(self):
                return self.duration <= 0                        
                                