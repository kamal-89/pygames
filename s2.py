
import pygame
import random

from pygame.constants import WINDOWHITTEST
x=pygame.init()

#colors
white = (255, 255 , 255)
red = (255,0,0)
black =(0,0,0)

screen_width = 1000
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width , screen_height ))

background = pygame.image.load("wp.png").convert()
pygame.display.set_caption("SnakesbyKamal")
pygame.display.update()

#game specific variable
exit_game = False
game_over = False
snake_x = 50
snake_y = 60
snake_size = 30
velocity_x = 0
velocity_y = 0
food_x = random.randint(30, screen_width/1.25)
food_y = random.randint(30, screen_height/1.25)
score = 0
init_velocity =5
fps = 60

clock =pygame.time.Clock()
font = pygame.font.SysFont(None , 50)
def text_screen(text , color , x ,y):
    screen_text = font.render(text, True , color)
    gameWindow.blit(screen_text , [x,y])


#gameloop
while not exit_game:

    
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT :
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y =0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity_x -= init_velocity
                velocity_y =0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocity_y -= init_velocity
                velocity_x =0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                velocity_y += init_velocity
                velocity_x =0


    snake_x += velocity_x
    snake_y += velocity_y

    if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<20 :
        score +=1
        
        
        food_x = random.randint(30, screen_width/1.25)
        food_y = random.randint(30, screen_height/1.25)

    
    gameWindow.fill((0,0,0))
    gameWindow.blit(background , [0,0])
    text_screen("Score : " +str(score*10) , red , 5 , 5)
    pygame.draw.rect(gameWindow, red , [food_x , food_y , snake_size, snake_size  ])
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y , snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
