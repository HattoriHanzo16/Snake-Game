import pygame
import random
import time


UP = (0,-17)
DOWN = (0,17)
LEFT =(-17,0)
RIGHT = (17, 0)

class snake:
    def __init__(self,screen):
        self.screen = screen
        self.dir = LEFT
        self.body = [(i, 400) for i in range(300+50, 300+ 76 + 50, 17)]
    
    def displaySnake(self):
        pygame.draw.circle(self.screen,(207, 3, 0),self.body[0],10)
        for piece in self.body[1:]:
            pygame.draw.circle(self.screen,tuple([random.randint(0,255) for _ in range(3)]),piece,10)

        self.body = [(self.body[0][0] + self.dir[0], self.body[0][1] + self.dir[1])] + self.body[:-1]
    
    def moveSnake(self,ls):
        for event in ls:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.dir != UP:
                    self.dir = DOWN
                if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.dir != DOWN:
                    self.dir = UP
                if (event.key == pygame.K_a  or event.key == pygame.K_LEFT) and self.dir != RIGHT:
                    self.dir = LEFT
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.dir != LEFT:
                    self.dir = RIGHT
        
        
    
   
    
    def OverConditions(self):
        if any([i[0]<75 or i[0] > 1200 - 17 - 63 for i in self.body]):
            return True
        if any([i[1]<75 or i[1] > 700 - 17 - 60 for i in self.body]):
            return True
        
        for block in self.body[1:]:
            if self.body[0] == block:
                return True
        return False


        
    def grow(self):
     self.body.append((self.body[-1][0] - self.dir[0],self.body[-1][1] + self.dir[1]))            
                
                
        


                
                



            