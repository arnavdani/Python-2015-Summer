import pygame, sys 

class Bullet(object):

    def __init__(self,width, height,x,y,dx,dy,
                 image, displaySurface):
        #how fast to left to right
        self.dx = dx
        #how fast to move up and down
        self.dy = dy
        self.displaySurface = displaySurface
        self.rect = pygame.Rect(x, y, width, height) 				      
        #Image to display as bullet
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey( pygame.Color("White"))
        self.image = pygame.transform.scale(self.image, 
                                            (width,height))

    def draw(self):
        self.displaySurface.blit(self.image,
                                 [self.rect.x ,self.rect.y ])		      

    def move(self):
        #add the move amount to the current
        #postion to move the bullet
        self.rect.y = self.rect.y + self.dy	   
        self.rect.x = self.rect.x + self.dx

    def checkCollision(self,rect):
        #if the bullet hit 
        #this rect return true
        return self.rect.colliderect(rect) 

    def shotMissed(self):
        #is it off top or left of screen	
        if self.rect.y < 0 or self.rect.x < 0 :
            return True
        #is it off bottom
        elif self.rect.x > self.displaySurface.get_rect().width:
            return True
        #is it off right
        elif self.rect.y > self.displaySurface.get_rect().height:
            return True
        #it must still be on the screen
        else:
            return False