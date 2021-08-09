from typing import MutableMapping
import pygame
import sys
import os
import time
pygame.font.init()
pygame.mixer.init()
sys.path.append(".")
from snake import snake
from food import food

class App:
    
    def __init__(self):
        self.running = False
        self.clock = None
        self.FPS = None
        self.snake = None
        self.food = None
        self.score = None
        self.database =   None
        self.scoreBoard = []
        self.musicOn = False

        self.opening_music = pygame.mixer.Sound('material/snake_jazz1Hour.ogg')
        self.runningMusic =pygame.mixer.music.load('material/Monkeys-Spinning-Monkeys.ogg')
        self.EndingMusic = pygame.mixer.Sound('material/Directed by Robert B. Weide.ogg')
        self.crashMusic = pygame.mixer.Sound('material/hit.wav')

        self.screen = None
        

        self.ending_background = pygame.image.load('material/realEnding.png')
        self.opening_background = pygame.image.load('material/realOpening.png')
        self.background = pygame.image.load('material/Background.png')

    def run(self):
        self.init()
        self.opening()
        pygame.mixer.music.play(-1)
        self.musicOn = True
        while self.running: 
            self.update() 
            self.render()
        self.cleanUp()
        
        

    def init(self):
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Snake")

        self.score = 0
        self.FPS = 20
        self.difficulty = 'Easy'
        
        self.database =   open('scores.txt','r+')
        self.scoreBoard = [int(i) for i in self.database.read() if i!=' ']
        
        
        self.snake = snake(self.screen)
        self.food = food(self.screen)
        self.clock = pygame.time.Clock()
        self.running = True

    def update(self):
        ls = pygame.event.get()
       
        self.events()

        self.snake.moveSnake(ls)
        
        self.mute(ls)
        self.difficulty1(ls)
        self.eat()

        
        
    def events(self):
        ls = pygame.event.get()
        for event in ls:
            if event.type == pygame.QUIT:
                self.running = False
         


    def render(self):
        self.clock.tick(self.FPS)
        self.screen.blit(self.background,[0,0])
        self.snake.displaySnake()
        self.food.drawFood()
        
        #score system
        self.show_score((234,45,44),'Grind Typeface',60)

        #checking if game is over(snake collide or out of grid)
        if self.snake.OverConditions():
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(self.crashMusic)
            time.sleep(1)
            self.game_over()
          

        pygame.display.flip()


    def eat(self):
        if abs(self.snake.body[0][0] - self.food.position[0]) <= 17 and \
            abs(self.snake.body[0][1] - self.food.position[1]) <= 17:
            self.food.position = self.food.place_food()
            self.score += 1
            self.snake.grow()
        
        

    def cleanUp(self):
        pygame.quit()
  
    def game_over(self):
        self.database.write(str(self.score)+' ')

        pygame.mixer.Sound.play(self.EndingMusic)
        my_font1 = pygame.font.SysFont('Grind Typeface', 80)
        
        score_surface = my_font1.render(f'Your Score: {self.score}', True, (0,0,0))
        score_rect = score_surface.get_rect()
        score_rect.midtop = (200,0)


        arg  = 0
        if len(self.scoreBoard) > 0:
            if max(self.scoreBoard) > self.score:
                 arg = max(self.scoreBoard)
            else:
                arg = self.score
        else:
            arg = self.score 
        score_surface1 = my_font1.render(f'Personal Best: {arg}', True, (0,0,0))
        score_rect1 = score_surface.get_rect()
        score_rect1.midtop = (200, 80)


        while True:
            self.screen.blit(self.ending_background,[0,0])
            self.screen.blit(score_surface,score_rect)
            self.screen.blit(score_surface1,score_rect1)
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.stop(self.EndingMusic)
                    self.run()
        
    def show_score(self ,color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (1200/10, 15)
        self.screen.blit(score_surface, score_rect)

    def difficulty1(self,ls):
        for event in ls:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                if self.FPS>30:
                    self.FPS = 20
                else:
                    self.FPS+=5
     
    
    def opening(self):
    
        pygame.mixer.Sound.play(self.opening_music)
        while True:
            self.screen.blit(self.opening_background,[0,0])      
            pygame.display.flip()
            ls = pygame.event.get()
            for event in ls:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    pygame.mixer.Sound.stop(self.opening_music)
                    return 

    def mute(self,ls):
        for event in ls:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    if self.musicOn:
                        pygame.mixer.music.stop()
                        self.musicOn = False
                    else:
                        pygame.mixer.music.play()
                        self.musicOn = True



                     

   

if __name__ == "__main__":
    app = App()
    app.run()