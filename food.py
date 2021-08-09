import pygame
import random


class food:
    def __init__(self,screen):
        self.looks = pygame.image.load('material/Apple.png').convert_alpha()
        self.icon = pygame.transform.scale(self.looks,(17,17))
        self.size = 10
        self.screen = screen
        self.position = self.place_food()

    def place_food(self):
        return (random.randint(100,1000),random.randint(100,600))
    
    def drawFood(self):
        self.screen.blit(self.icon,self.position)


        
    
